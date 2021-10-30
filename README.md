# TCP Remote shell wordlist attack (Direct bind)

This program will automatically try commands on a target TCP direct shell and display the result

List of arguments:

```
  -ip -> Target IP
  -port -> Target port
  -w -> Wordlist file to read from (default: linux-commands-merged.txt)
  -errstr -> Uknown command string to match (default: No such command)
  -delay -> Delay after every sent command (default: 0.25). Increasing this value might be necessary if there's a high ping or a cooldown
```

To install simply do "pip install -r requirements.txt"

Default wordlist taken from https://github.com/yzf750/custom-fuzzing/blob/master/linux-commands-merged.txt
