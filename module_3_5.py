def get_multiplied_digit(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
       return first * get_multiplied_digit(int(str_number[1:]))

result = get_multiplied_digit(40203)
print(result)
