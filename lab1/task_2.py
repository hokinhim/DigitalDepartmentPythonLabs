# TODO Найдите количество книг, которое можно разместить на дискете
diskette_capacity = 1.44
book_pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
count_books = int(diskette_capacity * 1024 * 1024 / (book_pages * lines_per_page * chars_per_line * bytes_per_char))
print("Количество книг, помещающихся на дискету:", count_books)
