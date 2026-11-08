def bubble_sort(book_list):
    n = len(book_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if book_list[j].sort_year > book_list[j + 1].sort_year:
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]
                swapped = True
        if not swapped:
            break
    return book_list
