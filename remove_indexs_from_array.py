# Remove same indices from a array and return a new array
def remove_indexs_from_array(instances_ids, instances_names, index_remove):

    index_remove.sort(reverse=True)

    for index in index_remove:
        del instances_ids[index]
        del instances_names[index]

    return instances_ids, instances_names, index_remove



