# given a number count the number of digit in the number

def count_digit(num):
    num = str(num)
    return len(num)

if __name__=='__main__':
    num = int(input('enter the number'))
    print('number of digit',count_digit(num))