import pytest


def pytest_addoption(parser):
    parser.addoption("--id", action="store", default="client id for spotipy")
    parser.addoption("--secret", action="store", default="client secret for spotipy")


@pytest.fixture(scope="session")
def id(request):
    val = request.config.option.id
    if val is None:
        pytest.skip()
    return val


@pytest.fixture(scope="session")
def secret(request):
    val = request.config.option.secret
    return val
