import logging
import time
from pathlib import Path

from src import parser, helpers


def main():
    logger = logging.getLogger(__name__)
    example_path = r"input/a_example.txt"
    t1 = time.time()
    n_books, n_libraries, total_days, libraries, books = parser.parse_file(Path(example_path))
    logger.info(f"Total_time: {time.time() - t1}")

    print(helpers.get_score(libraries, books, total_days))


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    main()
