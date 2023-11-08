# taking n input from the user
# and printing the sum


def des(a):
    return sum(a)

n = int(input('how many integers are in the string'))
l = []
for i in range(n):
    l.append(int(input(f'enter {i+1}th integer')))
    
result = des(l)

print('sum =',result)


