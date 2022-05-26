import os

from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

from azure.storage.fileshare import (
    ShareServiceClient,
    ShareClient,
    ShareDirectoryClient,
    ShareFileClient
)
import json
from os import walk

# Create a ShareServiceClient from a connection string
service_client = ShareServiceClient.from_connection_string(connection_string)
print(f'Primary Endpoint: {service_client.primary_endpoint}')
print(f'Primary Hostname:{service_client.primary_hostname}')
print(f'API Version :{service_client.api_version}')
print(f'Account Name:{service_client.account_name}')
print(f'URL :{service_client.url}')
print('=' * 50)


