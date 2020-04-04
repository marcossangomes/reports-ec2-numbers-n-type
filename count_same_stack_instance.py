import json
from collections import Counter
from get_instance_type import get_instance_type
from list_instances_by_tag_value import list_instances_by_tag_value

# Functin to generete json with same instances names, instance type and total of theses same instances
def count_same_stack_instance(instances_ids, instances_names):

    lista = []

    # Array with count of the same instances names
    instances_counter = Counter(instances_names)

    try:

        for value in instances_counter:
            print(value)
            print(instances_counter[value])
           # print("\n")
            
            # Creating the json value
            jsonObject = {
                "Stack" : value,
                "Number of instances" : int(instances_counter[value]),
                "Type of instances" : get_instance_type(list_instances_by_tag_value('Name', value))
            }

            lista.append(jsonObject)

            data_json = json.dumps(lista, indent=2)

    # Exception to treat if the instance name are blank.
    except Exception as err:
        print(err)


    # Write in json file the values of the jsonObject
    f = open('report-instances-numbers-and-type', "w")
    f.write(str(data_json))
    f.close()