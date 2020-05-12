#Importing required modules
import requests
import json
import csv
from config import *

#Set default URL to call Meraki API
mainUrl = "https://api.meraki.com/api/v0"

#API URL to get Networks from Organization
netIdUrl = mainUrl + "/organizations/{}/networks".format(org_id)

#Constructing headers
headers = {
  'Content-Type': 'application/json',
  'X-Cisco-Meraki-API-Key': api_key
}
#Creating the file
f = open("passwords.csv", "a")

#Call the API
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

#Reading the password and saving to file
for network in responseNetJson:
    netId = network['id']
    if network['type'] in ('combined'):
        try:
            ssidUrl = mainUrl + "/networks/{}/ssids".format(netId)
            responseSsid = requests.get(url=ssidUrl, headers=headers)
            responseSsidJson = json.loads(responseSsid.content)
            for ssid in responseSsidJson:
                if ssid['enabled'] == True and ssid['authMode'] == 'psk':
                    tofile = ("Loja: " + network['name'], ", SSID: " + ssid['name'], ", Modo: " + ssid['authMode'], ", Senha: " + ssid['psk'])
                    print ("Salvando as senhas para a loja: " + network['name'])
                    f.writelines(tofile)
                    f.write("\n")       
        except:
            print("Não temos wifi")
f.close()