from assertpy import assert_that
from tests.utils.api_client import Client
from tests.integration.mock_objects import NEW_PET_OBJECT_1, NEW_PET_OBJECT_2, NEW_PET_OBJECT_3


# test update pet category name - expected 200
def test_update_pet_category_name():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)
    data = res.json()

    NEW_PET_OBJECT_edit = NEW_PET_OBJECT_1.copy()
    NEW_PET_OBJECT_edit['category']['name'] = 'Cats'
    res_update = client.put('/pet', json=NEW_PET_OBJECT_edit)
    data_update = res_update.json()
    assert_that(res_update.status_code).is_equal_to(200)

    res_get = client.get('/pet/' + str(data["id"] + 1))
    data_get = res_get.json()
    data_update.pop('id')
    data_get.pop('id')
    assert_that(data_update).is_equal_to(data_get)


# test update pet name- expected 200
def test_update_pet_name():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)
    data = res.json()

    NEW_PET_OBJECT_edit = NEW_PET_OBJECT_1.copy()
    NEW_PET_OBJECT_edit['name'] = 'Boby'
    res_update = client.put('/pet', json=NEW_PET_OBJECT_edit)
    data_update = res_update.json()
    assert_that(res_update.status_code).is_equal_to(200)

    res_get = client.get('/pet/' + str(data["id"] + 1))
    data_get = res_get.json()
    data_update.pop('id')
    data_get.pop('id')
    assert_that(data_update).is_equal_to(data_get)


# test update pet photo name - expected 200
def test_update_pet_photo():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)
    data = res.json()

    NEW_PET_OBJECT_edit = NEW_PET_OBJECT_1.copy()
    NEW_PET_OBJECT_edit['photoUrls'] = ['some-photo-4']
    res_update = client.put('/pet', json=NEW_PET_OBJECT_edit)
    data_update = res_update.json()
    assert_that(res_update.status_code).is_equal_to(200)

    res_get = client.get('/pet/' + str(data["id"] + 1))
    data_get = res_get.json()
    data_update.pop('id')
    data_get.pop('id')
    assert_that(data_update).is_equal_to(data_get)


# same validation for update tags(id/name) and status(but this one found that can be changed to any value ???bug???)

# test update pet photo with wrong syntax - expected 405 Validation exception
def test_update_pet_photo_validation_exception():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    NEW_PET_OBJECT_edit = NEW_PET_OBJECT_1.copy()
    NEW_PET_OBJECT_edit['photoUrls'] = 'some-photo-4'
    res_update = client.put('/pet', json=NEW_PET_OBJECT_edit)
    # update pet with wrong body (photoUrls as string and not list)- get 500 instead of 405 Validation exception
    assert_that(res_update.status_code).is_equal_to(405)


# test update pet photo for pet that not exist - expected 404 Pet not found
def test_update_pet_that_not_exist():
    client = Client()
    res_update = client.put('/pet', json=NEW_PET_OBJECT_2)
    # update pet that not exist return 200 and not 404 Pet not found
    assert_that(res_update.status_code).is_equal_to(404)


# test update pet photo for pet that not exist - expected 400 Invalid ID supplied
def test_update_pet_with_ivalid_id():
    client = Client()
    res_update = client.put('/pet', json=NEW_PET_OBJECT_3)
    # expected 400 Invalid ID supplied - data json with id as a string - get 500!!!
    assert_that(res_update.status_code).is_equal_to(400)
