import pytest
from django.contrib.auth.models import User

# @pytest.fixture
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     print('create-user')
#     return user 

# def test_set_check_password1(user_1):
#     print('check-user1')
#     assert user_1.username == "test-user"

# def test_set_check_password2(user_1):
#     print('check-user1')
#     assert user_1.username == "test-user"

# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     return user

# def test_set_check_password(user_1):
#     assert user_1.username == "test-user"

# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == "MyName" 

# def test_new_user(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff 

# def test_new_user(user_factory):  
#     user = user_factory.build()
#     print(user)
#     assert True

# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.create()
#     count = User.objects.all().count()
#     print(count)
#     print(user)
#     assert True
 
# 19:00 

# def test_new_user(new_user1):
#     print(new_user1.username)
#     assert True
 
# 23:00
def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert  True