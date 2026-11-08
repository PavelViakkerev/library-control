def binary_search(sorted_books, isbn):
    low, high = 0, len(sorted_books) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_isbn = sorted_books[mid].isbn
        if mid_isbn == isbn:
            return sorted_books[mid]
        if mid_isbn < isbn:
            low = mid + 1
        else:
            high = mid - 1
    return None
