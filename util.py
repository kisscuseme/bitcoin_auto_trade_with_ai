def get_index(obj_list, field, value):
    for i in range(len(obj_list)):
        if obj_list[i][field] == value:
            return i
    return None

def get_num_to_str(num):
    return str(format(round(num,3),','))

