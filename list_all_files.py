# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# it does pattern matching and expansion

import glob
# All files and directories ending with .txt and that don't begin with a dot:
print(glob.glob("/home/adam/*.txt")) 
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
print(glob.glob("/home/adam/*/*.txt")) 
