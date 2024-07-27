from omegaconf import OmegaConf, DictConfig
import hydra

@hydra.main(config_path='.', config_name='config')
def main(config: DictConfig):
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()