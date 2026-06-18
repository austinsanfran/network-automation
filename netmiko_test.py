from netmiko import ConnectHandler
device = {
    'device_type': 'cisco_ios',
    'host': '127.0.0.1',
    'username': 'admin',
    'password': 'admin',
}

connection = ConnectHandler(**device)
output = connection.send_command('show version')
print(output)
connection.disconnect()
