import ablib
import time

lcd = ablib.Daisy24(0)
lcd.backlighton()

while True:
	lcd.clear()
	lcd.setdoublefont()
	lcd.putstring("Hello World !")

	time.sleep(1)

	lcd.clear()
	lcd.setsinglefont()
	lcd.putstring("Hello World !")

	time.sleep(1)

