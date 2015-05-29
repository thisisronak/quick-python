#getting to know placeholders, much like a format specifier in good old langauges


def main():
    f = open('input.txt')
    #basic usage enumerate, returns an index and the corresponding character/line/string/number
    for index, char in enumerate(f):
        print index, char
    f = 'this is an example'
    for index, char in enumerate(f):
        print index, char
    #getting to know placeholders
    for index, char in enumerate(f):
        if char=='s':
            print 'index {} is an s'.format(index)
    # use continue and break as loop conditionals
    
if __name__ == "__main__":main()
