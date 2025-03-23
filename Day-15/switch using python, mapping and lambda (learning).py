def switch(value):
    return { "case1": lambda: print("This is case 1"), "case2": lambda: print("This is case 2")}.get(value,"invalid value")

choice="case2"
switch(choice)
switch(("case1"))
switch(5)


'''
learn mapping, lambda, switch use'''
