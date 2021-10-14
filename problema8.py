a=str(input("Introduceti sirul"))
sir1=""
sir2=""
sir3=""
for i in a:
    if (ord(i)>=65)and(ord(i)<=89):
        sir1+=chr(ord(i)+1)
    else:
        sir1+=i
print("a)Inlocuieste litele de la A pana la Y cu urmatoarea litera: \n",sir1)
for i in a:
    if i=='Z':
        sir2+="A"
    else:
        sir2+=i
print("b)Inlocuieste litele de Z cu A: \n",sir2)
for i in a:
    if i==' ':
        sir3+="-"
    else:
        sir3+=i
print("c)Inlocuieste spatiu cu - : \n",sir3)
