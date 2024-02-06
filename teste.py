import re

def is_ipv4(address):
    # Padrão de expressão regular para endereço IPv4 com ou sem CIDR
    ipv4_pattern = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/?\d{0,2}$')
    return ipv4_pattern.match(address) is not None

def is_ipv6(address):
    # Padrão de expressão regular para endereço IPv6
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$')
    return ipv6_pattern.match(address) is not None

# Lista de endereços IP
addresses = ['177.124.128.0/22', '2804:2870::/32', '143.255.200.0/22']

ip_addresses = []

# Verifica se algum dos valores na lista é um endereço IPv4 ou IPv6
for address in addresses:
    if is_ipv4(address):
        ip_addresses.append(address)
    elif is_ipv6(address):
        ip_addresses.append(address)

print (ip_addresses)