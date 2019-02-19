def find(ordered_list, element_to_find):
    start_index = 0
    end_index = len(ordered_list) - 1

    print(ordered_list, element_to_find)

    while True:
        middle_index = (end_index + start_index) // 2


        if middle_index == start_index or middle_index == end_index:
            if ordered_list[middle_index] == element_to_find or ordered_list[end_index] == element_to_find:
                return True
            else:
                return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element > element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index

if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]

    print(find(l, -15))
    print(find(l, 1))
    print(find(l, 4))
    print(find(l, 100))
    print(find(l, 10))
