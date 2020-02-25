import logging

from model import Library


def get_score(libraries, books, n_days):
    logger = logging.getLogger(__name__)
    next_subscribe = 0
    score = 0
    books_subscribed = []
    active_libraries = []
    for day in range(n_days):  # from 0 to 6 if n_days = 7
        s = f"Starting day '{day}' with '{len(active_libraries)} active libraries and '{len(books_subscribed)}':{score}"
        logger.debug(s)
        if day == next_subscribe and libraries:
            active_lib: Library = libraries.pop(0)
            next_subscribe += active_lib.signup
            active_libraries.append(active_lib)
        for active_lib in active_libraries:
            books_lib = [book for book in active_lib.books if book not in books_subscribed]
            for n in range(active_lib.books_day):
                if books_lib:
                    subbed_book = books_lib.pop(0)  # pops first
                    books_subscribed.append(subbed_book)
                    active_lib.books_scanned.append(subbed_book)
                    score += books[subbed_book].score
                else:
                    break

    return active_libraries, books_subscribed, score


def get_score_numba(libraries, books, n_days):
    next_subscribe = 0
    score = 0
    books_subscribed = []
    active_libraries = []
    for day in range(n_days):  # from 0 to 6 if n_days = 7


