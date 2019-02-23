import subprocess
import sys
import re
import os
import zipfile
import time
import datetime
import shutil

# check if wiki folder exists, if yes then delete existing folder
_MAX_COUNT=5
_GREETING ="Welcome,\n"
_folder = "reader-mediacenterjs.wiki"
_commit = str(subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']))
_branch = subprocess.check_output(['git','branch','-r']).split('\n')[1].split('/')[1]
print 'branch '+_branch
filename = (_branch+"-"+_commit)[:-1]
if os.path.exists(_folder):
        subprocess.call(['chmod', '-R', '+w', _folder])
        shutil.rmtree(_folder)
        print "folder removed"
# clone the wiki dir
subprocess.call(["git","clone","https://github.com/rohitkumar003/reader-mediacenterjs.wiki.git"]) # Cloning
print "clone successful"
os.chdir("./reader-mediacenterjs.wiki/")
print "changed dir"
if(not os.path.isfile(filename+'.zip')):
        shutil.make_archive(filename, 'zip', '../build/debug')
        print "file zipped"
else:
        print exit
artifacts = []

with open('testpage.md', 'r') as f:
	artifacts = f.readlines()
	artifacts = filter(lambda x: x.find('.zip')!=-1, artifacts)
	if(len(artifacts)== _MAX_COUNT):
		searchObj = re.search( r'[\(](.*)[\)]', artifacts[0], re.M|re.I)
		if searchObj:
			file_to_be_removed = searchObj.group(1)
			subprocess.call(['git','rm',file_to_be_removed])
			print 'Artifact removed: '+ file_to_be_removed
		else:
			print 'No Artifact found to remove'

	artifacts = [x.strip('\n') for x in artifacts][0:_MAX_COUNT]
	artifacts.append('['+filename+'] ('+filename+'.zip)')
	print 'contents '+str(artifacts)
with open('testpage.md', 'w+') as f:
	f.write('\n'.join(artifacts))
	f.close()

        
print subprocess.check_output(['git', 'status','-s'])
subprocess.call(["git","add","{0}.zip".format(filename)])
subprocess.call(["git","add","testpage.md"])
subprocess.call(["git","commit","-m"," 'Uploading artifacts'"])
print "changes commit"
subprocess.call(["git","push"])
os.chdir("../")
