# Hossein Ahmadi
# My WebLog : https://mrpython.blog.ir
# Detect Mobile Model From Picture


from os import popen,path
from sys import argv


def help():
    print ("""
    Usage : python3 detect-mob.py <picture address>
    Example : python3 detect-mob.py ~/Desktop/mob.jpg
    """)
    exit()

def notExist(file):
    print ("""
    Error : {} Not Exist :(
    """.format(file))
    exit()
if len(argv) < 2:
    help()
else:
    if path.isfile(argv[1]) == False :
        notExist(argv[1])
    

pic = argv[1]
command = "exif {} | grep Model".format(pic)
model = popen(command).read().strip("\n")
try :
    model = model[(model.index("|") + 1):]
except : 
    print ("Sorry . There are some problems :(")
    exit()
print("Model : {}".format(model))
command = "firefox https://www.google.com/search?q=\"{}\"".format(model)
popen(command)

