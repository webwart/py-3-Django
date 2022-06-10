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

def test_new_user(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff 