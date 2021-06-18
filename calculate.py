import argparse


def calculate(salary: float):
    first_level_rate = 8.9 / 100.0
    first_level_limit = 69400.0
    second_level_rate = 13.2 / 100.0
    second_level_limit = 290000.0

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
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [SALARY]...",
        description="Print Duke retirement contriubution for a given salary."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument('salary', help="Find Duke Reitrement contriubution for this salary", type=float, nargs='*')
    return parser


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    if not args.salary:
        sal = 1000000
        print(f'For ${sal} salary, Duke retirement contriubution = ${calculate(sal):.2f}')
    for sal in args.salary:
        try:
            print(f'For ${sal} salary, Duke retirement contriubution = ${calculate(sal):.2f}')
        except Exception as err:
            print(f"{sys.argv[0]}: {sal}: {err.strerror}", file=sys.stderr)


if __name__ == '__main__':
    main()
