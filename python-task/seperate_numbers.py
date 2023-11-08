
q = int(input('number of strings = '))
l = []
for i in range(q):
    a = input(f'{i} String = ')
    l.append(a)
    
#........trivial...solution...........

def solution(s): #s = '99100'
    it_is = 0
    for i in range(len(s)//2): # 0,1
        first = s[:i+1] # for first loop it takes only 9
        # now i generate the rest of array untill its length is less than s
        first = int(first)
        new_string = ''
        inn =0
        while(len(new_string)<len(s)):
            new_string = new_string + str(first+inn)
            inn +=1
        if s == new_string:
            print('YES', first)
            it_is =1
            return
        else: continue

    if it_is==1:pass
    else: print('NO')
        

for i in l:
    solution(i)














'''

def genStr(first,n):
    generated = ''
    for i in range(n):
        generated = generated + str(first+i)

    return generated

for i in l:
    
    if len(i) ==1:
        print('NO')
        continue

    for k in range(1,len(i)//2 + 1):
        gen_str = i[:k]
        int_str1 = int(gen_str)
        no_of_numbers = len(i)//k
        if i == genStr(int_str1, no_of_numbers):
            print('YES', gen_str)
            break
        else: continue
    
    print('NO')
    
'''
    
    
    


















