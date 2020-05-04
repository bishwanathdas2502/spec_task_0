# write a python program to print fibonacci series and also check whether a given input number is fibonacci
# number or not

def is_fibo(n):
    a = []
    a.append(0)
    a.append(1)
    flag = True
    while flag:
        a.append(a[-1] + a[-2])
        if a[-1] == n:
            return True
        elif a[-1] > n:
            flag = False
    return False

def fibo(nth):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2,nth+1):
        a.append(a[-1]+a[-2])
    return a

if __name__ == '__main__':
    nth = int(input("enter the number of terms of fibonacci series "))
    n = int(input('enter the number to be checked in fibonacci series '))
    arr = fibo(nth)
    for num in arr:
        print(num,end = " ")
    print(f'\n{n} is a fibonacci number: {is_fibo(n)}')


