import os
from collections import defaultdict


BOOK = "frankeinstein.txt"


def main():
    content = read_book()
    get_report(content, sort_by_key=False)


def read_book():
    """Read file from ./book/
    Filename given as a global: BOOK

    Returns:
        str: contents of the file.
    """
    with open(os.path.join("", "books", BOOK)) as f:
        content = f.read()
        return content


def count_words(source: str):
    """Returns the word count of a str

    Args:
        source (str)

    Returns:
        int: total word count
    """
    words = source.split()
    return len(words)


def count_letters(source: str):
    """Creates a dict of the alnum characters of the given str.

    Args:
        source (str)
    """

    def default():
        return 0

    count = defaultdict(default)

    for char in source.upper():
        if char.isalnum():
            count[char] += 1

    return count


def get_sorted_count(count: dict, sort_by_key=True, reverse=False):
    """Sort the given dict according to the given parameters.
    Returns the compiled statistics of the characters in the dict as a str.

    Args:
        count (dict): dict to be sorted
        sort_by_key (bool, optional): Defaults to True.
        reverse (bool, optional): Defaults to False.

    Returns:
        str: compiled statistics of the chars.
    """
    data = ""
    if sort_by_key:
        order = list(count.keys())
        order.sort(reverse=reverse)
        for key in order:
            data += f"The character {key} was found {count[key]} times.\n"
    else:
        keyes = list(count.keys())
        values = list(count.values())
        sorted_values = values[:]
        sorted_values.sort(reverse=not reverse)
        for value in sorted_values:
            i = values.index(value)
            data += f"The character {keyes.pop(i)} was found {values.pop(i)} times.\n"

    return data


def get_report(source, sort_by_key=True, reverse=False):
    """Print the full report of the given str. Word count, and character statistics.

    Args:
        source (str): The string of which the report is needed.
        sort_by_key (bool, optional): Defaults to True.
        reverse (bool, optional): Defaults to False.
    """
    start_text = f"\n### Report on book: {''.join(BOOK.split('.')[:-1])} ###\n"
    words = f"{count_words(source)} words were found in the book.\n\n"
    characters = get_sorted_count(count_letters(source), sort_by_key=sort_by_key, reverse=reverse)
    end_text = "\n### Report end ###\n"

    report = start_text + words + characters + end_text
    print(report)


if __name__ == "__main__":
    main()
