def prGreen(prt):
    print(f"\033[00;92m{prt}\033[00m")

def OneBinary(N ,L1 ,L2  ,padd):
    s=[]
    L = L2-L1
    print(L)
    endpadding=L%N
    start = L-endpadding
    end = (2 * L)
    for v in range(start,end+1):
        s.append('0')
    for j in range(endpadding,len(s), N):
            if (j+N) < end+1 : s[j] = '1'
    ''' row header'''        
    s.insert(0,str(N).rjust(padd)+'|')
    prGreen(''.join(s))
    return s

def ADDString(a,b , l):
    if a == '1' and b == '1':
        l.append('2')
    elif a =='0' and b == '0':
        l.append('0')
    elif a == '1' and b == '0':
        l.append('1')
    elif a == '0' and b == '1':
        l.append('1')

def addStrings(x,y):
    i = 0
    l=[]
    min_len = min(len(x) , len(y))
    max_len = max(len(x) , len(y))

    while(i< min_len):
        ADDString(x[i] , y[i],l)
        i = i+1

    if max_len == len(y):
        l = l+y[i:max_len]
    elif max_len == len(x):
        l = l+x[i:max_len]   
        
    return l

def GetFList(N,M, max_length):
    L1  = N
    L2 = N * M * max_length #77 * 3#7680 * 3
    #N = N
    padd = len(str(L2-L1))
    V1 = OneBinary(N,L1 , L2, padd)
    l1 = [i+N-L2%N+L1-1 for i , val in enumerate(V1) if val == '1' ]

    print(l1)

    L1  = M
    L2 = N * M * max_length #77 * 3
    #N =M
    padd = len(str(L2-L1))
    V2 = OneBinary(M,L1 , L2, padd)
    l2 = [i+M-L2%M+L1-1 for i , val in enumerate(V2) if val == '1' ] 

    print(l2)
    print(len(V1) , len(V2))

    l =addStrings(V1,V2)
    s=''
    for i , val in enumerate(l):
        if val == '2':
            print(" {} = {} * {} = {} * {} ".format(i , M , int(i/M)  , N, int(i/N) ))
        s = s + str(val)

    #print(s)


def GetFList2(X,Y, max_length):
    L1  = X
    L2 = X * int(X/Y) * max_length #77 * 3#7680 * 3
    N = X
    padd = len(str(L2-L1))
    V1 = OneBinary(N,L1 , L2, padd)
    l1 = [i+N-L2%N+L1-1 for i , val in enumerate(V1) if val == '1' ]

    print(l1)

    L1  = Y
    L2 = X * int(X/Y) * max_length #77 * 3
    M =int(X/Y)
    padd = len(str(L2-L1))
    V2 = OneBinary(M,L1 , L2, padd)
    l2 = [i+M-L2%M+L1-1 for i , val in enumerate(V2) if val == '1' ] 

    print(l2)
    print(len(V1) , len(V2))

    l =addStrings(V1,V2)
    s=''
    for i , val in enumerate(l):
        if val == '2':
            print(" {} = {} * {} = {} * {} ".format(i , M , int(i/M)  , N, int(i/N) ))
        s = s + str(val)

    #print(s)


GetFList(12353, 17  , 10)

#GetFList2(27,9,1)

'''
L1  = 13
L2 = 13 * 7 * 4 #77 * 3#7680 * 3
N = 13
padd = len(str(L2-L1))
V1 = OneBinary(N,L1 , L2, padd)
l1 = [i+N-L2%N+L1-1 for i , val in enumerate(V1) if val == '1' ]

print(l1)

L1  = 7
L2 = 21 * 7 * 4 #77 * 3
N =7
padd = len(str(L2-L1))
V2 = OneBinary(N,L1 , L2, padd)
l2 = [i+N-L2%N+L1-1 for i , val in enumerate(V2) if val == '1' ] 

print(l2)
print(len(V1) , len(V2))

l =addStrings(V1,V2)
s=''
for i , val in enumerate(l):
    if val == '2':
        print(i)
    s = s + str(val)
print(s)
            
          
'''
'''
L1  = 360 * 1
L2 = 360 * 2
N =5
padd = len(str(L2-L1))
start = (L1-L2%N-1) #if L1 ==0  else L1
V1 = OneBinary(N,L1 , L2, padd)
print( [i+start for i , val in enumerate(V1) if val == '1' ])

L1  = 360 * 2
L2 = 360 * 3
N =5
padd = len(str(L2-L1))
start = (L1-L2%N-1) 
V1 = OneBinary(N,L1 , L2, padd)
print( [i+start for i , val in enumerate(V1) if val == '1' ])

L1  = 360 * 3
L2 = 360 * 4
N =5
padd = len(str(L2-L1))
start = (L1-L2%N-1) 
V1 = OneBinary(N,L1 , L2, padd)
print( [i+start for i , val in enumerate(V1) if val == '1' ])
'''
'''
#########TBD
L1  = 11
L2 = 360
N =7
start = (L1+L2%N) if L1 ==0  else L1
padd = len(str(L2-L1))
V1 = OneBinary(N,L1 , L2, padd)
print( [i for i , val in enumerate(V1) if val == '1' ])
'''