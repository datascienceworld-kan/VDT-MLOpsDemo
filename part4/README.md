## Preparing tracking infrastructure

1. Create s3 buckets
2. Run a postgres sql server as metric store:

I am using a docker image and creating a postgres server as given below

```shell
docker run --name pg14 -e POSTGRES_PASSWORD=gun125 -p 5432:5432 -d postgres:latest
```

This will create a docker container named `pg14`

You can connect to it using psql

```shell
psql -U postgres -h localhost
```
Once you hit enter just give the password, in this case its `gun125`. Once you are connected to your postgres instance create a database named `mlflow` as given below:

```sql
CREATE DATABASE mlflow;
```

Finally you can run the mlflow tracking server as given below

```shell
mlflow server --backend-store-uri postgresql://postgres:gun125@localhost:5432/mlflow --default-artifact-root s3://gunmlartifacts/project1/ --no-serve-artifacts
```

You can then point your browser to `localhost:5000` to see the tracking server in action.

## Final mlflow pipeline

We have made changes to the `modeltraining` component, by including the `mlflow.log()` statements in our training script.

To run our final project we will need to do the following:
```shell
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
mlflow run . --experiment-name=hotel_occupancy
```

Also notice the only changes in `part4/modeltraining/run.py` are the inclusion of `mlflow.log()` statements compared `part3/modeltraining/run.py`