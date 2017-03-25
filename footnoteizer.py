import os
import re

regex = re.compile(r'\[\d\..*?[^\]]\]')
dirname = '_posts/'

for filename in os.listdir(dirname):
    with open(dirname + filename, 'r+') as f:
        found = False
        fileFootnotes = []
        i = 1
        for line in f:
            for m in re.finditer(regex, line):
                fileFootnotes.append([i, m.group(0)])
                # Example: replace 'sat' with 'slept'
                line = line[:m.start()] + "[^"+str(i)+"]" + line[m.end():]
                i = i + 1
                found = True
            if found:
                f.write(line)

        if len(fileFootnotes):
            f.write("\n\n")
            for note in fileFootnotes:
                actualFootnote = "[^"+str(note[0])+"]: "+note[1][4:-1]+"\n\n"
                print actualFootnote
                f.write(actualFootnote)
