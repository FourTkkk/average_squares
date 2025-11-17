"""Computation of weighted average of squares."""

import argparse

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]

def read_numbers_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    # 去掉换行符，然后转换成数字
    cleaned = [line.strip() for line in lines]
    return convert_numbers(cleaned)



# if __name__ == "__main__":
#     numbers_strings = ["1","2","4"]
#     weight_strings = ["1","1","1"]        
    
#     numbers = convert_numbers(numbers_strings)
#     weights = convert_numbers(weight_strings)
    
#     result = average_of_squares(numbers, weights)
    
#     print(result)

# -----------------------------
# argparse interface (NEW PART)
# -----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser( 
        description="Compute the (weighted) average of squares of given numbers."
    )

    parser.add_argument(
        "file_numbers",
        type=str,
        help="File containing one number per line."
    )

    # # Read only numbers from the command line (weights remain None)
    # parser.add_argument(
    #     "numbers",
    #     nargs="+",              # at least one number
    #     type=str,               # keep string so convert_numbers still works
    #     help="Numbers to compute the average of squares for."
    # )

    # 2️⃣ optional argument: --weights
    parser.add_argument(
        "--weights",
        # nargs="+",
        type=str,
        help="Optional file containing one weight per line."
    )

    args = parser.parse_args()

    # # Convert numbers from strings → floats
    # numbers = convert_numbers(args.numbers)
    # Read numbers from file
    numbers = read_numbers_from_file(args.file_numbers)

    # For now, weights stay None (exercise requirement)
    if args.weights is not None:
        # weights = convert_numbers(args.weights)
        weights = read_numbers_from_file(args.weights)
    else:
        weights = None

    # Compute result
    result = average_of_squares(numbers, weights)
    print(result)