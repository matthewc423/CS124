import math
import random
import sys
import fileinput
import numpy as np

strass_arr = [1]
conven_arr = [1]

def strass(n):
    if n == 1:
        return 1
    else:
        return 18 * ((n // 2) ** 2) + 7 * strass(n // 2)

def conv(n):
    return ((2 * n) - 1) * (n ** 2)

for i in range(1, 15):
    i = 2 ** i
    x = strass(i)
    if strass(i) not in strass_arr:
        strass_arr.append(strass(i))

    y = conv(i)
    if y not in conven_arr:
        conven_arr.append(y)

for i in range(len(strass_arr)):
    strass_arr[i] = math.log(strass_arr[i], 2)
    conven_arr[i] = math.log(conven_arr[i], 2)

#print(strass_arr)
#print(conven_arr)

#answer = 2^10 -> between 2^9 and 2^10 but it's better to round up


#[0.0, 4.643856189774724, 7.948367231584678, 10.97799536861296, 13.898506917637288, 16.76674887797676, 19.607776390707034, 22.434025713219864, 
#25.25206736373329, 28.065493632808725, 30.87630645884265, 33.685633611232575, 36.494114312725245, 39.30211214311711, 42.109834312774304]

#[0.0, 3.5849625007211565, 6.807354922057604, 9.90689059560852, 12.954196310386875, 15.977279923499918, 18.988684686772164, 21.99435343685886, 
#24.997179480937625, 27.99859042974533, 30.999295387023412, 33.999647736528374, 36.99982387901573, 39.999911942195425, 42.99995597176956]




# plt.plot(strass_arr, 'r')
# plt.plot(conven_arr, 'b')
# plt.ylabel("Number of Operations")
# plt.xlabel("Value of n")
# plt.show()

def evenshelper(evens):
  newevens = []

  for even in evens:
    if even * 2 < 258:
      newevens.append(even * 2)
      newevens.append(even * 2 - 1)
  
  if newevens == []:
    return newevens
  return evens + evenshelper(newevens) 

def oddshelper(odds):
  newodds = []
  for odd in odds:
    if odd * 2 < 258:
      newodds.append(odd * 2)
      newodds.append(odd * 2 - 1)
  
  if newodds == []:
    return newodds
  return odds + evenshelper(newodds) 

def even_odd(crossover):
  even_sizes = []
  odd_sizes = []
  for i in range(crossover, crossover * 2 + 1, 1):
    if i % 2 == 0:
      even_sizes.append(i)
    else:
      odd_sizes.append(i)
  return even_sizes, odd_sizes

  

def strass2(mat_len, crossover):
  if crossover > mat_len:
    return conv(mat_len)
  if mat_len % 2 == 0:
    return 18 * ((mat_len // 2) ** 2) + 7 * strass2(mat_len // 2, crossover)
  else:
    return 18 * (((mat_len + 1) // 2) ** 2) + 7 * strass2((mat_len + 1) // 2, crossover)


def make_matrix(length):
  arr = []
  for i in range(length):
    arr.append([])
  
  x = len(arr)
  for i in range(x):
    for j in range(length):
      arr[i].append(random.randint(0, 1))
      
  return arr


def conventional(a, b):
  n = len(a)
  
  matrix = []
  
  for i in range(n):
    matrix.append([0] * n)
  
  for i in range(n):
    for j in range(n):
      for k in range(n):
        matrix[i][j] += a[i][k] * b[k][j]
  
  return matrix



# def pad_matrix(matrix, crossover):
  
#   #crossover is global var
#   n = len(matrix)
#   if crossover > n:
#     return matrix
  
#   initial_num = math.ceil(n / crossover)
  
#   counter = 1
#   while counter < initial_num:
#     counter *= 2
  
#   #multiple of counter
#   padding = n + counter // 2
#   padding = padding - (padding % counter)
#   if padding < n:
#     padding += counter
#   padding = padding - n
  
#   for i in range(len(matrix)):
#     for j in range(padding):
#       matrix[i].append(0)
      
#   add_row = [0] * (len(matrix) + padding)
#   for i in range(padding):
#     matrix.append(add_row)

#   return matrix

def pad_matrix(m):
  n = len(m)
  if n % 2 == 0:
    return m
  
  for i in range(n):
    m[i].append(0)
      
  add_row = [0] * (n + 1)
  m.append(add_row)
  return m

def add(x, y):
  # output = []
  # print(len(x), len(y))
  # for i in range(len(x)):
  #   output.append([0] * len(x))
  #   for j in range(len(x)):
  #     output[i][j] = x[i][j] + y[i][j]   
  # return output
  return (np.add(np.array(x), np.array(y))).tolist()
                
def sub(x, y):
  # output = []
  # for i in range(len(x)):
  #   output.append([0] * len(x))
  #   for j in range(len(x)):
  #     output[i][j] = x[i][j] - y[i][j]   
  # return output
  return (np.subtract(np.array(x), np.array(y))).tolist()

def unpad(x, n):
  m = []
  for i in range(n):
    m.append([0] * n)
    for j in range(n):
      m[i][j] = x[i][j]
  return m
        
def strassens(x, y, crossover):
  original = len(x)
  if crossover > original:
    return conventional(x, y)
  m1 = x
  m1 = pad_matrix(m1)
  m2 = y
  m2 = pad_matrix(m2)
  n = len(m1)
  
  size = n//2
  A = []
  B = []
  C = []
  D = []
  E = []
  F = []
  G = []
  H = []
  
  for i in range(size):
    A.append(m1[i][:size])
    E.append(m2[i][:size])
    B.append(m1[i][size:])
    F.append(m2[i][size:])
  for i in range(size, n, 1):
    C.append(m1[i][:size])
    G.append(m2[i][:size])
    D.append(m1[i][size:])
    H.append(m2[i][size:])
  A = pad_matrix(A)
  B = pad_matrix(B)
  C = pad_matrix(C)
  D = pad_matrix(D)
  E = pad_matrix(E)
  F = pad_matrix(F)
  G = pad_matrix(G)
  H = pad_matrix(H)

  P1 = unpad(strassens(A, sub(F, H), crossover), size)
  P2 = unpad(strassens(add(A, B), H, crossover), size)
  P3 = unpad(strassens(add(C, D), E, crossover), size)
  P4 = unpad(strassens(D, sub(G, E), crossover), size)
  P5 = unpad(strassens(add(A, D), add(E, H), crossover), size)
  P6 = unpad(strassens(sub(B, D), add(G, H), crossover), size)
  P7 = unpad(strassens(sub(C, A), add(E, F), crossover), size)

  a = add(P6, add(P5, sub(P4, P2)))
  b = add(P1, P2)
  c = add(P3, P4)
  d = add(P7, add(P5, sub(P1, P3)))
    
  result = []
  for i in range(n):
    if i < size:
      result.append(a[i] + b[i])
    else:
      result.append(c[i - size] + d[i - size])
            
  return result
    

def print_matrix(m):
  for i in range(len(m)):
    print(m[i])
  print()

if int(sys.argv[1]) == 0:

  file = sys.argv[3]
  n = int(float(sys.argv[2]))

  x = []
  y = []

  for i in range(n):
    x.append([0] * n)
    y.append([0] * n)

  lcounter = 0
  col = 0
  row = 0
  for line in fileinput.input(files = file):
    if lcounter < n ** 2:
      x[row][col] = int(line)
      col += 1
      if col >= n:
        row += 1
        col = 0      
      lcounter += 1
    else:
      y[row - n][col] = int(line)
      col += 1
      if col >= n:
        row += 1
        col = 0      

  matrix = strassens(x, y, 10)
  #matrix = unpad(matrix, n)
  #matrix = conventional(x, y)
  for i in range(n):
    print(matrix[i][i])

elif int(sys.argv[1]) == 1:
  occurrences = {}

  for n in range(2, 258, 1):
    l = []
    for cross in range(2, 70, 1):
      x = make_matrix(n)
      y = make_matrix(n)
      l.append(strass2(len(x), cross))
    m = l.index(min(l)) + 2
    if m not in occurrences:
      occurrences[m] = 0
    occurrences[m] += 1
  occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1]))
  for key in occurrences:
    print(key, ": ", occurrences[key])

else:
  n = 22
  x = make_matrix(n)
  y = make_matrix(n)
  matrix = strassens(x, y, 10)
  print_matrix(matrix)

