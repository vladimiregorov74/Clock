
import time
a = list(map(int, input('Установить таймер на сколько времени(ЧЧ ММ СС)?\n>>>').split()))
s = a.pop()
if a:
	s += a.pop()*60
	if a:
		s += a.pop()*3600
while s+1:
	d = '{:02}:{:02}:{:02}'.format(s//3600%24, s//60%60, s%60)
	print(d, end='\r')
	time.sleep(1)
	s -= 1
print('\a\a\a\a')
	