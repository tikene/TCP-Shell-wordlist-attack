# TCP Remote shell wordlist attack (Direct bind)

**This program will automatically try a list of commands on a TCP direct shell and display the results**

![fe36c8d9e21edad138a8e4b231d6ab56 (1)](https://user-images.githubusercontent.com/92279236/139542496-2c49a72c-000f-4043-a9ac-37accdd950d9.gif)

**Arguments:**

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

**Installation:**

To install simply do "pip install -r requirements.txt"

**Credits:**

Default wordlist taken from https://github.com/yzf750/custom-fuzzing/blob/master/linux-commands-merged.txt
