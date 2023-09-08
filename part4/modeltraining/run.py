import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, confusion_matrix  
from s3fs.core import S3FileSystem
import argparse
import logging 
import mlflow
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument("--x_path",
                    type=str,
                    help="Path to predictor data")
parser.add_argument("--y_path",
                    type=str,
                    help="path to target vector")
parser.add_argument("--n_estimators",
                    type=int,
                    help="Number of trees in random forest")
parser.add_argument("--max_depth",
                    type=int,
                    help="Max depth of each tree in random forest model")
parser.add_argument("--n_jobs",
                    type=int,
                    help="Number of cpu cores to be used for processing")
def get_s3(s3_path):
    s3 = S3FileSystem()
    return np.load(s3.open(s3_path), allow_pickle=True)

def main(args):
    logging.info("Reading X and y")
    logging.info(f"X on s3 at {args.x_path}, starting download")
    X = get_s3(args.x_path)
    logging.info(f"y on s3 at {args.y_path}, starting download")
    y = get_s3(args.y_path)
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)
    clf = RandomForestClassifier(args.n_estimators,
                                max_depth=args.max_depth,
                                n_jobs=args.n_jobs)
    logging.info("Training the model")
    clf = clf.fit(X_train,y_train)
    preds = clf.predict(X_test)
    pred_proba = clf.predict_proba(X_test)[:,1]
    cm = confusion_matrix(y_test,preds)
    auc=roc_auc_score(y_test,pred_proba)
    t_n, f_p, f_n, t_p = cm.ravel()
    logging.info(f"AUC is {auc} \n TP: {t_p} \n FP: {f_p} \n TN: {t_n} \n FN: {f_n}")
    mlflow.log_metrics({"tn":t_n,'fp':f_p,'fn':f_n,'tp':t_p,"auc":auc})
    mlflow.sklearn.log_model(clf,'rf_model',input_example=X_test[0:,])
    local_path = mlflow.artifacts.download_artifacts(args.x_path)
    mlflow.log_artifact(local_path)
    local_path = mlflow.artifacts.download_artifacts(args.y_path)
    mlflow.log_artifact(local_path)

if __name__=="__main__":
    args=parser.parse_args()
    main(args)
