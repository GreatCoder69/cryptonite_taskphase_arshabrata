# Chaining Commands
Before we start executing commands to get the flag, we have to connect to the server using our SSH key. 
The command is as follows : 
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Chaining with Semicolons
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295116514000765019/image.png?ex=670d7abf&is=670c293f&hm=c540ed89e6f045e75071fb38ad857851243e3ac91698a80b1f7a176434bf0beb&=&format=webp&quality=lossless&width=1413&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295117159118278819/image.png?ex=670d7b58&is=670c29d8&hm=621b732c2d568721803537a3af12c375fcba397011e33759c4c4d72e45bd4327&=&format=webp&quality=lossless&width=1175&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295117789647999086/image.png?ex=670d7bef&is=670c2a6f&hm=cf986aa42801bd886a62fda5b6fd60a20128f9917d25c11eb32bf91962eb0be1&=&format=webp&quality=lossless&width=906&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295118865272930314/Screenshot_2024-10-14_014941.png?ex=670d7cef&is=670c2b6f&hm=4c589250581d6d6ee34455ec5a9011b25ff846c492abd8b98919ab4e61523927&=&format=webp&quality=lossless&width=1163&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295119752985055252/image.png?ex=670d7dc3&is=670c2c43&hm=ce1d1501ca85c6945006bf1965ff7a182cfaa27830b3687f88300b98d810b000&=&format=webp&quality=lossless&width=1227&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295120192497651742/image.png?ex=670d7e2c&is=670c2cac&hm=3b75fdb7ff592a6a97ebee16108df73036278d67b51509c09af3f937db61c72c&=&format=webp&quality=lossless&width=1175&height=591)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295120735026544691/image.png?ex=670d7ead&is=670c2d2d&hm=e30b231f6b37e61c7905f0604b817c82bc166ba4fd8cdc0dd7ed0f3d67a30924&=&format=webp&quality=lossless&width=1440&height=412)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295122253263933450/image.png?ex=670d8017&is=670c2e97&hm=7715d809a18a6885a6320f01b447fa1e3b2a600969203ffbef4c451b809a8406&=&format=webp&quality=lossless&width=1177&height=593)
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


