#fizzbuzz.py 
#Author: Henry Tay

import sys, getopt

def main(argv):
    """
    Fizzbuzz is a program that counts between the integers 1 and 100, replacing
    multiples of 3 with the string 'fizz' and multiples of 5 with the string 
    'buzz' and multiples of both 3 and 5 with the string 'fizzbuzz'. The number
    to count to and the multiples with which to replace can be specified by the
    user.
    """
    #Set default parameters
    params = [False, 3, 5, 100]
    processOptions(argv, params)
    help, fizz, buzz, N = (params[0], params[1], params[2], params[3])
    if help:
        usage(0)
    for i in range(1,N+1):
        output = ""
        if i % fizz == 0:
            output += "fizz"
        if i % buzz == 0:
            output += "buzz"
        if output == "":
            output = i
        print output
    
    
def usage(exitOption):
    print ("usage: fizzbuzz.py \n \t -h : Print usage."
            "\n \t -f <fizzNumber>: Set fizz number. Default is 3."
            "\n \t -b <buzzNumber>: Set buzz number. Default is 5."
            "\n \t -n <N>: Numbers counted. Default is 100.")
    sys.exit(exitOption)
    
def processOptions(argv, params):
    """
    Processes command line options and sets the value of program parameters
    accordingly.
    """
    try:
        opts, args = getopt.getopt(argv, "hf:b:n:")
    except:
        print "Error: unrecognized option."
        usage(2)
        
    for opt, arg in opts:
        if opt == '-h':
            params[0] = True
        if opt == '-f':
            params[1] = int(arg)
        if opt == '-b':
            params[2] = int(arg)
        if opt == '-n':
            print arg
            params[3] = int(arg)
    
    return
        
if __name__ == "__main__":
    main(sys.argv[1:])
        
    