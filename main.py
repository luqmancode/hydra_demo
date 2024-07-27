from omegaconf import OmegaConf, DictConfig
import os

def main() -> None:
    res = OmegaConf.create()
    print(res)
    res1 = OmegaConf.create({
        "some_key": "some_value",
        "random_numbers": [1,3,2,5],
        "some_config": {"nested_key_config": [-1, 34, 22]}
    })
    print(OmegaConf.to_yaml(res1))

    list_inputs = ["new_key", "no_value", "training.batch_size=10", "training.lr=2"]
    res2 = OmegaConf.from_dotlist(list_inputs)
    print(OmegaConf.to_yaml(res2))

    res3 = OmegaConf.load('./config.yaml')
    print(res3)
    print(OmegaConf.to_yaml(res3))

    res4 = OmegaConf.from_cli()
    print(OmegaConf.to_yaml(res4))

    res3.training['scheduler'] = 'Some Schedulsr'
    print(res3.training.scheduler)

    var_conf = OmegaConf.load('./variable-interpolation-config.yaml')
    print(OmegaConf.to_yaml(var_conf, resolve=True))

    os.environ['USER'] = 'luqman'
    os.environ['PASSWORD1'] = 'seecret'
    env_var = OmegaConf.load('./env_variable_config.yaml')
    print(OmegaConf.to_yaml(env_var, resolve=True))


    config1 = OmegaConf.load('./config_to_merge1.yaml')
    config2 = OmegaConf.load('./config_to_merge2.yaml')
    merged_config = OmegaConf.merge(config1, config2)
    merged_config.merge_with_cli()
    print(OmegaConf.to_yaml(merged_config))

if __name__ == "__main__":
    main()