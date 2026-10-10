'''
Simple math calculator without using eval()

This will handle basic math and a single level deep parentheses as that was the scope of the task.
Nested parentheses aren't supported.
'''

'''
Remove spaces from the string, then make sure it contains only valid arithmetic characters
'''
def sanitize(my_string):
    # strip all spaces, tabs, and newlines from the string
    my_string = my_string.replace(" ", "").replace("\t", "").strip()
    # allow only arithmetic characters (digits and decimal point, operators, parentheses)
    allowed_chars = "0123456789.+-*/()"
    for char in my_string:
        if char not in allowed_chars:
            raise ValueError("Error: Invalid character")
    return my_string

'''
Calculate the result of the sanitized arithmetic string without using eval()
Example: "4+ ((60 * 8) +7)- 9"
'''
def calculate(my_string: str) -> int | float:
    my_string = sanitize(my_string)
    # see if we have more than one level of parentheses
    # string length
    print(f"******* String: {my_string}")
    length = len(my_string)
    current_result = 0
    left = ''
    right = ''
    current_operator = ''
    in_parentheses = False
    paren_string = ''

    for i in range(length):
        print(f"Processing character: {my_string[i]}")
        if my_string[i] == '(':
            # see if we're already inside parentheses (nested)
            if in_parentheses:
                raise ValueError("Nested parentheses are not supported")
            in_parentheses = True
            continue
        if my_string[i] == ')':
            in_parentheses = False
            right = calculate(paren_string)
            paren_string = ''
            continue
        if in_parentheses:
            paren_string += my_string[i]
            continue
        if my_string[i] in "0123456789":
            if current_operator == '':
                left = f"{left}{my_string[i]}"
            else:
                right = f"{right}{my_string[i]}"
            continue
        if my_string[i] in "+-*/":
            if current_operator == '':
                current_operator = my_string[i]
            else:
                if left and right:
                    current_result = domath(left, current_operator, right)
                    left = str(current_result)
                    right = ''
                    current_operator = my_string[i]
        print(f"'{left}' '{current_operator}' '{right}' = '{current_result}'")

    # the final right.
    if left and right:
        current_result = domath(left, current_operator, right)
        print(f"'{left}' '{current_operator}' '{right}' = '{current_result}'")
    return int(current_result)

def domath(left: str, operator: str, right: str) -> int | float:
    if not left or not right or not operator:
        raise ValueError("Invalid expression")
    print(f"Calculating: {left} {operator} {right}")
    if operator == '+':
        return int(left) + int(right)
    elif operator == '-':
        return int(left) - int(right)
    elif operator == '*':
        return int(left) * int(right)
    elif operator == '/':
        return int(left) / int(right)
    else:
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    # array of math problems
    problems = [
        "47 + 4",
        "6 +3-2",
        "10 / 2",
        "5 +( 5 - 2)",
        "5 + ((5 - 2))"
    ]
    for problem in problems:
        try:
            sanitized = sanitize(problem)
            result = calculate(problem)
            eval_result = eval(sanitized)
        except (ValueError, ZeroDivisionError) as e:
            result = str(e)
        finally:
            print(f"------ {problem}: {sanitized} = {result} (eval: {eval_result})")
