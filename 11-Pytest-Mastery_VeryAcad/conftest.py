import pytest

from pytest_factoryboy import register
from tests.factories import UserFactory, ProductFactory, CategoryFactory

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)

# added after 18:40
@pytest.fixture 
def new_user1(db, user_factory):
    user = user_factory.create()
    return user
