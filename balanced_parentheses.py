def compareBrackets(p):
    value_closing = "" #side where will be assigned closing brackets (to be compared)
    stack_closing = []
    cond = sizeBrackets(p)  #this fuction will return a boolean to know if each part (stack) of input has the same size (opening and closing brackets)
    if cond:
        for i in p:
            if i in ['[','(','{']:
                if i == '(':
                    value_closing = ')'
                elif i == '[':
                    value_closing = ']'
                elif i == '{':                
                    value_closing = '}'
                stack_closing.append(value_closing)                    
            else:
                if i != stack_closing[len(stack_closing)-1]:
                    return "Not Balanced"
                else:
                    stack_closing.pop()
        return "Balanced"
    else:
        return "Not Balanced"
def sizeBrackets(p):
    cond = True
    stack_opening = []
    stack_closing = []
    for i in p:
        if i in ['[','(','{']:
            stack_opening.append(i)
        else:        
            stack_closing.append(i)
        cond = True if len(stack_opening) == len(stack_closing) else False
    return cond       
        
input_user = input("Enter a set of brackets to check if balanced: ")
print(compareBrackets(input_user))

'''def pop(li):
    lista = li[:]
    ultimo = lista[len(lista)-1]
    lista[len(lista)-1] = None
    return ultimo'''
#create the fuction pop and push from scratch
