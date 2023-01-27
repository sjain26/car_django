# import pytest
# from seller.models import CarList


# @pytest.mark.parametrize(
#     "seller_name ,seller_mobile,model_name, description,condtion_car, asking_price,manufactured_date, validity",
#     [
#         ("NewTitle", 1111, "New_model", "slugdescription", "E", 45871,"2022-12-22", True),
#        # ("NewTitle", 1111, "NewDescription", "slugdestricption", "E",48651, "2022-12-29", False),
#     ]
# )
# def test_list_instance(
#     db, car_list_factory,seller_name, seller_mobile,model_name, description,condtion_car,asking_price, manufactured_date, validity
# ):

#     test = car_list_factory(
#         seller_name=seller_name,
#         seller_mobile=seller_mobile,
#         model_name=model_name,
#         description=description,
#         condtion_car=condtion_car,
#         asking_price=asking_price,
#         manufactured_date=manufactured_date,
#     )

#     item = CarList.objects.all().count()
#     print(item)
#     assert item == validity
    
    
#     def test_sm(test_car_list_instance):
#         print(test_car_list_instance)


