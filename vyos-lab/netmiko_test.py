from netmiko import ConnectHandler
import time

device = {
    'device_type': 'vyos',
    'host': '192.168.54.129',
    'username': 'vyos',
    'password': 'vyos',
    'global_cmd_verify': False,
}

connection = ConnectHandler(**device)
connection.write_channel('show interfaces\n')
time.sleep(10)
output = connection.read_channel()
print(output)
connection.disconnect()