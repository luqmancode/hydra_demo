from omegaconf import OmegaConf, DictConfig
import hydra
import os
from hydra.utils import get_original_cwd, to_absolute_path
import logging

logger = logging.getLogger(__name__)

@hydra.main(config_path='.', config_name='config')
def main(config: DictConfig):
    print(OmegaConf.to_yaml(config))
    print("CURRENT_WORKING_DIRECTORY: ", os.getcwd())
    print("BASE PATH: ", get_original_cwd())
    print("File Path(some.txt): ", to_absolute_path('some.txt'))
    logger.info("Some Log message")
    logger.debug("Some debug message")

if __name__ == "__main__":
    main()