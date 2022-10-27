import argparse
import sys
import pyfiglet as fig
from colorama import init, Fore
import socket
import time
import queue
import threading
import requests

# __COLOURS
init()
yellow = Fore.LIGHTYELLOW_EX
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
cyan = Fore.LIGHTCYAN_EX
pink = Fore.MAGENTA
reset = Fore.RESET

# __title
title = (fig.figlet_format("PORT SCANNER"))
print(yellow + title + reset)
print("  " * 20, f"~{cyan}*.*{red} SHY.BUG {cyan}*.*{reset}\n")

# __cmd-line arguments
argparse = argparse.ArgumentParser(description=f"{pink} THIS TOOL IS USED TO SCAN THE PORTS IN A NETWORK\n{reset}",
                                   usage=f"{blue}python3 {sys.argv[0]}{pink} -i {reset}<target ip_address>"
                                         f"{pink} -p1 {reset}<starting port_no.>"
                                         f"{pink} -p2 {reset}<ending port_no.>"
                                         f"{pink} -T {reset}<threads>\n")

argparse.add_argument("-i", "--ip", help=f"{green}enter the target ip_address {reset}", required=True)
argparse.add_argument("-p1", "--stport", help=f"{green}enter the staring port no. for scanning{reset}", required=True)
argparse.add_argument("-p2", "--endport", help=f"{green}enter the ending port no. for scanning{reset}", required=True)
argparse.add_argument("-T", "--threads",
                      help=f"{green}enter the no. for threads for multithreaded&fast-output [min:5]{reset}\n",
                      required=True)

args = argparse.parse_args()
ip = args.ip
stport = int(args.stport)
endport = int(args.endport)
thread = int(args.threads)

result = f"\n{cyan} OPEN PORTS:{reset}\n"
qu = queue.Queue()

strt_time = time.time()


def scan(arg):
    global result, bnr
    while not qu.empty():
        port = qu.get()
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"{blue}Scanning for port: {port}")
        try:
            skt.settimeout(3)
            cnt = skt.connect((ip, port))
            try:
                try:
                    bnr = skt.recv(1024).decode()
                except:
                    webrespo = requests.get("http://" + ip)
                    bnr = webrespo.headers['Server']

                bnr = ''.join(bnr.splitlines())
            except:
                bnr = "unknown"
            result += f"{yellow}{time.ctime(time.time())}\n\t {green}[*] port: {reset}{port}{green} is open{reset}\n" \
                      f"\t{red}service running on port:{port}\t{reset}{bnr}\n\n"
            bnr = None
            skt.close()
        except:
            pass
        qu.task_done()


for q in range(stport, endport + 1):
    qu.put(q)

for t in range(thread):
    trd = threading.Thread(target=scan, args=(t,))
    trd.start()
qu.join()

end_time = time.time()
print(result)
print(f"\n Scanning completed for :\n\t    ip: {pink}{ip}{reset}\n"
                                   f"\t ports: {pink}{(endport-stport)+1}{reset}\n"
                                   f"\t  time: {pink}{(end_time-strt_time)} seconds\n")