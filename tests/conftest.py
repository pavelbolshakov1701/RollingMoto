import pytest


@pytest.fixture()
def set_up():
    print('START TEST BUY MOTO!')
    yield
    print('FINISH TEST BUY MOTO!')


@pytest.fixture(scope='module')
def one_moto():
    print('BUY ONLY ONE MOTO')
    yield
    print('FINISH BUY ONLY ONE MOTO')

@pytest.fixture(scope='module')
def some_moto():
    print('BUY SOME MOTOS')
    yield
    print('FINISH BUY SOME MOTOS')