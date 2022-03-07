from assertpy import assert_that
from tests.utils.api_client import Client
from tests.integration.mock_objects import NEW_PET_OBJECT_1


# test delete pet by petId - expected 200
def test_delete_pet_by_pet_id():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_delete = client.delete('/pet/' + str(data["id"]))
    assert_that(res_delete.status_code).is_equal_to(200)


# test delete pet that not exist - expected 404 Pet not found
def test_delete_pet_that_not_exist():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_delete = client.delete('/pet/' + str(data["id"] + 1))
    assert_that(res_delete.status_code).is_equal_to(404)


# test delete pet with invalid petId - expected 400 Invalid ID supplied
def test_delete_pet_by_Invalid_pet_id():
    client = Client()

    res_delete = client.delete('/pet/' + 's$$')
    # there is no validation in the server that petId it's int - so we get 404 not found instead of 400 Invalid ID supplied
    assert_that(res_delete.status_code).is_equal_to(400)
