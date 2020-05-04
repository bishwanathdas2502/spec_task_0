# Accept n number from user and calculate the sum of all number between 1 to n including n

def add_(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

if __name__=='__main__':
    n = int(input('Enter the number n'))
    print('sum:',add_(n))
