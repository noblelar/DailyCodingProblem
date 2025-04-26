

def sevenish_number(n):
    result = 0
    power = 0
    while n > 0:
        if n & 1:
            result += 7 ** power
            print(result, power, n)
        power += 1
        n >>= 1
    return result

the_list = sevenish_number(5)
print(the_list)


