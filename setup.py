import platform
import sys
import os
print('Welcome to the osripper setup utility')


print("""Python version: %s
system: %s 
machine: %s
platform: %s
version: %s
""" % (
sys.version.split('\n'),
platform.system(),
platform.machine(),
platform.platform(),
platform.version(),
))

if platform.system() == "Darwin":
    print("MacOS detected...  Ultimate Compatibility")
    ngchoice=input('Do you want to install with ngrok support? (y/n): ')
    if ngchoice=='y' or 'Y':
        print('You will need your ngrok Api key (not the tunnel key)')
        print('You can get this key for free from here https://dashboard.ngrok.com/api')
        print('\n')
        ngrok_auth = input('Please enter your key: ')
    os.system("pip3 install -r requirements.txt")
    with open('creds', 'w+') as creds:
        creds.write(str(ngrok_auth))
        creds.close
    ngrok_activation='ngrok authtoken '+ngrok_auth    
    os.system(ngrok_activation)
if platform.system() == "Windows":
    print("This version does NOT support windows. Please use an older version.")
    sys.exit(1)
elif platform.system() == "Linux":
    print("Linux Detected ... Great")
    ngchoice=input('Do you want to install with ngrok support? (y/n): ')
    if ngchoice=='y' or 'Y':
        print('You will need your ngrok Api key (not the tunnel key)')
        print('You can get this key for free from here https://dashboard.ngrok.com/api')
        print('\n')
        ngrok_auth = input('Please enter your key: ')
        os.system("sudo apt install patchelf")
    os.system("pip3 install -r requirements.txt")
    with open('creds', 'w+') as creds:
        creds.write(str(ngrok_auth))
        creds.close   
    ngrok_activation='ngrok authtoken '+ngrok_auth    
    os.system(ngrok_activation) 
    os.system("pip3 install -r requirements.txt")

