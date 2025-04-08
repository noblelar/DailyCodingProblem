

def get_binary(num):
   binary = ""
   while (num != 0):
      remainder = num % 2
      binary = str(remainder) + binary
      num = (num - remainder) / 2

   return binary

def consec_run(num):
   consec_count = 0
   print(num)

   num_in_binary = get_binary(num)
   print(num_in_binary)

   return consec_run



consec_run(156)