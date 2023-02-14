grammar={"S":["Aa","Ba"],
        "A":["Ba"],
        "B":["c"]
}
def getFirst(sym):
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
    print(s)
        
def getFollow(sym):
    s=set()
    

i=0
# while(True):
#     args=input("Enter Production Rule (Enter - to stop) > ").split()
#     if(len(args)==0 or args[0]=="-"):
#         break
#     grammar[args[0]]=args[1:]
# print(grammar)
while(True):
    args=input("First(0),Follow(1) : <val> > ").split()
    if(args[0]=='0'):
        getFirst(args[1])
    if(args[0]=='1'):
        getFollow(args[1])
