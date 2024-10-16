# Shell Variables
Before we start executing commands to get the flag, we have to connect to the server using our SSH key.
The command is as follows :
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Printing Variables
### Problem :
![s22225810162024](https://a.okmd.dev/md/670fef6fedbf7.png)
### Solution :
![s22232110162024](https://a.okmd.dev/md/670fef8424b6f.png)
```
echo $FLAG
```
The value of flag is stored in the variable FLAG.
We get the flag by printing the value of FLAG using $ and echo.
### Flag for the challenge :
```
pwn.college{0Gro5dhUKvSEZiubCzG6kNN69Zo.ddTN1QDL4IDO0czW}
```

## 2. Setting Variables
### Problem :
![s22234510162024](https://a.okmd.dev/md/670fef9e27bee.png)
### Solution :
![s22235610162024](https://a.okmd.dev/md/670fefa781a5c.png)
```
PWN=COLLEGE
```
We store the value COLLEGE in PWN using =. This gives us the flag.
### Flag for the challenge :
```
pwn.college{k0oPFkoOcwDrlbbHru5GCGNHxaQ.dlTN1QDL4IDO0czW}
```

## 3. Multi-word Variables
### Problem :
![s22242410162024](https://a.okmd.dev/md/670fefc4e57a3.png)
### Solution :
![s22244110162024](https://a.okmd.dev/md/670fefd51eb1e.png)
```
PWN="COLLEGE YEAH"
```
We store the multi-word variable using "". This gives us the flag.
### Flag for the challenge :
```
pwn.college{Me-TRr1UZu0Iockqk7MnHU6-Sg5.dBjN1QDL4IDO0czW}
```

## 4. Exporting Variables
### Problem :
![s22252610162024](https://a.okmd.dev/md/670ff00337c40.png)
![s22253810162024](https://a.okmd.dev/md/670ff00ea8b7b.png)
### Solution :
![s22254710162024](https://a.okmd.dev/md/670ff0171aa33.png)
```
export PWN=COLLEGE
```
We store COLLEGE in the variable and PWN and export it to the new shell.
```
COLLEGE=PWN
```
We store PWN in the variable COLLEGE but do not export it to the new shell.
```
sh
```
This opens up a new shell.
```
/challenge/run $PWN
```
We pass the value of PWN (which we exported) as argument of /challenge/run which gives us the flag.
### Flag for the challenge :
```
pwn.college{s7dK4RRy6IiH-dWi5afKqJszUOk.dJjN1QDL4IDO0czW}
```

## 5. Printing Exported Variables
### Problem :
![s22260110162024](https://a.okmd.dev/md/670ff02580957.png)
### Solution :
![s22263310162024](https://a.okmd.dev/md/670ff044bb127.png)
```
env | grep pwn.college
```
We pipe the output of grep which gives all exported values in the shell into the grep command with pwn.college to obtain the flag.
### Flag for the challenge :
```
pwn.college{MWQUeJoGSXtNp1PsOnRqNa2zgPe.dhTN1QDL4IDO0czW}
```

## 6. Storing Command Output
### Problem :
![s22265410162024](https://a.okmd.dev/md/670ff05a32ab6.png)
### Solution :
![s22270410162024](https://a.okmd.dev/md/670ff063ee1f8.png)
```
PWN=$(/challenge/run)
```
This reads the output of /challenge/run into the variable PWN.
```
echo $PWN
```
This prints out the flag to our terminal.
### Flag for the challenge :
```
pwn.college{oiLfE2WBpK3AaL1Tl7Ra6G0coye.dVzN0UDL4IDO0czW}
```

## 7. Reading Input
### Problem :
![s22272210162024](https://a.okmd.dev/md/670ff076bc339.png)
### Solution :
![s22273610162024](https://a.okmd.dev/md/670ff08366e3f.png)
```
read -p "input : " PWN
```
This gives a prompt "input : " and then takes input from user. In this case we enter COLLEGE.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{cDzZm-mUg8zKy4pBwNdVg3m-6Kq.dhzN1QDL4IDO0czW}
```

## 8. Reading Files
### Problem :
![s22281610162024](https://a.okmd.dev/md/670ff0ad2a5b4.png)
### Solution :
![s22283010162024](https://a.okmd.dev/md/670ff0b96d108.png)
```
read PWN < /challenge/read_me
```
We read the output of /challenge/read_me directly into the variable PWN using < to redirect.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{4t8CZtFPFrw40g7furU83yRAtaD.dBjM4QDL4IDO0czW}
```
