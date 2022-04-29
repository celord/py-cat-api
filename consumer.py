from the_cat_api.cat_api import TheCatApi
from the_cat_api.models import *
catapi = TheCatApi()
result = catapi.get_kitty()
result = catapi.get_clowder_of_kitties(amt=6)
print(result)

# from the_cat_api.rest_adapter import RestAdapter
# from the_cat_api.models import *
# catapi = RestAdapter()
# my_params = {'limit': 5}
# result = catapi.get("/images/search", ep_params=my_params)
# print(result.data)
