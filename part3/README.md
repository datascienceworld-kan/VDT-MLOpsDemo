## Orchestrating pipeline using Mflow

This contains the code samples which allow the components to be orchestrated using mlflow

The structure of the components is as follows:

```shell
- datavalidation:
    - MLproject
    - conda.yaml
    - *.py
- featurenegineering:
    - MLproject
    - conda.yaml
    - *.py
- modeltraining:
    - MLproject
    - conda.yaml
    - *.py
MLproject
conda.yaml
config.yaml
run.py
```

1. [Datavalidation](./datavalidation/)

The difference between this component and the one which we created in part 2 is that there is now an MLproject file.

We can run just this component using mlflow by executing the commands as given below

```shell
cd datavalidation
mlflow run . -P train_path=s3://gunmlartifacts/datalake/raw_zone/train.csv -P test_path=s3://gunmlartifacts/datalake/raw_zone/test.csv -P landing_zone_path=s3://gunmlartifacts/datalake/landing_zone/
```
*You might want to change the paths, to paths on your s3 drive.*

The above takes care of creating the relevant conda environment and running our code with the correct set of dependencies.

2. [Featureengineering](./featurenegineering/)

Just like we created the data validation component we can create a feature engineering component as well by creating an `MLproject` file.

To run this component following command will be used

```shell
cd featureengineering
mlflow run . -P validated_train_path=s3://gunmlartifacts/datalake/landing_zone/train.csv -P feature_store_path=s3://gunmlartifacts/feature_store
```
*You might want to change the paths, to paths on your s3 drive.*

3. [Model-training](./modeltraining/s)

Lastly we will include an `MLproject` file for the model training component. We will use the following set of commands to run this component with MLflow.

```shell
cd modeltraining
mlflow run . -P x_path=s3://gunmlartifacts/feature_store/X.npy -P y_path=s3://gunmlartifacts/feature_store/y.npy -P n_estimators=120 -P max_depth=15 -P n_jobs=-1
```
*You might want to change the paths, to paths on your s3 drive.*

Finally we can run all the components together by creating a `MLproject` file in the root of the project folder and create a new `run.py` file to run each component. 

Use the following command to run all the components

```shell
mflow run .
```