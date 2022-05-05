# Created by Connor Steele
print("Path to input file:")
filepath = input()
print("File to process:")
filename = input()
fullpath = filepath + '\\' + filename

# Make sure the full path to the file is valid
try:
    f = open(fullpath, 'r', encoding='utf-16')
except OSError:
    fullpath = "\"" + fullpath + "\""
    print("\nInput file does not exist:", fullpath)
    print("Program will now terminate\n")
    quit()

out = open(filepath + '\\' + 'CleanMarks.txt', 'w+')
count = 0
out.write("Video Chapters\n")

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
        # Write all remaining characters in the line and seperate words
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