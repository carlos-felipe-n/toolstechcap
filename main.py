import os

name = os.name
name_so = f'\n{os.uname().sysname}'
name_network = f'\n{os.uname().nodename}'

print(name, name_so, name_network)