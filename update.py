# update code

import os
import sys

#os.system('git init')
os.system('git add .')

#os.system('git remote rm origin')
#os.system('git remote add origin git@github.com:izlyforever/sourceCode.git')
if len(sys.argv) < 2:
	os.system('git commit -m "update"')
else:
	os.system('git commit -m "' + ' '.join(sys.argv[1:]) + '"')

os.system('git push origin master')
# os.system('git push -f origin master')
