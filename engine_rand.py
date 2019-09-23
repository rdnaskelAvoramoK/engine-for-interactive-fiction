from math import ceil
m=["A","B","C","D","E","F","G","H","I","J","K","L"]

q_loc = int(input("Введи количество локаций\n___"))
print("количество ввода данных = ",sum(x for x in range(q_loc)))
b = [0]
n = sk = 0
s = []
#генерация карты
POLE = [b*q_loc for x in range(q_loc)]
#установление связей локаций
for x in range(q_loc):
	for y in range(x+1,q_loc):
		print("Сколько мостов соединяет локацию \"", m[x],"\" и локацию \""+
		 m[y],"\"")
		POLE[y][x] = POLE[x][y] = int(input())
        #подсчёт общего количества связей
		n += POLE[x][y]
	#подсчёт количества связей для локации
	sl = sum(POLE[x]) 
	#подсчёт максимально возможного количества посещений локации
	kf = ceil(sl/2)   
	sk += kf
	#организация справки по карте
	s.append([m[x],sl,kf])
print("всего мостов",n)
for a in POLE:
	print(a)
for t in s:
	print(t)
if (n+1)==sk or n==sk:
	print("True")
else:
	print("Folse")

#выбор начальной точки из условия прохождения всех связей
start_point = list(s[i][0] for i in range(len(s)) if s[i][1]%2)
if start_point==[]:
	start_point = list(s[i][0] for i in range(len(s)))
print("Выбери начальную локацию"," или ".join(list(str(x) for x
 in start_point)))
start_point = input()
s_loc = m.index(start_point)

def unicursal(map,start):
	while sum(map[start])!=0:
		sign = list(m[i] for i in range(len(map[start])) if map[start][i]!= 0)
		print("Ты находишся в", m[start],"локации. \n",
		"можешь переместиться в", " или ".join(sign))
		new_loc=m.index(input())
		map[start][new_loc]-=1
		map[new_loc][start]-=1
		start=new_loc
		
	print("Конец пути. Пока!")

unicursal(POLE,s_loc)