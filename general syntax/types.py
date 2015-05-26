#types in python

def main():
    a = 1
    print (type(a), a)
    a = (1)
    print (type(a), a)
    a = (1,)
    print (type(a), a)
    a = [1,2,3,4,5]
    print (type (a), a)
    a = 0
    b = 1
    a,b = b,a
    print a, b #and python magic!
    #I may have missed a few like string and stuff

if __name__ == "__main__" : main()
