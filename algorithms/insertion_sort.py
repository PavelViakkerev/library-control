def insertion_sort(book_list):
    for i in range(1, len(book_list)):
        key = book_list[i]
        j = i - 1
        while j >= 0 and key.sort_year < book_list[j].sort_year:
            book_list[j + 1] = book_list[j]
            j -= 1
        book_list[j + 1] = key
    return book_list