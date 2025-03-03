from google.cloud import storage

def set_bucket_permissions(bucket_name, member, role):
    """Grants a specific role to a user or service account on a GCS bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Get the current IAM policy
    policy = bucket.get_iam_policy(requested_policy_version=3)

    # Add a new IAM binding
    policy.bindings.append({"role": role, "members": {member}})

    # Set the updated policy
    bucket.set_iam_policy(policy)

    print(f"Role {role} granted to {member} on bucket {bucket_name}")

# Example Usage
set_bucket_permissions("bucket_labs-1", "user:example@gmail.com", "roles/storage.objectViewer")
