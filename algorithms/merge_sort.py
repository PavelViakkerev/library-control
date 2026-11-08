def merge_sort(book_list, key=lambda b: b.sort_year):
    if len(book_list) <= 1:
        return list(book_list)

    mid = len(book_list) // 2
    left = merge_sort(book_list[:mid], key)
    right = merge_sort(book_list[mid:], key)

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
