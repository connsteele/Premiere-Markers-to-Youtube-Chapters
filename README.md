# PremiereMarkerCleanup
 Convert exported marker.txt file from Premiere into usable YouTube chapters

Usage:
- First input the filepath
- Second input the filename
- A new file called CleanMarks.txt will be created in your filepath
- Call the program using the following "python MarkerClean.py"
- Test input can be found in the examples directory
    - 
- Code runtimes is O(N)

To Do:
- Add guards for code
    - ex) path or file doesn't exist where user wants to read
    - Instead of breaking each line up into a list processing each character in every might be be faster
- Ability to pick minutes or hours as a time format
- Explore multithreading options for input (probably not needed)