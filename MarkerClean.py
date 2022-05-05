# Created by Connor Steele
from asyncore import write

filepath = input()
filename = input()
fullpath = filepath + '\\' + filename
out = open(filepath + '\\' + 'cleanmarkers.txt', 'w+')

count = 0

out.write("Video Chapters\n")

with open(fullpath, 'r', encoding='utf-16') as f:
    for line in f:
        # Skip the first line
        if (count > 0):
            # Get rid of all whitespace (including tabs)
            strbuf = line.split()
            chari = 0
            for char in strbuf[1]:
                if (chari > 2 and chari < 8):
                    out.write(char)
                chari += 1
            out.write(' ')
            # See if you can make the code below faster
            for i in range (2, len(strbuf)):
                for char in strbuf[i]:
                    out.write(char)
                # Add spaces between words, but not at the end of it all
                if i < len(strbuf) - 1:
                    out.write(' ')
            out.write('\n')
        count += 1        

f.close()
out.close()