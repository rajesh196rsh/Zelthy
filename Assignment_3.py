#importing the required libraries
import subprocess
import os

#code the find the available networks
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
available_networks = networks.decode('ascii')
available_networks = available_networks.replace("\r","")
print("Below is the available networks")
print(available_networks)

#Function to connect the wifi based on the available networks
def connectWifi(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    os.system(command)
  
# function to connect to the wifi network    
def connect(name, SSID):
    command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    os.system(command)
  
  
# input wifi name and password
name = input("Pleae provide the Wi-Fi name from the above list to connect ")
password = input("Password: ")
  
# establish new connection
connectWifi(name, name, password)
  
# connect to the wifi network
connect(name, name)
print("If wifi {} is not connected please use the correct password to connect".format(name))