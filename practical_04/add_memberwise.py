def add_memberwise(list_1, list_2):
    result_list = []
    if len(list_1) < len(list_2):
        for i in range(0, len(list_1)):
            result_list.append(float(list_1[i]) + float(list_2[i]))
        for i in range(len(list_1), len(list_2)):
            result_list.append(float(list_2[i]))
    else:
        for i in range(0, len(list_2)):
            result_list.append(float(list_1[i]) + float(list_2[i]))
        for i in range(len(list_2), len(list_1)):
            result_list.append(float(list_1[i]))
    return result_list


numbers_1 = [2, 1.5, 3, 4, 1]
numbers_2 = [1, 1, 1, 1]
print(add_memberwise(numbers_1, numbers_2))
