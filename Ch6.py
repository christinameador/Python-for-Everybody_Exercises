str = 'X-DSPAM-Confidence:0.8475'
index = str.find(':')
newStr = str[index+1:-1]
# print(newStr)
newFloat = float(newStr)
# print(newFloat)