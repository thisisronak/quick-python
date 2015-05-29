#prints fibonacci series till 100
def main():
  a1, a2 = 0,1
  print a1, " "
  while a2<100:
    print a2," "
    a1, a2 = a2, a1+a2
  read()

#reads lines from a text file
def read():
  f = open("input.txt")
  for x in f:
    print x

    
if __name__ =="__main__":main()
