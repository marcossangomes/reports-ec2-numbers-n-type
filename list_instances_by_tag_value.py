import boto3

def list_instances_by_tag_value(tagkey, tagvalue):
    # When passed a tag key, tag value this will return a list of InstanceIds that were found.
    try:

        ec2client = boto3.client('ec2')

        response = ec2client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:'+tagkey,
                    'Values': [tagvalue]
                }
            ]
        )
        instancelist = []
        for reservation in (response["Reservations"]):
            for instance in reservation["Instances"]:
                instancelist.append(instance["InstanceId"])
        return instancelist[0]

    except Exception as err:
        print(err)
        return 'it was not possible to map the type of the instance'