def list_files(bucket_name):
    """Lists all files in the specified bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    blobs = bucket.list_blobs()
    for blob in blobs:
        print(blob.name)

# Example Usage
list_files("bucket_labs-1")
