import boto3

# Function to get all instances types
def get_all_instances_type(instances_ids):

    instances_types = []

    for instance_id in instances_ids:
        client = boto3.client('ec2', region_name='us-east-1')
        response = client.describe_instance_attribute(
            Attribute='instanceType',
            DryRun=False,
            InstanceId=instance_id
        )

        instances_types.append(response['InstanceType']['Value'])
        print(instances_types)

    return instances_types