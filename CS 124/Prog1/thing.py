def primes_upto(limit):
    prime = [True] * limit
    for n in range(2, limit):
        if prime[n]:
            yield n # n is a prime
            for c in range(n*n, limit, n):
                prime[c] = False # mark composites

def generate_list(primes, total_length):
    result_list = [1] * total_length
    for i in range(total_length):
        result_list = result_list[0:i + 1] + [j * primes[i] for j in result_list[i+1:total_length]]
    return result_list

primes = list(primes_upto(542))
total_length = 100
result_list = generate_list(primes, total_length)

for prime in primes[:9]:
    count = sum(1 for item in result_list if item % prime == 0)
    print(f"{prime}: {count}")
