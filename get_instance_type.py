import boto3

# Get instance type with instance id
def get_instance_type(id):

    try:
        client = boto3.client('ec2')

        response = client.describe_instance_attribute(
            Attribute='instanceType',
            DryRun=False,
            InstanceId=id
        )

        return response['InstanceType']['Value']

    except Exception as err:
        print(err)
        return 'It was not possible to raise the type of the instance'


