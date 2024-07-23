import re


def generator_numbers(text: str):
    list_numbers = re.findall(r'\s\d+\.\d+\s', text)

    for number in list_numbers:
        yield float(number.strip())


def sum_profit(numbers: list):
    return sum(numbers)
