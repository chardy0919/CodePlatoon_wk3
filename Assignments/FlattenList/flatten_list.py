def flatten_list(lst):
    new_list = []
    for item in lst:
        if type(item) == list:
            for item2 in item:
                new_list.append(item2)
        else:
            new_list.append(item)
    return new_list

def recurse(input, index = 0, new_list = []):
    if index == len(input):
        return new_list
    else:
        if type(input[index]) == list:
            for item in input[index]:
                new_list.append(item)
        else:
            new_list.append(input[index])
    return recurse(input, index+1)