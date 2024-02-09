# Write Number in Expanded Form

def expanded_form(num):
    num = str(num)
    result = []
    for i in range(len(num)):
        if num[i] != '0':
            result.append(num[i] + '0'*(len(num)-i-1))
    return ' + '.join(result)

print(expanded_form(25678))