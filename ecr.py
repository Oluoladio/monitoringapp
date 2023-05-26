import boto3

ecr_client = boto3.client('ecr', region_name='us-east-1')

repository_name = "my-cloud-monitoring-repo" # give it a name of your choice
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)