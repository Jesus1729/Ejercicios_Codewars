# Remove the parentheses

def remove_parentheses(s):
    parentheses_count = 0
    output = ""
    for i in s:
        if i=="(":
            parentheses_count += 1
        elif i==")":
            parentheses_count -= 1
        else:
            if parentheses_count == 0:
                output += i
    return output

print(remove_parentheses("example(unwanted thing)example"))