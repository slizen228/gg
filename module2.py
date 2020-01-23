f=open('mat_dv.txt','r')
l=list()
l8=list()
l9=list()
l10=list()
l11=list()
s=str()
s1=str()
a=int()
b=int()
max8=0
max9=0
max10=0
max11=0
for line in f:
    s=line
    l=s.split('  ')
    if l[2]==8:
        b=l[3]+l[4]
        if b>max8:
            l8=l
            max8=b
        elif b==max8:
            l8.append(l)
    if l[2]==9:
        b=l[3]+l[4]
        if b>max9:
            l9=l
            max9=b
        elif b==max9:
            l9.append(l)
    if l[2]==10:
        b=l[3]+l[4]
        if b>max10:
            l10=l
            max10=b
        elif b==max10:
            l10.append(l)
    if l[2]==11:
        b=l[3]+l[4]
        if b>max11:
            l11=l
            max11=b
        elif b==max11:
            l11.append(l)
print(l8)
print(l9)
print(l10)
print(l11)
