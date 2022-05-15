import yaml


def read_yaml_config(file_name: str) -> dict:
    config: dict = yaml.load(open(file_name), Loader=yaml.Loader)
    return config


if __name__ == "__main__":
    print(read_yaml_config("example.yaml"))
