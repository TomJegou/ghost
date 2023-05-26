import os, random, string, sys

all_char = string.printable[:-38]

list_args = sys.argv

def set_hostname(hostname):
    os.system(f"hostnamectl set-hostname {hostname}")

def random_hostname(length):
    r = ""
    for i in range(length):
            r += random.choice(all_char)
    return r

if "-t" in list_args:
    new_hostname = list_args[list_args.index("-t") + 1]
    set_hostname(new_hostname)
    
else: 
    if "-l" in list_args:
        hostname_length = int(list_args[list_args.index("-l") + 1])
        new_hostname = random_hostname(hostname_length)
        set_hostname(new_hostname)
    else:
        hostname_length = random.randint(5,20)
        new_hostname = random_hostname(hostname_length)
        set_hostname(new_hostname)
        
if "-i" in list_args:
    os.system("service NetworkManager stop")
    os.system(f"macchanger -r {list_args[list_args.index('-i') + 1]}")
    os.system("service NetworkManager start")
