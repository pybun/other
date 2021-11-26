def sieve(n):
    if n < 2:
        return None
    else:
        list = []
        help = []
        for i in range(2, n + 1):
            if i not in help:
                list.append(i)
                for j in range(i * i, n + 1, i):
                    help.append(j)
        return list

def isprime(n):
    if n < 2:
        return None
    else:
        list = sieve(n)
        if n in list:
            return True
        else:
            return False

def factorization(n):
    if n < 2:
        return None
    else:
        list = []
        help = sieve(n)
        for i in help:
            count = 0
            if n % i == 0:
                while n % i == 0:
                    n //= i
                    count += 1
                list.append([i, count])
        return list

def divisornumber(n):
    if n == 1:
        return 1
    elif n < 1:
        return None
    else:
        list = factorization(n)
        count = 1
        for i in list:
            count *= i[1] + 1
        return count

def iscoprime(n, m):
    if n < 1 or m < 1:
        return None
    else:
        a = divisornumber(n * m)
        d = divisornumber(n) * divisornumber(m)
        if a == d:
            return True
        else:
            return False
        