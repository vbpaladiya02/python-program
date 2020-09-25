import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(file) as f:
        filelist=f.read().split("\n")
    
    for fi in files:
        if fi not in filelist:
            os.rename(fi,fi.capitalize())
        if os.path.splitext(fi)[1]==format:
            os.rename(fi,f"{i}{format}")
            i+=1


soldier(r"D:\temp",r"D:\Study\test.txt",".jpg")

