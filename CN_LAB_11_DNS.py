import socket


def ip_to_hostname(ip_address):
    hostname = socket.gethostbyaddr(ip_address)
    if hostname:
        print("The hostname for ip address :", ip_address, " is :", "https://" + hostname[0])


def hostname_to_ip(hostname):
    ip_address = socket.gethostbyname(hostname)
    print("ip address for :", hostname, " is :", ip_address)


ip_address = "8.8.8.8"
ip_to_hostname(ip_address)
hostname = "www.example.com"
hostname_to_ip(hostname)