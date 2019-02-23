import subprocess
import sys
import re
import os
import zipfile
import time
import datetime
import shutil

# check if wiki folder exists, if yes then delete existing folder
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
		
with open('testpage.md','a+') as f:
        f.write("\n["+filename+"] ("+filename+".zip)" )
        f.close()
        
print subprocess.check_output(['git', 'status','-s'])
os.system('git add %s.zip '%filename)
os.system('git add testpage.md')
os.system("git commit -m 'Uploading artifacts'")
print "changes commit"
os.system('git push')
os.chdir("../")
##def get_file_count():
##    zipCounter = len(glob.glob1("./reader-mediacenterjs.wiki","*.zip"))
##    print zipCounter
#def get_delete_old_files():
##    now = time.time()
##    folder = './folder_name'
##    #files = [os.path.join(folder, filename) for filename in os.listdir(folder)]
##    for dirpath, dirnames, filenames in os.walk(folder):
##        for filename in filenames:
##            curpath = os.path.join(dirpath,filename)
##            if filename.endswith(".zip"):
##                #file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
##                #if datetime.datetime.now() - file_modified > datetime.timedelta(hours=1):
##                    #os.remove(curpath)
