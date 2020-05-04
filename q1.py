# Accept two number from user and return their product and if product is greater than 1000 return their sum


def product_(num1 , num2):
    return num1 * num2
def addition_(num1,num2):
    return num1 + num2

if __name__=='__main__':
    num1 = int(input('Enter 1st number'))
    num2 = int(input('enter 2nd number'))

    prod = product_(num1,num2)
    print('product:',prod)
    if prod > 1000:
        print('addition',addition_(num1,num2))
