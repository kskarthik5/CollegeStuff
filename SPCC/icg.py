
st=input()
ans=0
num=""
op=""
ops=[]
nums=[]
prev=""
icg=""
sym={}
n=1
icg=[]
for i in range(len(st)):
    if(op in ['+','-','*','/']):
        ops.append(op)
        op=""
        nums.append(int(num))
        num=""
    if(ord(st[i])>=48 and ord(st[i])<=57):
        num=num+st[i]
    else:
        op=op+st[i]
if(num!=""): nums.append(int(num))
while(len(ops)!=0):
    try:
        a=ops.index('/')
        v='t'+str(n)
        n1=nums[a]
        n2=nums[a+1]
        if(isinstance(n1,str)):
            n1=sym[n1]
        if(isinstance(n2,str)):
            n2=sym[n2]
        sym[v]=n1/n2
        icg.append('{}={}/{}'.format(v,nums[a],nums[a+1]))
        nums[a]=v
        nums.pop(a+1)
        ops.pop(a)
        n+=1
    except:
        try:
            a=ops.index('*')
            v='t'+str(n)
            n1=nums[a]
            n2=nums[a+1]
            if(type(n1) is str):
                n1=sym[n1]
            if(type(n2) is str):
                n2=sym[n2]
            sym[v]=n1*n2
            icg.append('{}={}*{}'.format(v,nums[a],nums[a+1]))
            nums[a]=v
            nums.pop(a+1)
            ops.pop(a)
            n+=1
        except:
            try:
                a=ops.index('-')
                v='t'+str(n)
                n1=nums[a]
                n2=nums[a+1]
                if(type(n1) is str):
                    n1=sym[n1]
                if(type(n2) is str):
                    n2=sym[n2]
                sym[v]=n1-n2
                icg.append('{}={}-{}'.format(v,nums[a],nums[a+1]))
                nums[a]=v
                nums.pop(a+1)
                ops.pop(a)
                n+=1
            except:
                try:
                    a=ops.index('+')
                    v='t'+str(n)
                    n1=nums[a]
                    n2=nums[a+1]
                    if(type(n1) is str):
                        n1=sym[n1]
                    if(type(n2) is str):
                        n2=sym[n2]
                    sym[v]=n1+n2
                    icg.append('{}={}+{}'.format(v,nums[a],nums[a+1]))
                    nums[a]=v
                    nums.pop(a+1)
                    ops.pop(a)
                    n+=1
                except:
                    break
print("\nIntermediate Code - ")
print('\n'.join(icg))
print("\nAns: ",sym[nums[0]])
