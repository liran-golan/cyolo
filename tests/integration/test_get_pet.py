from assertpy import assert_that
from tests.utils.api_client import Client
from tests.integration.mock_objects import NEW_PET_OBJECT_1, NEW_PET_OBJECT_2


# test get pet by petId - expected 200
def test_get_pet_by_pet_id():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_get = client.get('/pet/' + str(data["id"]))
    data_get = res_get.json()
    assert_that(data).is_equal_to(data_get)


# test get pet by status available - expected 200
def test_get_pet_by_status():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    res_get = client.get('/pet/findByStatus?status=available')
    data_get = res_get.json()
    available_pets = 0

    for pet in data_get:
        assert_that(pet['status']).is_equal_to('available')
        available_pets += 1

    assert_that(res_get.status_code).is_equal_to(200)
    assert_that(available_pets).is_greater_than(0)


##################### same validation for status pending/sold #######################################


# test get pet by Invalid status value - expected 400 Invalid status value
def test_get_pet_by_ivalide_status_value():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_2)
    assert_that(res.status_code).is_equal_to(200)

    res_get = client.get('/pet/findByStatus?status=notValid')
    # inavalid status return 200 and not 400 Invalid status value
    assert_that(res_get.status_code).is_equal_to(400)


# test get pet with invalid id - expected 400 Invalid ID supplied
def test_get_pet_with_invalid_petId():
    client = Client()

    res_get = client.get('/pet/s')
    # there is no validation in the server that petId it's int - so we get 404 not found instead of 400 Invalid ID supplied
    assert_that(res_get.status_code).is_equal_to(400)


# test get pet with invalid id - expected 404 Pet not found
def test_get_pet_that_not_exist():
    client = Client()

    res_get = client.get('/pet/-10')
    assert_that(res_get.status_code).is_equal_to(404)
