
'''
Remove spaces from the string, then make sure it contains only valid arithmetic characters
'''
def eval_sanitize(my_string):
    # strip all spaces, tabs, and newlines from the string
    my_string = my_string.replace(" ", "").replace("\t", "").strip()
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
        "4+ ((60 * 8) +7)- 9",
    ]
    for problem in problems:
        try:
            sanitized_problem = eval_sanitize(problem)
            result = int(eval(sanitized_problem))
        except ValueError as e:
            result = str(e)
        print(f"{problem}: {sanitized_problem} = {result}")