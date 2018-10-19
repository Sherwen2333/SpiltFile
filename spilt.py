file= open('source','r')
for i in file.readlines():
    i=i.split(' ')
    z=open(str(i[0]+i[1])+'.txt','w')
    for c in i[2:]:
        z.write(str(c).lower()+'\n')
file.close()