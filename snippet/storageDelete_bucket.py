def delete_bucket(bucket_name):
    """Deletes a Cloud Storage bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    bucket.delete()

    print(f"Bucket {bucket_name} deleted.")

# Example Usage
delete_bucket("bucket_labs-1")
