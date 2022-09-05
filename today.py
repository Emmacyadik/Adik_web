f=open("file1.txt")
for line in f:
	date=line.split(' ')
	
	name=[0]
	wins = str (date[1])
	losses = str (date[2])

	win_percent = 100 * wins / (wins + losses)
	print (f"{name} : wins {win_percent: .2f}%")
