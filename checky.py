'''Usage: checky [file path] [checksum type] [checksum provided by creators] OR checky

Welcome to Checky! A program that gets the checksum of a file on your computer and allows you to compare the checksum with the checksum given by the creator of the file to ensure its integrity. 
Checksums are often long and hard to read and even harder to compare. That is where this tool helps. If you have a checksum that is unsupported by the program type in 'custom' when prompted to type the kind of checksum you have.'''

#main is a user defined 

from main import *
from argparse import ArgumentParser

	

parser = ArgumentParser()
parser.add_argument("-file")
parser.add_argument("-hsh")
parser.add_argument("-original_checksum")
args = parser.parse_known_args()
args2 = args[1]

args3 = []
for z in args2:
	args3.append(z)

if len(args3) == 3:
	checksum(args3[0], args3[1], args3[2])
elif 1<=len(args3)<3 or len(args3) > 3:
	print("Incorrect number of arguments. Try again!\nUSAGE: checky [file path] [checksum type] [checksum provided by creators] OR checky")
	system("pause")
	exit()
else:
	main()


