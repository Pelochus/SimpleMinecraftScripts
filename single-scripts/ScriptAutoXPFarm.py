# Automatiza la granja de XP de Ignacio Landia
# Todo va en segundos

import pyautogui
import os
import time
import ctypes

# ---------- VARIABLES ----------

t = 210 # Variable del tiempo para cambiar mas facilmente el programa (en este caso, es la de que tarda desde estar en el slab hasta volver a matar zombies
tad = 3.55 # Tiempo de izquierda a derecha (Teclas A-D)
tws = 1.82 # Tiempo de adelante a atras (Teclas W-S)
e = 0 # Elapsed time del programa
dur = 3600 # Tiempo que durara el loop y por tanto el programa, desde despues del timesleep inicial

# ---------- SUBPROCESOS, DEFINICIONES Y CLASES ----------

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def hold(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
   
# Convertir los valores feos de DirectInputs a letras legibles: https://gist.github.com/tracend/912308

w = 0x11
a = 0x1E
s = 0x1F
d = 0x20
shift = 0x2A
n1 = 0x02

# ---------- MAIN ----------

time.sleep(8) # Margen que deja antes de empezar a ejecutarse el programa
print("STARTING NOW...")
hold(shift) # Mantiene Shift para evitar morirse de hambre
hold(n1)
release(n1) # NOTA: EL 1 ES EL SITIO DONDE DEBE ESTAR UBICADA LA ESPADA, n1 significa numero 1 del teclado

while e < dur:
	# Movimiento hacia la derecha
	hold(d)
	time.sleep(tad)
	release(d)
	# Movimiento hacia atras
	hold(s)
	time.sleep(tws)
	release(s)
	# Movimiento a la derecha 2
	hold(d)
	time.sleep(tad/2)
	release(d)
	
	# Este trozo es cuando golpea a los zombies
	pyautogui.click()
	time.sleep(0.5)
	pyautogui.click()
		
	# Movimiento hacia la izquierda 2 (opuesto a derecha 2)
	hold(a)
	time.sleep(tad / 1.85)
	release(a)
	# Movimiento hacia delante
	hold(w)
	time.sleep(tws)
	release(w)
	# Movimiento a la izquierda
	hold(a)
	time.sleep(tad)
	release(a)
	
	# Calculos de e y release shift para 
	e = e + (tad*3 + tws*2 + 0.5)
	print("Elapsed time:", e)
	release(shift)
	print("Shift is released; you can now stop the script without possible bugs")
    
	if e >= dur:
		release(shift)
	else:
		time.sleep(t) # Margen de tiempo
		hold(shift)
		print("Shift is hold, try not to stop the program for now (few seconds)")
		e = e + t
		print("Elapsed time:", e)

print("Final elapsed time:", e)
print("Total duration:", dur + 8)
release(shift)
pyautogui.alert("Finished")