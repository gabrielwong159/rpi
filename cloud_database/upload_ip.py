#!/usr/bin/python3
# put in /etc/rc.local
import netifaces as ni
from firebase import firebase
from firebase_config import *

# url = <url>
# secret = <secret>
# email = <email>
auth = firebase.FirebaseAuthentication(secret, email, True, True)
firebase = firebase.FirebaseApplication(url, auth)

DEVICE_NAME = "Raspberry_Pi"

def get_ip_addresses():
    ip_addresses = {}
    for interface in ni.interfaces():
        if_address = ni.ifaddresses(interface)
        if ni.AF_INET in if_address:
            ip_addresses[interface] = if_address[ni.AF_INET][0]['addr']

    return ip_addresses

def put_ip_addresses(name):
    for k,v in get_ip_addresses().items():
        firebase.put(DEVICE_NAME, k, v)
    print("All IP addresses of {} uploaded".format(name))

put_ip_addresses(DEVICE_NAME)
#d = firebase.get(DEVICE_NAME, None)
