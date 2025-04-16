

let_values = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


# print(len(let_values))
# print(let_values.keys())


def getRom_num(dec_num):
   rom_num_value = 0

   for index, item in enumerate(dec_num):
      # print(index, item)
      next_index = 0
      if(index < len(dec_num)-1):
         next_index = index + 1
         # print("next_item", dec_num[next_index])
         next_item = dec_num[next_index]
      print(let_values[item] , let_values[next_item] )
      if(let_values[item] < let_values[next_item] ):
         rom_num_value -= let_values[item]
      else:
         rom_num_value += let_values[item] 


   return rom_num_value

print(getRom_num("XIV"))



# AI Solution 
def roman_to_int(s):
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Test case
print(roman_to_int("XIV"))  # Output: 14
print(roman_to_int("MCMXCIV"))  # Output: 1994
