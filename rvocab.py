import re

file = open("text.txt")
text = file.read()
file.close()

text = re.sub(r"[\n\r\t]", r" ", text)
text = re.sub(r" {2,}", r" ", text)

print(text)
