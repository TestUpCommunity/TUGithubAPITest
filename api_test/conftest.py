import pytest, os
from Environment import Env
from configparser import ConfigParser

@pytest.fixture(scope="module", autouse=True)
def env():
    config = ConfigParser()
    config.read('data.ini')
    api_root_url=config[os.environ['env']]['api_root_url']
    yield Env(api_root_url=api_root_url,token=os.environ['token'])

@pytest.fixture(scope="module", autouse=True)
def just_print():
    print("我只是打印一段文本")