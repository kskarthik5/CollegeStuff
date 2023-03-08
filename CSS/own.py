def val(ch):
    if(ch == ' '):
        return 26
    return ord(ch.lower())-97

def sym(val):
    if(val == 26):
        return ' '
    return chr(val+97)

def encrypt(msg):
    temp=""
    n=len(msg)
    for i in range(0,n,2):
        c1=val(msg[i])
        if(i+1<n):
            c1+=val(msg[i+1])
        c2=val(msg[i])
        if(i+1<n):
            c2-=val(msg[i+1])
        if(c2<0):
            c2=100+c2
        if(c1<10):
            c1="0"+str(c1)
        if(c2<10):
            c1="0"+str(c2)
        temp+=str(c1)+str(c2)
    print(temp)
    
def decrypt(cip):
    n=len(cip)
    msg=""
    for i in range(0,n,4):
        apb=int(cip[i]+cip[i+1])
        amb=int(cip[i+2]+cip[i+3])
        if(amb>52):
            amb=amb-100
        n1=(apb+amb)//2
        n2=(apb-amb)//2
        msg+=sym(n1)
        msg+=sym(n2)
    print(msg)
        

while(True):
    c=input("Encrypt(e)/Decrypt(d): ")
    if(c=='e'):
        encrypt(input())
    if(c=='d'):
        decrypt(input())