a='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
a1=a 
a2=a
a3=a
for i in range(0,len(a1)-2,2):
    a1[i]=chr(ord(a1[i])+1)
print(a1)
while (a2.find("Z")>=0):
    a2[a2.find("Z")+1]="A"
print(a2)
while (a3.find(" ")>=0):
    a3[a3.find(" ")+1]="-"
print(a3)
