import re

text = input()
pattern = "\\b(([a-z]{1})\.([a-z]{2,})\.(\d{4})\@alumnos\.urjc\.es)|(([a-z]+)\.([a-z]{2,})\@urjc\.es)\\b"
results = re.findall(pattern, text)

for match in results:
    if (len(match[1]) == 1):
        print("alumno " + match[2] + " matriculado en " + match[3])
    else:
        print("profesor " + match[5] + " apellido " + match[6])