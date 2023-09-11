import mlflow 
import hydra
from omegaconf import DictConfig
import os 

@hydra.main(config_name="config",config_path="conf",version_base="1.2")
def main(cfg:DictConfig):
    base_path = hydra.utils.get_original_cwd()
    _= mlflow.run(uri=os.path.join(base_path,"datavalidation"),
                   entry_point="main",
                   parameters={
                       'train_path':cfg.data.train_path,
                       'test_path':cfg.data.test_path,
                       'landing_zone_path':cfg.data.landing_zone_path
                   })
    _ = mlflow.run(uri=os.path.join(base_path,"featureengineering"),
                   entry_point="main",
                   parameters={
                       'feature_store_path': cfg.data.feature_store_path,
                       'validated_train_path': cfg.data.validated_train_path
                           })
    _ = mlflow.run(uri=os.path.join(base_path,'modeltraining'),
                   entry_point="main",
                   parameters = {
                       "x_path":cfg.data.x_path,
                       "y_path":cfg.data.y_path,
                       "n_estimators":cfg.hyperparams.n_estimators,
                       "max_depth":cfg.hyperparams.max_depth,
                       "n_jobs":cfg.hyperparams.n_jobs
                   })
if __name__=="__main__":
    main()

