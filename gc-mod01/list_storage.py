from google.cloud import storage

import sys

key = sys.argv[1]
storage_client = storage.Client.from_service_account_json(key)

buckets = list(storage_client.list_buckets())

print(buckets)
