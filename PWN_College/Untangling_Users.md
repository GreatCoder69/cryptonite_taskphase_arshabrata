# Untangling Users
Before we start executing commands to get the flag, we have to connect to the server using our SSH key.
The command is as follows :
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Becoming Root with su
### Problem :
![s15480810192024](https://a.okmd.dev/md/67138762efa13.png)
### Solution :
![s15482010192024](https://a.okmd.dev/md/6713876d16b46.png)
```
su
```
We use su to get root access. Usage of su requires entering a password for authentication.
On being prompted, we enter the password hack-the-planet that has been provided in the problem.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{UW5GaRw7R_Ssk6KFA-S4Fu_Ec9P.dVTN0UDL4IDO0czW}
```

## 2. Other Users with su
### Problem :
![s15482910192024](https://a.okmd.dev/md/67138776c93a5.png)
### Solution :
![s15483810192024](https://a.okmd.dev/md/6713877f45a05.png)
```
su zardus
```
We use su zardus to get access to files as the user zardus.
Usage of su requires entering a password for authentication.
On being prompted, we enter the password dont-hack-me that has been provided in the problem.
```
/challenge/run
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{MwrWuL3iw0eBukjppE8HLlxeIYe.dZTN0UDL4IDO0czW}
```

## 3. Cracking Passwords
### Problem :
![s15485010192024](https://a.okmd.dev/md/6713878c85926.png)
![s15490110192024](https://a.okmd.dev/md/671387977e4b5.png)
### Solution :
![s15490810192024](https://a.okmd.dev/md/6713879e36b87.png)
```
john /challenge/shadow-leak
```
We have got a copy of /etc/shadow in /challenge/shadow-leak which contains the hashed values of the passwords stored in the terminal.
We use the program John the Ripper to get the password for zardus. This gives us the password of zardus before hashing it for encryption.
```
su zardus
```
We use su zardus to switch the user to zardus. For authentication, we enter the password we just obtained in the last step.
```
/challenge/run
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{8qHiMR8vi2qJe2bQvGr8S6IgAWl.ddTN0UDL4IDO0czW}
```

##  4. Using sudo
### Problem :
![s15491910192024](https://a.okmd.dev/md/671387a9117a7.png)
![s15494010192024](https://a.okmd.dev/md/671387bdb6a1c.png)
### Solution :
![s15494910192024](https://a.okmd.dev/md/671387c6b4ed4.png)
```
sudo cat /flag
```
We use sudo to get root access and then read the file flag which gives us the flag.
### Flag for the challenge :
```
pwn.college{0H_c_uQ2WVKIIRLZ4UpYqCkj7v-.dhTN0UDL4IDO0czW}
```
