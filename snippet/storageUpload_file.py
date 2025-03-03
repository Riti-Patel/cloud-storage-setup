def upload_file(bucket_name, source_file_path, destination_blob_name):
    """Uploads a file to the specified bucket."""
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path)
    print(f"File {source_file_path} uploaded to {bucket_name}/{destination_blob_name}")

# Example Usage
upload_file("bucket_labs-1", "localfile.txt", "uploadedfile.txt")
   
