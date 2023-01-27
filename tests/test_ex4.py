# import pytest
# from django.contrib.auth.models import User
# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True

# def test_set_check_password1(user_1):
#     print('check-user1')
#     assert user_1.username == "test-user"

# def test_set_check_password2(user_1):
#     print('check-user2')
#     assert user_1.username == "test-user"

# def test_new_user(new_user1):
#     print(new_user1.model_name)
#     #assert new_user.first_name == "MyName"

# # def test_new_user2(new_user2):
# #     print(new_user2.is_staff)
# #     assert new_user2.is_staff

# def test_new_user1(new_user1):
#     print("-------------------",new_user1.seller_name)
#     assert True


# def test_user1(user_factory):
#     user= user_factory.build()
#     print(user.username)
#     assert True
    
# def test_new_1(car_list_factory):
#     user = car_list_factory.build()
#     print(user)
#     return user


# def test_buyer(buyer_factory):
#     product = buyer_factory.build()
#     print(product.buyer_name)
#     assert True


# def test_admin_str(adminuser):
#     assert adminuser.__str__() == "admin_user"
    
    

