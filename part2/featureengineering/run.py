import os
import argparse
import logging
import pandas as pd
import pickle
from s3fs.core import S3FileSystem
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
parser = argparse.ArgumentParser()
parser.add_argument("--validated_train_path",
                    type=str,
                    help="path to validated train file")
parser.add_argument("--feature_store_path",
                    type=str,
                    help="path to landing zone base directory")

def load_s3(s3_path,arr):
    s3 = S3FileSystem()
    with s3.open(s3_path, 'wb') as f:
        f.write(pickle.dumps(arr))

def main(args):
    logging.info("Reading validated data")
    df = pd.read_csv(args.validated_train_path)
    X = df.drop(['id','booking_status'],axis=1).values
    y = df['booking_status'].values
    load_s3(os.path.join(args.feature_store_path,"X.npy"),X)
    load_s3(os.path.join(args.feature_store_path,"y.npy"),y)
    logging.info("Saved data engineered artifacts")

if __name__=="__main__":
    args = parser.parse_args()
    main(args)
