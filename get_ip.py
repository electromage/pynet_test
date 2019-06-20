#!/usr/bin/env python

ip_address = input("What is the IP address? ")

ip_split = ip_address.split(".")

print("{:<12}{:<12}{:<12}{:<12}".format(ip_split[0],ip_split[1],ip_split[2],ip_split[3]))
