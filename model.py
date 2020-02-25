from collections import namedtuple

Library = namedtuple("Library", ["id", "signup", "books", "books_day", "books_scanned"])
Book = namedtuple("Book", ["id", "score", "is_scanned"])
