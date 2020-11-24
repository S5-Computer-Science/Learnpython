import sys,os

def main(argc:int,*argv):
    sys.stderr.write("Hello %s"%(argv[1]))
    sys.stderr.write("Have a nice day")

main(len(sys.argv),sys.argv)
     
