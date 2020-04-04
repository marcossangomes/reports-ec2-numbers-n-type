import boto3

# Function to get instances name with instance id
def get_instance_name(instance_id):

    # When given an instance ID as str e.g. 'i-1234567', return the instance 'Name' from the name tag.
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(instance_id)
    instancename = ''
    
    for tags in ec2instance.tags:
        try:
            if tags["Key"] == 'Name':
                instancename = tags["Value"]

            return instancename

        # Exception to return 'No name' if the instance name is blank
        except Exception as ex:
            #return 'No name'
            return ex

