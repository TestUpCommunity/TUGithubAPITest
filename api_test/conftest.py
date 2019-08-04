import pytest, os
from Environment import Env


@pytest.fixture(scope="module", autouse=True)
def env():
    yield Env(token=os.environ['token'])
