import re

text = input()
pattern = "\\b(C\/ |Calle )([A-Z\u00d1ÁÉÍÓÚ]{1}[a-zA-Z\u00f1áéíóúÁÉÍÓÚ\u00d1]+),? +?(Nº |N|n|Nº|N |n |nº |nº)? *?([0-9]+), +([0-9]{5})\\b"
results = re.findall(pattern, text)

#print(results)
for match in results:
    print(match[4] + "-" + match[1] + "-" + match[3])