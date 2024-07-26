from omegaconf import OmegaConf, DictConfig
import hydra 

@hydra.main(config_path=None)
def main(config: DictConfig) -> None:
    res = OmegaConf.to_yaml(config)
    print(res)


if __name__ == "__main__":
    main()