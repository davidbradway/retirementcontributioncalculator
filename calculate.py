def calculate(salary: float):
    first_level_percentage = 0.089
    second_level_percentage = 0.132
    transition = 64750
    upper_limit = 280000

    if salary >= upper_limit:
        amount = first_level_percentage * (transition) + second_level_percentage * (upper_limit - transition) 
        return amount
    elif salary > transition:
        amount = first_level_percentage * (transition) + second_level_percentage * (salary - transition) 
        return amount
    else:
        amount = first_level_percentage * salary 
        return amount

if __name__ == '__main__':
    print("Duke retirement contriubution: $"+ str(calculate(1000000.0)))
