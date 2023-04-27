import pytest


@pytest.fixture()  # обрабатывается каждый раз при вызове
def set_up():
    print("\n Start test")
    yield
    print("\n Finish test")


@pytest.fixture(scope="module")  # обрабатывается один раз для всего файла
def set_group():
    print("\n Enter system")
    yield
    print("\n Exit system")
