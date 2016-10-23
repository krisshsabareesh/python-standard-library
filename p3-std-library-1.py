
import time
start = time.time()

import re
print(re.findall(r'\bf[a-z]*', 'which fruit tree fruit the fastest.'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

import math
print(str(math.cos(math.pi/4)) + '\n')
print( math.log(512, 2))

import random
print(random.choice(['apple', 'mango', 'banana']))
print(random.sample(range(100), 10))
print(random.random())   ###Print a random float value : always less than one
print(random.randrange(10)) ###Print random integer chosen from a range of 1-9

import statistics         ###No module named statistics in Python2
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
###The SciPy project <https://scipy.org> 
###has many other modules for numerical computations.

#from urllib.request import urlopen   ###importing urllib is enough in python2
#with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response :
  #for line in response :
    #line = line.decode('utf-8')   #Decoding the binary data to text
    #if 'EST' in line or 'EDT' in line :
      #print(line)

from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1947, 8, 15)
print(now-birthday)
age = now-birthday
print(age.days)

##Data Compression
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

import smtplib

print()
print(time.time() - start)
