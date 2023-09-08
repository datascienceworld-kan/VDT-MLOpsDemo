import pandas as pd
from utils import SchemaTest,SchemaTrain
import argparse
import logging
import os
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
parser = argparse.ArgumentParser()
parser.add_argument("--train_path",
                    type=str,
                    help="path to the training data to be validated")
parser.add_argument("--test_path",
                    type=str,
                    help="path to the testing data to be validated")
parser.add_argument("--landing_zone_path",
                    type=str,
                    help="path to the landing zone")

def main(args):
    logging.info("Reading train and test files")
    train = pd.read_csv(args.train_path)
    test = pd.read_csv(args.test_path)
    logging.info("Validating train and test data")
    try:
        SchemaTrain.validate(train)
    except:
        logging.error("Train data validation failed")
        raise Exception("Stopping execution as validation failed")
    try:
        SchemaTest.validate(test)
    except:
        logging.error("Test data validation failed")
        raise Exception("Stopping execution as validation failed")
    logging.info("Finished data validation and now storing data to landing zone")
    test_path = os.path.join(args.landing_zone_path,"test.csv")
    train_path = os.path.join(args.landing_zone_path,"train.csv")
    train.to_csv(train_path,index=False)
    test.to_csv(test_path,index=False)
    logging.info("Train and test data saved in landing zone")

if __name__=="__main__":
    args = parser.parse_args()
    main(args)