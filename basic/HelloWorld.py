def main():
    global f
    f="Ganesh"
    print("Hello",f)
    #name=input("Hello, Please provide your name ")
    #print("Nice to meet you",name)


#functions in python
def noArg():
    print("This is no ArgMethod")

def varArg(*args):
    print("Multiple Arg method")
    for item in args:
        print(item)

def multiArg(a, *var):
    print(a)
    for item in var:
        print(var)

def returnMethod(val):
    return val*val


if __name__ == "__main__":
    f="test"
    main()
    print("Main Called !")
    #del f
    print(f)

    #var args can be of any type
    varArg(1,2,"String", 2.0,'a');
    
    multiArg("no-operation");
    
    multiArg("print","Ganesh","Ezhumalai");

    print("square method result:",returnMethod(3))