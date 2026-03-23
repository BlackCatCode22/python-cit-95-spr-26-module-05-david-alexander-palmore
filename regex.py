import re

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))