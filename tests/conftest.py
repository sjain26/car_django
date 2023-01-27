import pytest

from pytest_factoryboy import register
from tests.factories import UserFactory, CarListFactory, BuyerFactory
from django.contrib.auth.models import User

register(UserFactory)
register(CarListFactory)
register(BuyerFactory)


@pytest.fixture()
def test_product(db, car_list_factory):
    product = car_list_factory.create()
    print(product.description)
    assert True


@pytest.fixture
def user1(db, user_factory):
    user = user_factory.create()
    print(user)
    return user


@pytest.fixture
def new_user1(db, car_list_factory):
    user = car_list_factory.create()
    print(user)
    return user


@pytest.fixture
def test_buyer(db, buyer_factory):
    product = buyer_factory.create()
    print(product.buyer_name)
    assert True


@pytest.fixture
def adminuser(db, user_factory):
    new_admin = user_factory.create(
        username="admin_user",
        is_staff=True,
        is_superuser=True)
    return new_admin
