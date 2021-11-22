import os

os.chdir('C:\\Users\\rahma\\Desktop')

pics = (list(x for x in os.listdir() if '.png' in x or '.jpg' in x or '.jpeg' in x))
os.chdir('اسکرین شاتای امروز')
b = (list(x for x in os.listdir()))
for i in b:pics.append(i)
# creating a list with photos #
picstime = []
for i in range(len(pics)):
    if pics[i] in os.listdir():
        picstime.append(os.path.getmtime(pics[i]))
    else:
        os.chdir('..')
        picstime.append(os.path.getmtime(pics[i]))
        os.chdir('اسکرین شاتای امروز')
picstime = sorted(picstime)
# creating a list with photos time #
newpics = []
for i in range(len(picstime)):
    for j in range(len(pics)):
        if pics[j] in os.listdir():
            if picstime[i] == os.path.getmtime(pics[j]) and 'Annotation' in pics[j]:
                newpics.append(pics[j])
        else:
            os.chdir('..')
            if picstime[i] == os.path.getmtime(pics[j]) and 'Annotation' in pics[j]:
                newpics.append(pics[j])
            os.chdir('اسکرین شاتای امروز')
# sorting files #
os.chdir('..')
for file in newpics:
    if file in os.listdir():
        with open(file, 'rb') as src:
            data = src.read()
            with open(f'all screen shots\\{file}', 'wb') as dst:
                dst.write(data)
    else:
        os.chdir('اسکرین شاتای امروز')
        with open(file, 'rb') as src:
            data = src.read()
            with open(f'..\\all screen shots\\{file}', 'wb') as dst:
                dst.write(data)
        os.chdir('..')