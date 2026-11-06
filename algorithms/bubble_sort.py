def bubble_sort(book_list):
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j].year > book_list[j+1].year:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
    return book_list
