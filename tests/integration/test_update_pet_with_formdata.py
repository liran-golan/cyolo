from assertpy import assert_that
from tests.utils.api_client import Client
from tests.integration.mock_objects import NEW_PET_OBJECT_1


# test update pet neme and status by POST API
def test_update_pet():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_update = client.post('/pet/' + str(data['id']), 'name=boby&status=sold')
    assert_that(res_update.status_code).is_equal_to(200)

    res_get = client.get('/pet/' + str(data['id']))
    data_get = res_get.json()
    data['name'] = 'boby'
    data['status'] = 'sold'
    assert_that(data_get).is_equal_to(data)


# test update pet that not exist - expected 404 not found
def test_update_pet_that_not_exist():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_update = client.post('/pet/' + str(data['id'] + 1), 'name=boby&status=sold')
    assert_that(res_update.status_code).is_equal_to(404)


# test update pet with invalid inputs (name1,status1) - expected 405 invalid input
def test_update_pet_with_ivalid_input():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_update = client.post('/pet/' + str(data['id']), 'name1=boby&status1=sold')
    # didn'd update and get 200
    assert_that(res_update.status_code).is_equal_to(405)
