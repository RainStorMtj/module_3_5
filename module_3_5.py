def get_multiplied_digit(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digit(int(str_number[1:]))
    if first == 0:
        return 1
    else:
       return first

result = get_multiplied_digit(40203)
result2 = get_multiplied_digit(402030)
print(result)
print(result2)
