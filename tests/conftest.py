import pytest


def pytest_addoption(parser):
    """option setting for pytest"""
    parser.addoption("--id", action="store", default="client id for spotipy")
    parser.addoption("--secret",
                     action="store",
                     default="client secret for spotipy")

# pylint: disable=redefined-builtin
@pytest.fixture(scope="session")
def id(request):
    """make fixture with command arguments"""
    val = request.config.option.id
    if val is None:
        pytest.skip()
    return val


@pytest.fixture(scope="session")
def secret(request):
    """make fixture with command arguments"""
    val = request.config.option.secret
    return val
