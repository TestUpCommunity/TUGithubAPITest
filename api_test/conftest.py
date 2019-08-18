import pytest, os, sys

parent=os.path.dirname
libraries=parent(parent(__file__))+os.sep+"libraries"
api=parent(parent(parent(__file__)))+os.sep+"TUGithubAPI"
if libraries not in sys.path:
    sys.path.append(libraries)
if api not in sys.path:
    sys.path.append(api)


from Environment import Env
from configparser import ConfigParser

@pytest.fixture(scope="module", autouse=True)
def env():
    config = ConfigParser()
    config.read('../data/data.ini')
    api_root_url=config[os.environ['env']]['api_root_url']
    yield Env(api_root_url=api_root_url,token=os.environ['token'])

