import hydra
from omegaconf import DictConfig

@hydra.main(config_name="config",config_path="config",version_base="1.2")
def main(cfg:DictConfig):
    print(cfg.data.train_path)

if __name__=="__main__":
    main()