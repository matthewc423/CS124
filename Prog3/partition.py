
import random
import heapq
import math
import sys
import fileinput
import numpy as np

# def generate_solution(n):
#     sol = []
#     for i in range(n):
#         if random.randint(0, 1) == 0:
#             sol.append(-1)
#         else:
#             sol.append(1)
#     return sol

def generate_solution(n):
  # randnums = np.random.randint(0,1,n)
  # for i in range(len(randnums)):
  #   if randnums[i] == 0:
  #     randnums[i] = -1
  # return randnums
  return [(1 if random.random() < .5 else -1) for i in range(n)]


def t_iter(iteration):
  return 10 ** 10 * (.8) ** math.floor(iteration/300)

def random_move(s):
  s1 = []
  for a in s:
    s1.append(a)
  i = random.randint(0, len(s) - 1)
  j = random.randint(0, len(s) - 1)
  while j == i:
    j = random.randint(0, len(s) - 1)
  s1[i] *= -1
  if random.randint(0, 1) == 0:
    s1[j] *= -1
  return s1
  
def residue(sol, a):
   sum = 0
   for i in range(len(sol)):
      sum += (sol[i] * a[i]) 
   return abs(sum)
       

#repeated random
def repeated_random(a, n):
    sign_lst = generate_solution(len(a))
    for i in range(n):
        x = generate_solution(len(a))
        if residue(x, a) < residue(sign_lst, a):
            sign_lst = x  
    return sign_lst, residue(sign_lst, a)

def hill_climbing(a, n):
    s = generate_solution(len(a))
    for i in range(n):
        s1 = random_move(s)
        if residue(s1, a) < residue(s, a):
            s = s1
    return s, residue(s, a)
    

def simulated_annealing(a, n):
    s = generate_solution(len(a))
    sd_prime = []
    for i in s:
       sd_prime.append(i)
    for i in range(n):
        s_prime = random_move(s)
        if residue(s_prime, a) < residue(s, a):
            s = s_prime
        else:
            init_prob = math.exp(-(residue(s_prime, a) - residue(s, a)) / t_iter(n))
            if random.random() < init_prob: 
               s = s_prime
        if residue(s, a) < residue(sd_prime, a):
            sd_prime = s
    return sd_prime, residue(sd_prime, a)


def kk(a):
    neg_a = []
    for i in a:
        neg_a.append(i * -1)
    heapq.heapify(neg_a)
    while len(neg_a) > 1:
        n1 = heapq.heappop(neg_a)
        n2 = heapq.heappop(neg_a)
        heapq.heappush(neg_a, n1 - n2)
    return -1 * heapq.heappop(neg_a)

# def prepartition(a, p):
#     answer_lst = []
#     curr_sum = 0
#     num_elements = set(p)
#     for j in num_elements:
#         for i in range(len(p)):
#             if p[i] == j:
#                 curr_sum += a[i]
        
#         answer_lst.append(curr_sum)
#         curr_sum = 0
                
#     return answer_lst

def prepartition(a, p):
  result = [0] * len(a)
  for i in range(len(p)):
    result[p[i]] += a[i]
  
  return result
      
def random_p(n):
  p = []
  for i in range(n):
    p.append(random.randint(0, n - 1))
  return p

def random_move_p(p):
  p2 = []
  for num in p:
    p2.append(num)
  i = random.randint(0, len(p) - 1)
  j = random.randint(0, len(p) - 1)
  while p[i] == j:
    j = random.randint(0, len(p) - 1)
  p2[i] = j
  return p2
    
def repeated_random_part(a, n):
  p = random_p(len(a))
  for i in range(n):
    p2 = random_p(len(a))
    if kk(prepartition(a, p2)) < kk(prepartition(a, p)):
      p = p2
  return p, kk(prepartition(a, p))
  
def hill_climbing_part(a, n):
  p = random_p(len(a))
  for i in range(n):
    p2 = random_move_p(p)
    if kk(prepartition(a, p2)) < kk(prepartition(a, p)):
      p = p2
  return p, kk(prepartition(a, p))

def simulated_annealing_part(a, n):
  p = random_p(len(a))
  p3 = []
  for i in p:
     p3.append(i)
  for i in range(n):
    p2 = random_move_p(p)
    if kk(prepartition(a, p2)) < kk(prepartition(a, p)):
      p = p2
    else:
      probability = math.exp((-(kk(prepartition(a, p2))) - kk(prepartition(a, p))) / t_iter(n))
      if random.random() < probability:
         p = p2
    if kk(prepartition(a, p)) < kk(prepartition(a, p3)):
      p3 = p
  return p3, kk(prepartition(a, p3))
# every num in a is assigned a random number
# that number corresponds to which numbers must be in the same sign

#%%
if int(sys.argv[1]) == 0:
   file = sys.argv[3]
   a = []
   for line in fileinput.input(files = file):
      a.append(int(line))
   match int(sys.argv[2]):
      case 0:
         print(kk(a))
      case 1:
         s, r = repeated_random(a, 25000)
         print(r)
      case 2:
         s, r = hill_climbing(a, 25000)
         print(r)
      case 3:
         s, r = simulated_annealing(a, 25000)
         print(r)
      case 11:
         p, r = repeated_random_part(a, 25000)
         print(r)
      case 12:
         p, r = hill_climbing_part(a, 25000)
         print(r)
      case 13:
         p, r = simulated_annealing_part(a, 25000)
         print(r)


# 0: repeated random
# 1: hill climbing
# 2: simulated annealing
# 3: prepartitioned repeated random
# 4: prepartitioned hill climbing
# 5: prepartitioned simulated annealing
# 6: kk result
# algos = {}
# for i in range(7):
#   algos[i] = []
# for i in range(50):
#   a = []
#   for j in range(100):
#       a.append(random.randint(1, 10 ** 12))
#   algos[6].append(kk(a))
#   _, r = repeated_random(a, 25000)
#   algos[0].append(r)
#   _, r = hill_climbing(a, 25000)
#   algos[1].append(r)
#   _, r = simulated_annealing(a, 25000)
#   algos[2].append(r)
#   _, r = repeated_random_part(a, 25000)
#   algos[3].append(r)
#   _, r = hill_climbing_part(a, 25000)
#   algos[4].append(r)
#   _, r = simulated_annealing_part(a, 25000)
#   algos[5].append(r)


# import seaborn as sns

# sns.histplot(algos[0])
# #%%
# sns.histplot(algos[1])
# #%%
# sns.histplot(algos[2])
# #%%
# sns.histplot(algos[3])
# #%%
# sns.histplot(algos[4])
# #%%
# sns.histplot(algos[5])
# #%%
# sns.histplot(algos[6])






