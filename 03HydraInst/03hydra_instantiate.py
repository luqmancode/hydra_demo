import hydra
from omegaconf import DictConfig
import torch
from hydra.utils import instantiate 

class MyClass:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hello(self) -> str:
        return f'Hello {self.name}'

@hydra.main(config_path='.', config_name='config', version_base=None)
def main(config: DictConfig):
    myclass = MyClass(name='John')
    print(myclass.say_hello())

    myclasshydra = instantiate(config.my_class)
    print(myclasshydra.say_hello())

    parameters = torch.nn.Parameter(torch.randn(10, 10))
    partial_optimizer = instantiate(config.optimizer)
    optimizer = partial_optimizer([parameters])
    print(optimizer)
if __name__ == "__main__":
    main()