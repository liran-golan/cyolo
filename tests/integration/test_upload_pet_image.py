import os
from assertpy import assert_that
from tests.utils.api_client import Client
from tests.integration.mock_objects import NEW_PET_OBJECT_1

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'image.png')

# test upload_pet_image - expected 200
def test_upload_pet_image():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_upload = client.post('/pet/' + str(data['id']) + '/uploadImage', files={'file': ('file1', open(file_path, 'rb'))})
    assert_that(res_upload.status_code).is_equal_to(200)

# test upload pet image with bad request - expected 415 Unsupported Media Type
def test_upload_pet_image_without_inputs():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_upload = client.post('/pet/' + str(data['id']) + '/uploadImage' )
    assert_that(res_upload.status_code).is_equal_to(415)


# test upload_pet_image - expected 400 Error: Bad Request
# strange! according the swagger this one and the first one should swap??
def test_upload_pet_image_with_bad_request():
    client = Client()
    res = client.add_pet(NEW_PET_OBJECT_1)
    assert_that(res.status_code).is_equal_to(200)

    data = res.json()
    res_upload = client.post('/pet/' + str(data['id']) + '/uploadImage',headers={'Content-Type': 'multipart/form-data'}, files={'file': ('file1', open(file_path, 'rb'))})
    assert_that(res_upload.status_code).is_equal_to(400)