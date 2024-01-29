# follow.py

import os
import time

def follow(file_path: str):
    f = open(file_path)
    f.seek(0,os.SEEK_END) # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1) # sleep briefly and retry
        else:
            yield line

#while True:
    #fields = line.split(',')
    #name = fields[0].strip('"')
    #price = float(fields[1])
    #change = float(fields[4])
    #if change < 0:
        #print('%10s %10s.2f %10.2f' % (name, price, change))
