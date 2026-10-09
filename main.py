
'''
Remove spaces from the string, then make sure it contains only valid arithmetic characters
'''
def sanitize(my_string):
    # strip all spaces from the string
    my_string = my_string.replace(" ", "")
    # allow only arithmetic characters (digits and decimal point, operators, parentheses)
    allowed_chars = "0123456789.+-*/()"
    for char in my_string:
        if char not in allowed_chars:
            raise ValueError("Error: Invalid character")
    return my_string

if __name__ == "__main__":
    # array of math problems
    problems = [
        "4 + 4",
        "6 +3-2",
        "5 * 6 + ((202/2) - 1)",
    ]
    for problem in problems:
        try:
            sanitized_problem = sanitize(problem)
            result = int(eval(sanitized_problem))
        except ValueError as e:
            result = str(e)
        print(f"{problem} = {result}")