import pyautogui as pag
import keyboard
import time
s = "↓ ← ← ← ↓ ← ← ← ← ↓ ← ↓ ↓ → → ↑ ↑ → → → → ↓ → 2"
s1=s.split()
s="↑ ↑ → ↑ ↑ ↑ ↑ → → → ↓ → → ↓ ↓ ↓ ↓ ← ← ↓ 2"
s2=s.split()
s3= "← ← ← ← ← ↓ ↓ ↓ ↓ ← ← ↑ ↓ → → → → → → → → ↑ ↑ ↑ ↑ ↑ ↑ 1"
s3=s3.split()
s4="↓ ↓ ↓ → ↓ ↓ → ↑ ↑ → ↓ ↓ → ↑ ↑ → → ↓ ↓ → → ↑ ↑ 1"
s4=s4.split()
s5="↓ ↓ ↓ ↓ → → → → → ↑ ↓ ↑ ↑ ← ↑ ↑ ← ← ↑ ↑ ↑ 1"
s5=s5.split()
s6="← ↓ → → ↓ ↓ ← ← ↓ ← ← ↓ ↓ → → → → ↑ ↑ ← ← ↓ ↓ ↓ ↓ → → → ↑ ↑ → → → → ↓ ↓ ← ← ↓ → →   2 ← ↓ → → ↓ ↓ ← ← ↓ ← ← ↓ ↓ → → → → ↑ ↑ ← ← ↓ ↓ ↓ ↓ → → → ↑ ↑ → → → → ↓ ↓ ← ← ↓ → → 1"
s6=s6.split()
s7="↑ ↑ ↓ ← ← ↑ ↑ → ↓ ↓ ↓ ← ← ← ↑ ↑ ↑ ↑ → → ↑ ↓ → → → → ↑ ↑ → → ↑ ↑ 2"
s7=s7.split()
s8="← ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → →  2 2"
s8=s8.split()
s9="→ ↑ ↑ → → → → ↓ → → ← ↑ ↑ ↑ → → → → ↓ ↓ → → ↑ ↑ → ← ← ← ↑ ↑ ↑ ← ↑"
s9=s9.split()
s10="← ← ↓ ↓ ↓ → ← ← ← ← ← ← ↓ ↑ ← ↑ ↑ ↑ ← ← ← ← ← ↓ ↓ ↓ → ← ↓"#если найдется гений, который тут рассчитает тайминг, то я буду только рад
s10=s10.split()
def vvod(lst):
	for i in range(len(lst)):
		if lst[i]=='2':
			print(lst[i])
			keyboard.send("2")
		if lst[i]=='1':
			print(lst[i])
			keyboard.send("1")
		if lst[i]=='↓':
			#print(lst[i])
			keyboard.send("down")
		if lst[i]=='←':
			#print(lst[i])
			keyboard.send("left")
		if lst[i]=='↑':
			#print(lst[i])
			keyboard.send("up")
		if lst[i]=='→':
			#print(lst[i])
			keyboard.send("right")
		time.sleep(0.5)


while True:
	if (keyboard.is_pressed("1")):
		vvod(s1)
	
	if (keyboard.is_pressed("2")):
		vvod(s2)
	
	if (keyboard.is_pressed("3")):
		vvod(s3)
	
	if (keyboard.is_pressed("4")):
		vvod(s4)
		time.sleep(1)
		keyboard.send("enter")
		time.sleep(1)
		keyboard.send("up")
		time.sleep(0.5)
		keyboard.send("up")

	if (keyboard.is_pressed("5")):
		vvod(s5)
		
	if (keyboard.is_pressed("6")):
		vvod(s6)
		time.sleep(1)
		keyboard.send("enter")
		time.sleep(1)
	if (keyboard.is_pressed("7")):
		vvod(s7)
	
	if (keyboard.is_pressed("8")):
		vvod(s8)

	if (keyboard.is_pressed("9")):
		vvod(s9)

