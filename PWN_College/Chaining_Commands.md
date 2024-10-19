# Chaining Commands
Before we start executing commands to get the flag, we have to connect to the server using our SSH key.
The command is as follows :
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Chaining with Semicolons
### Problem :
![s15530910192024](https://a.okmd.dev/md/6713888f12f53.png)
### Solution :
![s15531910192024](https://a.okmd.dev/md/6713889899dd7.png)
```
/challenge/pwn ; /challenge/college
```
We use semicolon to chain these two commands.
/challenge/college is executed as soon as /challenge/pwn completes execution.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{IfEWY6nBCTvdqtH9fpBv3KlCSFf.dVTN4QDL4IDO0czW}
```

## 2. Your First Shell Script
### Problem :
![s15532910192024](https://a.okmd.dev/md/671388a30cfa1.png)
### Solution :
![s15533810192024](https://a.okmd.dev/md/671388ab79b7a.png)
```
touch x.sh
```
We create a shell script named "x".
```
nano x.sh
```
We write the commands one after the other in the shell script :
/challenge/pwn
/challenge/college
```
cat x.sh
```
We read the contents of our shell script.
```
bash x.sh
```
We run our shell script using bash. This gives us the flag.
### Flag for the challenge :
```
pwn.college{IfEWY6nBCTvdqtH9fpBv3KlCSFf.dVTN4QDL4IDO0czW}
```

## 3. Redirecting Script Output
### Problem :
![s15535010192024](https://a.okmd.dev/md/671388b8590ff.png)
### Solution :
![s15535810192024](https://a.okmd.dev/md/671388c04c6d7.png)
```
cat x.sh
```
We read the contents of our shell script. We have already added contents to this shell script in the last challenge.
```
bash x.sh | /challenge/solve
```
We run the shell script using bash and pipe the output into /challenge/solve using |.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{MdPjJwtQXwiPGgrRhIJybmQTtAW.dhTM5QDL4IDO0czW}
```

## 4. Executable Shell Scripts
### Problem :
![s15540810192024](https://a.okmd.dev/md/671388ca47a42.png)
### Solution :
![s15545910192024](https://a.okmd.dev/md/671388fd5f669.png)
```
nano x.sh
```
We write the following inside our shell script:
/challenge/solve
```
cat x.sh
```
We read our shell script.
```
chmod a+x x.sh
```
We edit the permissions of our shell script to make it executable for everyone.
```
./x.sh
```
We run the shell script as an executable file.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{kQUOh3RnUiUxN7mh9ojk0K7MM8K.dRzNyUDL4IDO0czW}
```
