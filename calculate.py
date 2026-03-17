import argparse
import sys


def calculate(salary: float) -> float:
    """
    Calculate the retirement contribution based on the given salary.
    The calculation is performed using a tiered rate system:
    - For salaries up to `first_level_limit`, a rate of `first_level_rate` is applied.
    - For salaries between `first_level_limit` and `second_level_limit`, 
      `first_level_rate` is applied to the first tier, and `second_level_rate` is applied to the remainder.
    - For salaries above `second_level_limit`, the contribution is capped at the maximum 
      calculated using both tiers.
    Args:
        salary (float): The annual salary for which the retirement contribution is calculated. 
                        Must be a non-negative value.
    Returns:
        float: The total retirement contribution based on the salary.
    Raises:
        ValueError: If the salary is negative.
    """

    first_level_rate = 8.9 / 100.0
    first_level_limit = 88650.0
    second_level_rate = 13.2 / 100.0
    second_level_limit = 360000.0

    if salary >= second_level_limit:
        amount = first_level_rate * (first_level_limit) + second_level_rate * (second_level_limit - first_level_limit)
        return amount
    elif salary > first_level_limit:
        amount = first_level_rate * (first_level_limit) + second_level_rate * (salary - first_level_limit)
        return amount
    elif salary >= 0:
        amount = first_level_rate * salary
        return amount
    else:
        raise ValueError("Enter a positive salary. You aren't paying to work at Duke, are you?!")


def init_argparse() -> argparse.ArgumentParser:
    """
    Initializes and returns an argument parser for the retirement contribution calculator.
    This function sets up an argument parser with the following options:
    - A version flag (`-v` or `--version`) to display the program version.
    - A positional argument `salary` to input one or more salary values for which the Duke retirement contribution will be calculated.
    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """

    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [SALARY]...",
        description="Print Duke retirement contribution for a given salary."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument(
        'salary', help="Find Duke Reitrement contribution for this salary",
        type=float, nargs='*'
    )
    return parser


def main() -> None:
    """
    The main function initializes the argument parser, processes command-line arguments,
    and calculates the Duke retirement contribution based on the provided salary or a default value.
    If no salary is provided via command-line arguments, it uses a default salary of $330,000.00
    and prints the calculated retirement contribution. If multiple salaries are provided, it
    iterates through them, calculates the contribution for each, and prints the result. Errors
    during calculation are caught and reported to standard error.
    Returns:
        None
    """

    parser = init_argparse()
    args = parser.parse_args()
    if not args.salary:
        salary = 330000.0
        print(f'For ${salary:.2f} salary, Duke retirement contribution = ${calculate(salary):.2f}')
    else:
        for salary in args.salary:
            try:
                print(f'For ${salary:.2f} salary, Duke retirement contribution = ${calculate(salary):.2f}')
            except Exception as err:
                print(f"{sys.argv[0]}: {salary}: {err.strerror}", file=sys.stderr)


if __name__ == '__main__':
    main()
