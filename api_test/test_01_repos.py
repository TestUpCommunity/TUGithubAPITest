import pytest


def test_list_all_public_repos(env):
    r = env.github.repos.list_all_public_repos()
    assert r.status_code == 200, "status_code should be 200 but actually={}".format(r)
    assert r.content[0].get('id') == 1
    assert r.content[0].get('name') == 'grit'
    assert r.content[0].get('private') == False

def test_list_organization_repos_number(env):
    r = env.github.repos.list_organization_repos("TestUpCommunity")
    assert r.status_code == 200, "status_code should be 200 but actually={}".format(r)
    assert len(r.content) == 2


def test_list_organization_repos_name(env):
    r = env.github.repos.list_organization_repos("TestUpCommunity")
    assert r.status_code == 200, "status_code should be 200 but actually={}".format(r)
    assert r.content[0].get('name') == "TUGithubAPI"
    assert r.content[1].get('name') == "TUGithubAPITest"

if __name__ == '__main__':
    pytest.main()