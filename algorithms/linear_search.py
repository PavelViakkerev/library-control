
def linear_search(linked_list, isbn):
    current = linked_list.head
    while current:
        if current.data.isbn == isbn:
            return current.data
        current = current.next
    return None