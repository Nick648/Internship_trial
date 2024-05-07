def main():
    n = int(input())
    books = list(map(int, input().split()))
    books_up, books_down, books_not_up = [], [], []
    max_book, min_book = max(books), min(books)
    max_book_f, min_book_f = min_book, max_book
    max_book_i, min_book_i = books.index(min_book), books.index(max_book)
    print(f'{min_book=}; {max_book=};\n'
          f'{min_book_f=}; {max_book_f=};\n'
          f'{min_book_i=}; {max_book_i=};\n')
    for i in range(n):
        if books[i] <= min_book_f:
            if abs(min_book - min_book_f) >= abs(min_book - books[i]) and abs(min_book_i - 0) >= abs(i - 0):
                print(f'Find min -> {i=}; {books[i]=}\n'
                      f'{abs(min_book - min_book_f)=} >= {abs(min_book - books[i])=};'
                      f'{abs(min_book_i - 0)=} >= {abs(i - 0)=};\n')
                min_book_f = books[i]
                min_book_i = i
        if books[i] >= max_book_f:
            if abs(max_book - max_book_f) >= abs(max_book - books[i]) and abs(max_book_i - 0) >= abs(i - 0):
                print(f'Find max -> {i=}; {books[i]=}\n'
                      f'{abs(max_book - max_book_f)=} >= {abs(max_book - books[i])=};'
                      f'{abs(max_book_i - (n-1))=} >= {abs(i - (n-1))=};\n')
                max_book_f = books[i]
                max_book_i = i
        print(f'\t{i=}\n'
              f'{min_book_f=}; {min_book_i=}; {max_book_f=}; {max_book_i=};\n')


if __name__ == '__main__':
    main()
