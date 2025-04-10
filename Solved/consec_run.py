

def get_binary(num):
   binary = ""
   abin = str(bin(num)[2:])
   while (num != 0):
      remainder = int(num % 2)
      binary = str(remainder) + binary
      num = (num - remainder) / 2

   return binary


def consec_run(num):
   consec_count = 0 
   count = 0 
   print(num) 

   num_in_binary = get_binary(num)
   print(len(num_in_binary))
   for x in num_in_binary :
      if x == "1":
         count = count + 1
         consec_count = count
      else: 
         count = 0


   return consec_count



thevalue = consec_run(156)
print(thevalue)