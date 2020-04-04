# Function to remove duplicate values in list
def duplicates(lst, item):
    same_values = [i for i, x in enumerate(lst) if x == item]
    return same_values

