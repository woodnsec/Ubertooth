import mmap
import sys
import os

#first arg of script is file name 
f = open(sys.argv[1])
file = sys.argv[1]
convert = 'tshark -V -r ' + file + '> ' + file + '.txt'
command = 'cat ' + str(file) + ' | grep CONNECT_REQ -A 13 -B 26 | tee ' + str(file) + '_results.txt'

#convert the pcap to .txt
print ('Converting ') + sys.argv[1] + (' to a .txt file...\n')
os.system(convert)

#search the converted pcap for CONNECT_REQ
print ('Searching for CONNECT_REQ in: ') + sys.argv[1] + ('\n')

if 'CONNECT_REQ' in open(file).read():
        print 'Connect request found!\n'
        os.system(command)
#     	os.system('cat test.txt | grep CONNECT_REQ -A 13 -B 26')
	sys.exit('End of file - exiting program')
else:
        print 'Could not find Connect request\n'
