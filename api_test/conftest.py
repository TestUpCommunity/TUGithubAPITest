import pytest, os
from Environment import Env


@pytest.fixture(scope="module", autouse=True)
def env():
    yield Env(token=os.environ['token'])

@pytest.fixture(scope="module", autouse=True)
def just_print():
    print("我只是打印一段文本")