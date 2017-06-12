def revertNum(list):
    max_num = list[0]
    max_index = 0
    for i in len(list):
        if max_num < list[i]:
            max_index = i
    list[0],list[max_index] = list[max_index],list[0]
    min_num = list[0]
    min_index = 0
    for i in len(list):
        if min_num < list[i]:
            min_index = i
    list[0],list[min_index] = list[min_index],list[0]

revertNum([1,2,3,4,5,6])
