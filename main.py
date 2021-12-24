fhand = open('mbox-short.txt')
for line in fhand:                      # Handles one line at a time
    shout = line.rstrip().upper()       # Removes newline and capitalizes
    print(shout)

count = 0
total = 0

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos + 1:].strip()
        SPAM_C = float(number)
        total = total + SPAM_C

average = total / count
print('Average spam confidence: ', average)

fname = input('Enter the file name: ')
try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1

print('There were', count, 'subject lines in', fname)str = 'X-DSPAM-Confidence:0.8475'
index = str.find(':')
newStr = str[index+1:-1]
# print(newStr)
newFloat = float(newStr)
# print(newFloat)

