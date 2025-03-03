def download_file(bucket_name, source_blob_name, destination_file_path):
    """Downloads a file from the bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_path)
    print(f"File {source_blob_name} downloaded to {destination_file_path}")

# Example Usage
download_file("bucket_labs-1", "uploadedfile.txt", "downloadedfile.txt")
