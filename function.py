#function calling
def biggest(n1, n2):
    if n1>n2:
        print(n1, 'is greater')
    else:
        print(n2, 'is greater')

no1 = int(input('enter no1: '))
no2 = int(input('enter no2: '))

biggest(no1, no2)
