from math import ceil
m=["A","B","C","D","E","F","G","H","I","J","K","L"]
q_loc=int(input("Введи количество локаций\n___"))
print("количество ввода данных = ",sum(x for x in range(q_loc)))
b=[0]
n=sk=0
s=[]
#генерация карты
POLE=[b*q_loc for x in range(q_loc)]
#установление связей локаций
for x in range(q_loc):
	for y in range(x+1,q_loc):
		print("Сколько мостов соединяет локацию \"", m[x],"\" и локацию \""+
		 m[y],"\"")
		POLE[y][x]=POLE[x][y]=int(input())
        #подсчёт общего количества связей
		n += POLE[x][y]
	#подсчёт количества связей для локации
	sl=sum(POLE[x]) 
	#подсчёт максимально возможного количества посещений локации
	kf=ceil(sl/2)   
	sk+=kf
	#организация справки по карте
	s.append([m[x],sl,kf])
print("всего мостов",n)

for a in POLE:
    print(a)

for t in s:
	print(t)

if (n+1)==sk:
	print("True")
else:
	print("Folse")