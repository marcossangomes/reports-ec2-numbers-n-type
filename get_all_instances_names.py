from get_all_instances_id import get_all_instances_id
from get_instance_name import get_instance_name

# Function to generate a list with all instances names
def get_all_instances_names(instances_ids):

    instances_names = []

    for instance in instances_ids:
        instances_names.append(get_instance_name(instance))

    return instances_names

