

def sevenish (n):
   sevenish_list = []

   count = 0

   while count < n: 
      next = 7**n 
      sevenish_list.append(next) 
      if n%2 == 1: 
         next = sevenish_list[count] + sevenish_list[count-1] 

   print(sevenish_list)
   return sevenish_list


the_list = sevenish(5)
print(the_list)


