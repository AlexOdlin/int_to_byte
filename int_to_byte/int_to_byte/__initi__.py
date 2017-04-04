from functools import reduce

def int_to_byte(int_number):
    byte_number = list()
    int_number = int(int_number)
    div = 0
    while (div != 1):
        div, mod = divmod(int_number, 2)
        int_number = div
        byte_number.append(mod)

    byte_number.append(1)
    byte_number.reverse()
    result = reduce(lambda a, b: str(a) + str(b), byte_number, '')

    print(result)
