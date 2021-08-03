#linux
# from wifi import Cell
# net=Cell.all("Wi-Fi")
# print(net)
from winwifi import WinWiFi
scan=WinWiFi.scan()
# print(scan)
for i in scan:
    print("SSID : "+i.ssid)
    print("MAC : "+i.bssid)
    print("Encrypt : "+i.encrypt)
    print("Auth : "+i.auth)
    print("strength : "+str(i.strength))
    print("=============================")