def in2pos(exp):
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    op=[]
    stack=[]
    for i in exp:
        if(i.isalnum()):
            op.append(i)
        elif i=='(':
            stack.append(i)
        elif(i==')'):
            while(stack[-1]!='('):
                op.append(stack.pop())
            stack.pop()
        else:
            while stack  and precedence.get(i,0)<=precedence.get(stack[-1],0):
                op.append(stack.pop())
            stack.append(i)
        #print("Output : ",op,"\tstack : ",stack)
    while(stack):
        op.append(stack.pop())
    return " ".join(op)
print(in2pos(input("Enter the infix Expression : ")))
