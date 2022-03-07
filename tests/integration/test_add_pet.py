from copy import deepcopy
from assertpy import assert_that
from tests.utils.api_client import Client
from tests.integration.mock_objects import NEW_PET_OBJECT_1


# test add new pet - expected 200
def test_add_pet():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    data.pop('id')
    NEW_PET_OBJECT_1.pop('id')
    assert_that(data).is_equal_to(NEW_PET_OBJECT_1)


# test add pet without name - expected 405 invalid input
def test_add_pet_without_name():
    client = Client()
    NEW_PET_OBJECT_1_without_name = NEW_PET_OBJECT_1.copy()
    NEW_PET_OBJECT_1_without_name.pop('name')

    res = client.add_pet(NEW_PET_OBJECT_1_without_name)
    # name is mandatory in the requirements - add without name return 200 and not 405 invalid input
    assert_that(res.status_code).is_equal_to(405)


# test add pet without photo - expected 405 invalid input
def test_add_pet_without_photo():
    client = Client()
    NEW_PET_OBJECT_1_without_photo = NEW_PET_OBJECT_1.copy()
    NEW_PET_OBJECT_1_without_photo.pop('photoUrls')

    res = client.add_pet(NEW_PET_OBJECT_1_without_photo)
    # photo is mandatory in the requirements - add without photo return 200 and not 405 invalid input
    assert_that(res.status_code).is_equal_to(405)


# test add 2 pets in different categories name but same category id - expected 200 ,server should change the category id
def test_add_pet_different_categories_with_same_category_id():
    client = Client()
    pet_1 = deepcopy(NEW_PET_OBJECT_1)
    pet_2 = deepcopy(NEW_PET_OBJECT_1)

    # change the category name only for pet 2 but stay with same id (0)
    pet_2['category']['name'] = 'different name'

    # create the pets
    res_1 = client.add_pet(pet_1)
    res_2 = client.add_pet(pet_2)

    # verify the successfully added
    assert_that(res_1.status_code).is_equal_to(200)
    assert_that(res_2.status_code).is_equal_to(200)

    pet_1_data = res_1.json()
    pet_2_data = res_2.json()

    # the category name and id of pet_1 and pet_2 should be different
    assert_that(pet_1_data['category']['name']).is_not_equal_to(pet_2_data['category']['name'])
    assert_that(pet_1_data['category']['id']).is_not_equal_to(pet_2_data['category']['id'])
