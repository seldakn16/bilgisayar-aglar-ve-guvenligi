import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    # Subnet maskı ile bir IPv4 ağ adresi oluşturuyoruz
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2  # 2 adres network ve broadcast için

# Örnek kullanım
subnet_mask = 9  # /9 subnet maskını belirtiyoruz

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f"/9 Toplam cihaz sayısı: {total_hosts}")  

# /9 Toplam cihaz sayısı: 8388606

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 10  

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /10 Toplam cihaz sayısı : {total_hosts}")  

# /10 Toplam cihaz sayısı: 4194302

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 11  

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /11 Toplam cihaz sayısı : {total_hosts}")  

# /11 Toplam cihaz sayısı : 2097150

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 12

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /12 Toplam cihaz sayısı : {total_hosts}")  

#/12 Toplam cihaz sayısı : 1048574 

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 13

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /13 Toplam cihaz sayısı : {total_hosts}")  

# /13 Toplam cihaz sayısı : 524286

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 14

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /14 Toplam cihaz sayısı : {total_hosts}")  

#/14 Toplam cihaz sayısı : 262142

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 15

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /15 Toplam cihaz sayısı : {total_hosts}")  

# /15 Toplam cihaz sayısı : 131070

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 16

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /16 Toplam cihaz sayısı : {total_hosts}")  

#  /16 Toplam cihaz sayısı : 65534

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 17

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /17 Toplam cihaz sayısı : {total_hosts}")  

#  /17 Toplam cihaz sayısı : 32766

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 18

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /18 Toplam cihaz sayısı : {total_hosts}")  

# /18 Toplam cihaz sayısı : 16382


############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 19

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /19 Toplam cihaz sayısı : {total_hosts}")  


# /19 Toplam cihaz sayısı : 8190

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 20

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /20 Toplam cihaz sayısı : {total_hosts}")  

# /20 Toplam cihaz sayısı : 4094

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 21

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /21 Toplam cihaz sayısı : {total_hosts}")  

# /21 Toplam cihaz sayısı : 2046

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 22

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /22 Toplam cihaz sayısı : {total_hosts}")  

#  /22 Toplam cihaz sayısı : 1022

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 23

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /23 Toplam cihaz sayısı : {total_hosts}")  

#/23 Toplam cihaz sayısı : 510

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 24

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /24 Toplam cihaz sayısı : {total_hosts}")  

#  /24 Toplam cihaz sayısı : 254

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 25

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /25 Toplam cihaz sayısı : {total_hosts}")  

# /25 Toplam cihaz sayısı : 126

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 26

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /26 Toplam cihaz sayısı : {total_hosts}")  

#  /26 Toplam cihaz sayısı : 62

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 27

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /27 Toplam cihaz sayısı : {total_hosts}")  

#/27 Toplam cihaz sayısı : 30

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 28

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /28 Toplam cihaz sayısı : {total_hosts}")  

#/28 Toplam cihaz sayısı : 14

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 29

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /29 Toplam cihaz sayısı : {total_hosts}")  


#/29 Toplam cihaz sayısı : 6

############################################

import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2 

subnet_mask = 30

total_hosts = hosts_from_subnet_mask(subnet_mask)
print(f" /30 Toplam cihaz sayısı : {total_hosts}")  

#  /30 Toplam cihaz sayısı : 2

