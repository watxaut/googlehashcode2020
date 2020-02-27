from src.model import Book, Library
import logging


def parse_file(file_path):
    logger = logging.getLogger(__name__)
    with open(file_path, "r") as f:
        n_books, n_libraries, total_days = [int(x) for x in f.readline().split(" ")]
        logger.info(f"N books: {n_books}, N Libraries: {n_libraries}, total days: {total_days}")
        # book 0 in list position 0
        books = [Book(book_id, int(score), False) for book_id, score in enumerate(f.readline().split(" "))]
        libraries = []
        counter = 0
        for line in f.readlines():
            if line == "\n":
                break
            if counter % 2 == 0:  # new library
                n_books_lib, signup, books_day = [int(x) for x in line.split(" ")]
            else:  # books of library
                books_lib = [int(x) for x in line.split(" ")]
                lib = Library(id=counter // 2, signup=signup, books=books_lib, books_day=books_day, books_scanned=[-1])
                libraries.append(lib)
            counter += 1

    return n_books, n_libraries, total_days, libraries, books
