from azure.storage.blob import BlobServiceClient
import config
import uuid


def list_blobs_in_container():
    print('\nListing Blobs In Container')
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        container_client = blob_service_client.get_container_client(config.container_name)
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print("*\t" + blob.name)

    except Exception as e:
        print(e)
        exit()


def upload_blob_to_container():
    print('\nUpload Blob To Container')

    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        blob_client = blob_service_client.get_blob_client(container=config.container_name, blob=str(uuid.uuid4())[0:8]+'.jpg')

        with open('demo_img.jpg', "rb") as data:
            blob_client.upload_blob(data)
    except Exception as e:
        print(e)
        exit()


def download_blob_from_container():
    print('\nDownload Blob From Container')
    try:
        blob_name = input('Enter File Name To Download: ')
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        blob_client = blob_service_client.get_blob_client(container=config.container_name, blob=blob_name)

        file = open('downloaded.jpg', 'wb')
        file.write(blob_client.download_blob().readall())
        file.close()

    except Exception as e:
        print(e)
        exit()


def remove_blob_from_container():
    print('\nRemove Blob From Container')

    try:
        print('Under Development')
    except Exception as e:
        print(e)
        exit()


def init():
    options = ['1', '2', '3', '4']
    msg_1 = '1: List Blobs In Container\n' \
            '2: Upload Blob To Container\n' \
            '3: Remove Blob From Container\n' \
            '4: Download Blob From Container'

    print(msg_1)
    option = input('Enter Option: ')
    if option not in options:
        print('Incorrect Option Entered!')
        exit()

    function_library = {
        '1': list_blobs_in_container,
        '2': upload_blob_to_container,
        '3': remove_blob_from_container,
        '4': download_blob_from_container
    }

    function = function_library[option]
    function()


init()
