# Perceiving Permissions
Before we start executing commands to get the flag, we have to connect to the server using our SSH key.
The command is as follows :
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Changing File Ownership
### Problem :
![s10063410192024](https://a.okmd.dev/md/671384adc5fcf.png)
![s10064410192024](https://a.okmd.dev/md/671384b5acdbe.png)
### Solution :
![s10065410192024](https://a.okmd.dev/md/671384c02d529.png)
```
chown hacker /flag
```
This turns the user hacker into the owner of the file flag.
```
ls -l /flag
```
This shows us the access permissions of the file flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{0ULfKrMc6k8WMzuw9Fc2WQnVJZg.dFTM2QDL4IDO0czW}
```

## 2. Groups and Files
### Problem :
![s10070510192024](https://a.okmd.dev/md/671384cb5595a.png)
![s10071610192024](https://a.okmd.dev/md/671384d6ab107.png)
![s10072610192024](https://a.okmd.dev/md/671384dfc0478.png)
### Solution :
![s10073810192024](https://a.okmd.dev/md/671384eb5cca8.png)
```
chgrp hacker /flag
```
This turns the group hacker into the owner of the file flag.
```
ls -l /flag
```
This shows us the access permissions of the file flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{ISMqecrnbLLLWdwpI8Zlku5W5rF.dFzNyUDL4IDO0czW}
```

## 3. Fun with Group Names
### Problem :
![s10074710192024](https://a.okmd.dev/md/671384f583a2c.png)
### Solution :
![s10075510192024](https://a.okmd.dev/md/671384fd5d074.png)
```
id
```
We find the name of the group our user is part of.
```
chgrp grp18355 /flag
```
This grants access of the flag to the grp18355 group and our user is part of this group.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{AWr34PADkBam92h_IQDKuhYKepu.dJzNyUDL4IDO0czW}
```

## 4. Changing Permissions
### Problem :
![s10080510192024](https://a.okmd.dev/md/671385077291e.png)
![s10081410192024](https://a.okmd.dev/md/671385105943a.png)
![s10082510192024](https://a.okmd.dev/md/6713851b9f3c7.png)
![s10083410192024](https://a.okmd.dev/md/6713852386e2f.png)
### Solution :
![s10084310192024](https://a.okmd.dev/md/6713852d63682.png)
```
ls -l /flag
```
This shows us the access permissions of the file flag.
```
chmod o+r /flag
```
We change the permission for other users (like us) to be able to read the flag.
```
ls -l /flag
```
This shows us the updated access permissions of the file flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{AOTCEjOYGYoVCBG00sRj4IrGqCa.dNzNyUDL4IDO0czW}
```

## 5. Executable Files
### Problem :
![s10085310192024](https://a.okmd.dev/md/6713853795136.png)
### Solution :
![s10090110192024](https://a.okmd.dev/md/6713853f79038.png)
```
ls -l /challenge/run
```
This shows us the access permissions of the file.
```
chmod a+x /challenge/run
```
We change the permission for all users (including us) to be able to execute the file.
```
ls -l /challenge/run
```
This shows us the updated access permissions of the file.
```
/challenge/run
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{cIIVxNas4haF7HX5pfK8iCoDKA9.dJTM2QDL4IDO0czW}
```

## 6. Permission Tweaking Practice
### Problem :
![s10091410192024](https://a.okmd.dev/md/6713854c3ff83.png)
### Solution :
![s10092210192024](https://a.okmd.dev/md/6713855465eec.png)
![s10094610192024](https://a.okmd.dev/md/6713856cdbd06.png)
![s10095610192024](https://a.okmd.dev/md/671385765a1eb.png)
![s10100610192024](https://a.okmd.dev/md/671385805f898.png)
![s10101710192024](https://a.okmd.dev/md/6713858a821f9.png)
![s10102410192024](https://a.okmd.dev/md/67138592747ee.png)
We keep following the instructions provided at every round and changing the permissions accordingly.
Once all rounds have been successfully cleared, we get the flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{4KZif2wvd8OGj4QaGvS8GfR7dVS.dBTM2QDL4IDO8czW}
```

## 7. Permission Setting Practice
### Problem :
![s10104210192024](https://a.okmd.dev/md/671385a54925c.png)
### Solution :
![s10105110192024](https://a.okmd.dev/md/671385ada3a0d.png)
![s10105910192024](https://a.okmd.dev/md/671385b53be73.png)
![s10110910192024](https://a.okmd.dev/md/671385bf8113d.png)
![s10111910192024](https://a.okmd.dev/md/671385c921552.png)
![s10112810192024](https://a.okmd.dev/md/671385d23e84d.png)
![s10113810192024](https://a.okmd.dev/md/671385dc40e5c.png)
We keep following the instructions provided at every round and changing the permissions accordingly.
Once all rounds have been successfully cleared, we get the flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{ED6h8wNKM2I175PYZAm_7Y_fRD2.dNTM5QDL4IDO0czW}
```

## 8. The SUID Bit
### Problem :
![s10114710192024](https://a.okmd.dev/md/671385e5e7f9b.png)
### Solution :
![s10115610192024](https://a.okmd.dev/md/671385ee874de.png)
```
ls -l /challenge/getroot
```
This shows us the access permissions of the file.
```
chmod a+s /challenge/getroot
```
We change the permission for all users (including us) to be able to execute the file.
```
/challenge/getroot
```
This sets the SUID bit for the program and let us run it as root.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{EJKb2ZwYvcV4uUioIZk_bmPOsDi.dNTM2QDL4IDO0czW}
```
