from netmiko import ConnectHandler
import converter

#Cisco Devices in the network Seperated by a Comma and in Double Qoutes ["0.0.0.0"]
all_devices = ['']


#Attention this is not a secure way to store passwords in a file!!
#USERNAME
username = ''

#PASSWORD
password = ''

#SECRET
enable_secret = ''


for ip in all_devices:
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
        'secret':enable_secret,
    }
    #initiate SSH Connection and Authenticate
    net_connect = ConnectHandler(**device)
    #Get Device Hostname
    hostname = net_connect.find_prompt()
    hostname = hostname[:-1]
    #Go into Privilage Exec Mode
    net_connect.enable()
    #run show running-config 
    output = net_connect.send_command("show running-config")
    #terminate session
    net_connect.disconnect()
    #write the output into a file 
    with open(f"{hostname}.txt",'w+') as f:
        f.write(output)
    converter.create_xml_json(hostname)    