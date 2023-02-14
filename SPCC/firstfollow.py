grammar={
}
def getFirst(sym):
    if( sym not in grammar.keys()):
        return sym
    s=set()
    def first(sym):
        vals=grammar[sym]
        for e in vals:
            if(e[0] >="A" and e[0]<="Z"):
                first(e[0])
            else:
                s.add(e[0])
    for e in grammar[sym]:
        if(e[0] >="A" and e[0]<="Z"):
            first(e[0])
        else:
            s.add(e[0])
    return s
        
def getFollow(val):
    s=set()
    def follow(sym):
        for e in grammar.keys():
            for i in grammar[e]:
                if sym in i:
                    #rules
                    if(i[-1]==sym):
                        follow(e)
                    else:
                        new=i[i.index(sym)+1]
                        if(new >="A" and new<="Z"):
                            follow(new)
                        else:
                            s.add(getFirst(new))
    follow(val)
    return s
    
i=0
while(True):
    args=input("Enter Production Rule (Enter - to stop) > ").split()
    if(len(args)==0 or args[0]=="-"):
        break
    grammar[args[0]]=args[1:]

while(True):
    args=input("First(0)/Follow(1) : <val> > ").split()
    if(len(args)==0):
        break
    res=None
    if(args[0]=='0'):
        res=getFirst(args[1])
    if(args[0]=='1'):
        res=getFollow(args[1])
    print(*res)