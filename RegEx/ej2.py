import re

text = input()
pattern = "\\b((?:E|E-|E )?\\d{4}(?:[-]| )?[A-Z]{3})\\b"
results = re.findall(pattern, text)
for match in results:
   print(match)



