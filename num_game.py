

def gen_nums(num):
   check = [1, 2, 4, 8, 16, 32, 64, 128, 264]

   A = [1]
   B = [2] 
   C = [4] 
   D = [8] 
   E = [16] 
   F = [32] 
   G = [64] 
   H = [128] 
   I = [264] 

   cl = len(check) - 1

   for n in range(num):
      start = n

      if(start >= I[0]):
         I.append(n)
         start = start - I[0]

      if(start >= H[0]):
         H.append(n)
         start = start - H[0]

      if(start >= G[0]):
         G.append(n)
         start = start - G[0]

      if(start >= F[0]):
         F.append(n)
         start = start - F[0]

      if(start >= E[0]):
         E.append(n)
         start = start - E[0]

      if(start >= D[0]):
         D.append(n)
         start = start - D[0]

      if(start >= C[0]):
         C.append(n)
         start = start - C[0]

      if(start >= B[0]):
         B.append(n)
         start = start - B[0]

      if(start >= A[0]):
         A.append(n)
         start = start - A[0]

         

   print(A)
   print(B)
   print(C)
   print(D)
   print(E)
   print(F)
   print(G)
   # print(H) 
   # print(I)  


gen_nums(100)

