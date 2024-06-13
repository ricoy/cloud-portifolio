from google.cloud import storage

import sys

key = sys.argv[1]

storage_client = storage.Client.from_service_account_json(key)

bucket_name = "tcb-gcp-ricoy-02"

bucket = storage_client.create_bucket(bucket_name)

buckets = list(storage_client.list_buckets())

print(*buckets, sep="\n")

