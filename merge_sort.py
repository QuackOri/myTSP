#merge_sort
target = [5, 3, 2, 9, 6, 1, 10, 4, 8, 7]

# 입력된 두 리스트를 정렬하여 합치는 함수
def merge(list1, list2):
    merge_list = []

    one, two = list1.pop(0), list2.pop(0)

    while one != 0 or two != 0:
        
        if (one >= two and two != 0) or one == 0:
            merge_list.append(two)
            if list2:
                two = list2.pop(0)
            else:
                two = 0
        elif (one < two and one != 0) or two == 0:
            merge_list.append(one)
            if list1:
                one = list1.pop(0)
            else:
                one = 0

    if one:
        merge_list.append(one)
    if two:
        merge_list.append(two)

    return merge_list

# 리스트를 반으로 분할해서 merge 함수로 보내는 함수
def list_split(array):
    if len(array) == 1:
        return array
    half = int(len(array) / 2)
    left = list_split(array[:half])
    right = list_split(array[half:])
    return merge(left, right)


print(list_split(target))
