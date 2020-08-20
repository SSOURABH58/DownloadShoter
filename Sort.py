import os
import shutil

gide={
    "images":['.jpg','.png','.psd','.ico','svg'],
    "documents":['.pdf','.txt','ttf'],
    "sounds":['.mp3'],
    "softwares":['.exe'],
    "ziped":['.zip']
}
defaults = ["images","documents","sounds","softwares","ziped","SHAREit","Sort.exe"]
rootdir = "C:/Users/ssour/Downloads"
testinglidt={
"images":[],
    "documents":[],
    "sounds":[],
    "softwares":[],
    "ziped":[]
}

def soter():
    files=os.listdir(rootdir)
    for file in files:
        if file not in defaults:
            for folder in gide:
                for ext in gide[folder]:
                    if ext in file:
                        testinglidt[folder].append(file)
                        source=rootdir+'/'+file
                        destination=rootdir+'/'+folder+'/'+file
                        shutil.move(source,destination)
                        break
    for files in testinglidt:
        print(files)
        print(testinglidt[files])

if __name__ == '__main__':
    soter()