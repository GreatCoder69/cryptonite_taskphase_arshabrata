# Pondering PATH
Before we start executing commands to get the flag, we have to connect to the server using our SSH key.
The command is as follows :
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. The PATH Variable
### Problem :
![s15581910192024](https://a.okmd.dev/md/671389c5caeb7.png)
### Solution :
![s15582810192024](https://a.okmd.dev/md/671389cd9cb6b.png)
```
PATH=""
```
We set the path to blank so that bash cannot find the rm command.
```
/challenge/run
```
The command tries to remove the flag but the blank path does not allow it to find the rm command.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{ghnDJFJDef6kpAsXLjNWUbGw_oN.dZzNwUDL4IDO0czW}
```

## 2. Setting PATH
### Problem :
![s15583810192024](https://a.okmd.dev/md/671389d7df660.png)
### Solution :
![s15584610192024](https://a.okmd.dev/md/671389e0284a2.png)
```
PATH="/challenge/more_commands"
```
We set the path to /challenge/more_commands because /challenge/run invokes the win command which only exists in this directory.
```
/challenge/run
```
This invokes the command win which gives us the flag.
### Flag for the challenge :
```
pwn.college{cKehOE_cJjAx9_gvgrnCaELHsvC.dVzNyUDL4IDO0czW}
```

## 3. Adding Commands
### Problem :
![s15585510192024](https://a.okmd.dev/md/671389e9c491f.png)
### Solution :
![s15591910192024](https://a.okmd.dev/md/67138a009b9c2.png)
```
touch win
```
Create a file win using touch.
```
nano win
```
We must use read since it is an inbuilt function that is not affected by PATH.
We write the following inside the win file :
read flag < /flag
echo "$flag"

```
cat win
```
Read the contents of the file.
```
chmod a+x win
```
Make the file executable for all users that can access the file.
```
PATH="/home/hacker"
```
We set the PATH to the location of win.
```
/challenge/run
```
This invokes the win command we just created.
This reads out the flag.
### Flag for the challenge :
```
pwn.college{A5sGw4ZQtfXXgoFHOvBfqPR6MpI.dZzNyUDL4IDO0czW}
```

## 4. Hijacking Commands
### Problem :
![s15593310192024](https://a.okmd.dev/md/67138a0e71df4.png)
### Solution :
![s15594410192024](https://a.okmd.dev/md/67138a1a3e691.png)
```
touch rm
```
Create a file rm using touch.
```
nano rm
```
We must use read since it is an inbuilt function that is not affected by PATH.
We write the following inside the rm file :
read flag < /flag
echo "$flag"

```
cat rm
```
Read the contents of the file.
```
chmod a+x rm
```
Make the file executable for all users that can access the file.
```
PATH="/home/hacker"
```
We set the PATH to the location of the rm file we just created.
```
/challenge/run
```
This tries to remove the file using rm but in the new path we provided, the rm command has been replaced by a command of our own.
This reads out the flag by using the rm function we just created.
### Flag for the challenge :
```
pwn.college{c5guUBWED38lFG02SdV4vwT6w3U.ddzNyUDL4IDO0czW}
```
