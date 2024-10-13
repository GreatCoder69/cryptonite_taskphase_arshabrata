# Untangling Users
Before we start executing commands to get the flag, we have to connect to the server using our SSH key. 
The command is as follows : 
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Becoming Root with su
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295108362295447674/image.png?ex=670d7327&is=670c21a7&hm=05cf923ca497c56992dedfd29bec04e3d0301f86e71b8d2d2360258377fc7c08&=&format=webp&quality=lossless&width=1007&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295108477215047770/image.png?ex=670d7342&is=670c21c2&hm=a1fcd632074a03dec93cc26271032c0b313bfc4f15abbf190b2a734c49800e7d&=&format=webp&quality=lossless&width=1175&height=592)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295109178834292837/image.png?ex=670d73ea&is=670c226a&hm=2fb94662f3c12d1d7822476905680218a8caeb3348aecfc763b3c6287aa3750e&=&format=webp&quality=lossless&width=1440&height=285)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295109804548952146/image.png?ex=670d747f&is=670c22ff&hm=843a371f835b4f0ba97fe23201339d918f34fe0302ca96f11493bbf133492bc8&=&format=webp&quality=lossless&width=1312&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295110333723049995/image.png?ex=670d74fd&is=670c237d&hm=16d1628f41eabaa4e085532a9fcef0e1155a54402881cd00566e49e9c9a82df1&=&format=webp&quality=lossless&width=957&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295110449070870611/image.png?ex=670d7519&is=670c2399&hm=71286cbea273e45535566e5039afd388c59bc75d500073c127bfc6a0156ecd0c&=&format=webp&quality=lossless&width=903&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295110988072484996/image.png?ex=670d7599&is=670c2419&hm=d1211d6f667b673998b321bd6ae9b6515f66524282b10fd5416c9d6860afdeb9&=&format=webp&quality=lossless&width=1172&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295112050292297848/image.png?ex=670d7696&is=670c2516&hm=e778ae241f96581e8b74554dfe97b386190d99591ec44f3b166acb87c238db87&=&format=webp&quality=lossless&width=1343&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295112118429028403/image.png?ex=670d76a7&is=670c2527&hm=0a8eeed9fd0495b59aba769d60a2de08beed695dc9cfeb4871de223581f291fa&=&format=webp&quality=lossless&width=1440&height=386)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295113520417083402/image.png?ex=670d77f5&is=670c2675&hm=bc655bbdb7b214f4b04da951f0cb07ceea0351dda3c5a01bcb6de73c042f076b&=&format=webp&quality=lossless&width=1178&height=592)
```
sudo cat /flag
```
We use sudo to get root access and then read the file flag which gives us the flag.
### Flag for the challenge : 
```
pwn.college{0H_c_uQ2WVKIIRLZ4UpYqCkj7v-.dhTN0UDL4IDO0czW}
```
