import boto3

# Function to generate a list with instances ids
def get_all_instances_id():
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.describe_instances()

    i = 0

    # Numbers of instances in the enviroment
    instances_len = (len(response['Reservations']))

    instance_ids = []

    # Create list with instances ids
    while i < instances_len:
        instance_ids.append(response['Reservations'][i]['Instances'][0]['InstanceId'])
        i += 1

    return instance_ids
