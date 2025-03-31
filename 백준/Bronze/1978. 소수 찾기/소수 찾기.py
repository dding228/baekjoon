def count_primes(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

n = int(input())
number=list(map(int, input().split()))

prime_count= sum(1 for n in number if count_primes(n))
print(prime_count)