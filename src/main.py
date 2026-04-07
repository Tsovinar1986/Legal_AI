from src.core.logger import logging
from src.core.exception import CustomException
import sys


def divide_numbers():
    try:
        result = 1 / 0
        print(result)
    except Exception as e:
        logging.info("Exception occurred during divide_numbers")
        raise CustomException(e, sys)


if __name__ == "__main__":
    divide_numbers()