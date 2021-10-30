# TCP Remote shell wordlist attack (Direct bind)

This program will automatically try commands on a target TCP direct shell and display the result

List of arguments:

```
usage: tcp-shell-wordlist.py [-h] [-ip TCP_IP] [-port TCP_PORT]
                             [-w WORDLIST_FILE] [-errstr NOTFOUND_MSG]
                             [-delay DELAY]

optional arguments:
  -h, --help            show this help message and exit
  -ip TCP_IP            *Target ip
  -port TCP_PORT        *Target port
  -w WORDLIST_FILE      List of commands to try
  -errstr NOTFOUND_MSG  Console uknown command string
  -delay DELAY          Delay after sending command
```

To install simply do "pip install -r requirements.txt"

Default wordlist taken from https://github.com/yzf750/custom-fuzzing/blob/master/linux-commands-merged.txt
