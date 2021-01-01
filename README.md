# StandardShell
Build a standard shell

## Working
* Shell is built by stdin and stdout. Take stdin and give stdout. This module is useful during RCE.
```python
from standard-shell import LinuxShell
```
* To develop a shell define stdout yourself. stdin is predefined as keyboard input.
```python
def rce_code(self, cmd):
	""" Write RCE Code to send command and return cmd output """
	return output
LinuxShell.stdout = rce_code #pwd should return /home/username
```
* Boom, You got a shell  
```python
rootshell = LinuxShell('root')
rootshell.interact()
root@machine:/root#
```
