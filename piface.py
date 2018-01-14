##import pifacecad_emulator
import pifacecad
import subprocess
from pifacecad.tools.question import LCDQuestion

##cad = pifacecad_emulator.PiFaceCAD()
cad = pifacecad.PiFaceCad()

cad.lcd.backlight_on()
#cad.lcd.write("hello")

#####xo = subprocess.check_output("wifi scan", shell=True).decode('utf-8')
xo = subprocess.check_output("iwlist wlan0 scanning  | grep ESSID", shell=True).decode('utf-8')
###cad.lcd.write(xo)
#print(xo)

ssids = []

for line in xo.split("\n"):
 ssid = line.split('\"')
 if ssid[0] != '': 
  #cad.lcd.write(ssid[1] + '\r') 
  ssids.append(ssid[1])
  #print(ssids)

print(ssids)
#>>> customcad = pifacecad.PiFaceCAD()
cad.lcd.cursor_off()
cad.lcd.blink_off()


question = LCDQuestion(question="Select WiFi net",answers=ssids,selector="#",cad=cad)
answer_index = question.ask()



