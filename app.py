from get_all_instances_id import get_all_instances_id
from get_all_instances_names import get_all_instances_names
from count_same_stack_instance import count_same_stack_instance
from duplicates import duplicates
from remove_indexs_from_array import remove_indexs_from_array
from send_msg_slack import send_msg_slack


# Retrieve all values from instances ids and intances names
instances_ids = get_all_instances_id()
instances_names = get_all_instances_names(instances_ids)
instances_names_complete = get_all_instances_names(instances_ids)

array_duplicados = []

#Create an array with the index
for instance_name in instances_names:

    index_same_values = duplicates(instances_names, instance_name)

    if len(index_same_values) > 1:
        #Removes the first element, where we will use base to get the instance id when calling the get_instances_type() function
        del index_same_values[0]
        for i in index_same_values:
            array_duplicados.append(i)


# Remove the index of the firsts same instances names
index_remove = array_duplicados

# Transform in dict in list
index_remove = list(dict.fromkeys(index_remove))

# remove indexs of the sames instances names
new_arrays = remove_indexs_from_array(instances_ids, instances_names, index_remove)


# Assigning the values of the new treated arrays to the variables
instances_ids = new_arrays[0]
instances_names_uniques = new_arrays[1]
instances_types = new_arrays[2]

# Functin to generete json with same instances names, instance type and total of theses same instances
print(count_same_stack_instance(instances_ids, instances_names))

# Funcition to send json report file on Slack
send_msg_slack()











