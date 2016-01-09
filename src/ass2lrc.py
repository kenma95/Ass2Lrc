import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "USAGE: python ass2lrc.py filename.ass"
    filename = sys.argv[1][:-4]
    f_in = open(filename+".ass","r")
    f_out = open(filename+".txt","w+")
    for line in f_in:
        if line.startswith("Dialogue:"):
            print line
            phrased = line.split(",")
            f_out.write(phrased[1])
            f_out.write(phrased[9])
    f_out.close()
    f_in.close()
