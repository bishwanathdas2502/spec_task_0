# print all prime between an interval and check whether a given number is prime or not


def is_prime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def prime_interval(low,high):
    ans = []
    for i in range(low,high+1):
        if is_prime(i):
            ans.append(i)
    return ans

if __name__ == '__main__':
    low,high = map(int,input('enter low and high of range with spaces in between').split())
    num = int(input('Enter the number to be checked as prime'))
    ans = prime_interval(low,high)
    print('primes in the interval:')
    for i in ans:
        print(i,end = " ")
    print(f'\n{num} is prime:{is_prime(num)}')

