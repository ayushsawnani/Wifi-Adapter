from warnings import catch_warnings
import os





#open up wifi bands
cmd = 'airport -s'
import subprocess

list = subprocess.check_output(cmd, shell=True).decode("utf-8")

ssid = []
rssi = []

networks = {}

for line in list.splitlines():
    print(line)

    if line.split()[0] == 'SSID': 
        continue

    try:

        if int(line.split()[1]) < 0:
            if line.split()[0] in networks.keys():
                if int(line.split()[1]) > networks[line.split()[0]]:
                    networks[line.split()[0]] = int(line.split()[1])
            else:
                networks[line.split()[0]] = int(line.split()[1])
        
    except:
        continue

    

print(networks)





#see which one is the lowest
min = -9999999999
best_network = ""
for key in networks.keys():
    if networks[key] > min:
        min = networks[key]
        best_network = key

print(min)
print(best_network)
#sets the wifi to that one

cmd2 = 'networksetup -setairportnetwork en0 ' + best_network
os.system(cmd2)