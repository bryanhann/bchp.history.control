import sys
import datetime
strptime=datetime.datetime.strptime

def is_dt_line(line):
    stamp = line.split('.')[0]
    try:
        dt=strptime(stamp,'%Y%m%dt%H%M%S')
        dT=strptime(stamp,'%Y%m%dT%H%M%S')
        return True
    except ValueError:
        return False
with open(sys.argv[1]) as fd:
    acc=[]
    for line in ( fd.readlines() ):
        assert is_dt_line(line)
        line =  line.strip()
        if line[8]=='t':
            line=line[:8] + 'T' + line[9:]
        print( line )
