def calculate(salary: float):
    first_level_rate = 8.9 / 100.0
    first_level_limit = 64750.0
    second_level_rate = 13.2 / 100.0
    second_level_limit = 280000.0

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

if __name__ == '__main__':
    print("Duke retirement contriubution: $"+ str(calculate(1000000.0)))
