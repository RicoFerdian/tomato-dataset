import glob, os, random

os.chdir("images")
# Ratio of train, test, val
ratio = (0.7,0.15,0.15)

filelist = []
trainlist = ''
testlist = ''
vallist = ''

for file in glob.glob("*.png"):
    filelist.append(file)
random.shuffle(filelist)

filecount = len(filelist)
tidx = 0
sidx = 0
vidx = 0
for i, file in enumerate(filelist):
    # the first ratio will goes to training dataset
    if i < filecount*ratio[0]:
        if tidx != 0:
            trainlist += '\n'
        trainlist += str(file)
        tidx += 1
    elif i>=filecount*ratio[0] and i < (filecount*ratio[0])+(filecount*ratio[1]):
        if sidx != 0:
            testlist += '\n'
        testlist += str(file)
        sidx += 1
    elif i>=filecount*ratio[1] and i < (filecount*ratio[0])+(filecount*ratio[1])+(filecount*ratio[2]):
        if vidx != 0:
            vallist += '\n'
        vallist += str(file)
        vidx += 1

text_file = open("D:\\Libraries\\Dataset\\TomatoSSD\\train.txt", "w")
text_file.write(trainlist)
text_file.close()
text_file = open("D:\\Libraries\\Dataset\\TomatoSSD\\test.txt", "w")
text_file.write(testlist)
text_file.close()
text_file = open("D:\\Libraries\\Dataset\\TomatoSSD\\val.txt", "w")
text_file.write(vallist)
text_file.close()
text_file = open("D:\\Libraries\\Dataset\\TomatoSSD\\trainval.txt", "w")
text_file.write(trainlist+'\n'+vallist)
text_file.close()