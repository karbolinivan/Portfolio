import pytest


@pytest.fixture()
def set_up():
    print("\nStatr test")
    yield
    print("\nFinish test")


@pytest.fixture(scope="module")
def set_group():
    print('\nStart test "test buy product"')
    yield
    print('\nEnd test "test buy product"')
