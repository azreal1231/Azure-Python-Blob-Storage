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


def create_new_blob_container():
    from azure.core.exceptions import ResourceExistsError
    print('\nCreate Blob Container')
    container_name = input('Enter New Container Name: ')
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        new_container = blob_service_client.create_container(container_name)
        properties = new_container.get_container_properties()
    except ResourceExistsError:
        print("Container already exists.")
    except Exception as e:
        print(e)
        exit()


def varify_container_existence():
    from azure.core.exceptions import ResourceNotFoundError
    container_name = input('Enter Container Name: ')

    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        container_client = blob_service_client.get_container_client(container_name)
        for blob in container_client.list_blobs():
            print("Found blob: ", blob.name)
    except ResourceNotFoundError:
        print("\nContainer not found.")
        exit()


def delete_container():
    from azure.core.exceptions import ResourceNotFoundError
    container_name = input('Enter Container Name To Be Removed: ')
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        blob_service_client.delete_container(container_name)
    except ResourceNotFoundError:
        print("Container already deleted.")


def list_all_containers():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.string)
        all_containers = blob_service_client.list_containers(include_metadata=True)
        for container in all_containers:
            print("*\t" + container['name'])
    except Exception as e:
        print(e)
        exit()


def restore_deleted_container():
    print('Still Under Dev\n')
    exit()


def init():
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    msg_1 = '1: List Blobs In Container\n' \
            '2: Upload Blob To Container\n' \
            '3: Remove Blob From Container\n' \
            '4: Download Blob From Container\n' \
            '5: Create New Blob Container\n' \
            '6: Check If Container Exists\n' \
            '7: Remove Container\n' \
            '8: List All Containers\n' \
            '9: Restore Deleted Container\n' \

    print(msg_1)
    option = input('Enter Option: ')
    if option not in options:
        print('Incorrect Option Entered!')
        exit()

    function_library = {
        '1': list_blobs_in_container,
        '2': upload_blob_to_container,
        '3': remove_blob_from_container,
        '4': download_blob_from_container,
        '5': create_new_blob_container,
        '6': varify_container_existence,
        '7': delete_container,
        '8': list_all_containers,
        '9': restore_deleted_container
    }

    function = function_library[option]
    function()


init()
