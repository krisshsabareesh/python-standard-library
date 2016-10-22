#Python

##________________
##Output formating
##----------------
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width=30)

##______________________________________________________________________________
"""The textwrap module formats paragraphs of text to fit a given screen width"""
##------------------------------------------------------------------------------
import textwrap
doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width=40))

##_________________________________________________________________________________________________________________
"""The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. 
This allows users to customize their applications without having to alter the application."""
##_________________________________________________________________________________________________________________
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

##___________________________________________________________________________________________________________________
"""The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument.
For mail-merge style applications, user supplied data may be incomplete and the safe_substitute() method may be more
appropriate — it will leave placeholders unchanged if data is missing"""
##___________________________________________________________________________________________________________________
t = Template('Return the $item to $owner.')  ##here is a non-ascii character and the encoding must be specified in python2 to get the result printed...else it will raise an error.
d = dict(item='unladen swallow')
try :
  t.substitute(d)
except :
  print("Caught the raised error")
print(t.safe_substitute(d))

##___________________________________________________________________________________________________________________
"""The locale module accesses a database of culture specific data formats. The grouping attribute of locale’s format 
function provides a direct way of formatting numbers with group separators"""
##___________________________________________________________________________________________________________________
import locale
print(locale.setlocale(locale.LC_ALL,'en_US.utf8'))
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))

##___________________________________________________________________________________________________________________
"""Template subclasses can specify a custom delimiter. For example, a batch renaming utility for a photo browser may 
elect to use percent signs for placeholders such as the current date, image sequence number, or file format"""
##___________________________________________________________________________________________________________________
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

##______________________________________________________________________________________________________________________
"""The struct module provides pack() and unpack() functions for working with variable length binary record formats. The 
following example shows how to loop through header information in a ZIP file without using the zipfile module.
Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. The "<" indicates that they are 
standard size and in little-endian byte order"""
##______________________________________________________________________________________________________________________
import struct
with open('../pythonStdLibrary.zip','rb') as f :
    data = f.read()
start = 0
for i in range(1) :
    start += 14
    fields = struct.unpack('<IIIH',data[start:start+14])
    print(fields)
    crc32, comp_size, uncomp_size, filenamesize = fields
    start += 16
    filename = data[start: start+filenamesize]
    start += filenamesize
    print(filename, hex(crc32), comp_size, uncomp_size, sep = ' <--> ')

##_____________________________________________________________________
"""At its simplest, log messages are sent to a file or to sys.stderr"""
##_____________________________________________________________________
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


##__________________________T_O_O_L_S___F_O_R___W_O_R_K_I_N_G___W_I_T_H___L_I_S_T_S______________________________________
"""The array module provides an array() object that is like a list that stores only homogeneous data and stores it more 
compactly. The following example shows an array of numbers stored as two byte unsigned binary numbers (typecode "H") 
rather than the usual 16 bytes per entry for regular lists of Python int objects"""
##_______________________________________________________________________________________________________________________
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

##_______________________________________________________________________________________________________________________
"""The collections module provides a deque() object that is like a list with faster appends and pops from the left side
but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches"""
##_______________________________________________________________________________________________________________________
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

unsearched = deque([1])
def breadth_first_search(unsearched) :
  node = unsearched.popleft()
  for m in gen_moves(node) :
    if is_goal(m) :
      return m
    unsearched.append(m)
