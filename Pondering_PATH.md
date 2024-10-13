# Pondering PATH
Before we start executing commands to get the flag, we have to connect to the server using our SSH key. 
The command is as follows : 
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. The PATH Variable
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295125113179607121/image.png?ex=670d82c1&is=670c3141&hm=ea6a986e7c5bf3f9d210a4a7beb4d91a9b6faa0ac993fd6a5bc474dedf50d655&=&format=webp&quality=lossless&width=1336&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295125339957104660/image.png?ex=670d82f7&is=670c3177&hm=5e463ae38970e247fa9d97119da2e422c53c975677b6ad9b5a8eaf3e2375b643&=&format=webp&quality=lossless&width=1175&height=590)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295125903390539927/image.png?ex=670d837d&is=670c31fd&hm=fc15b4e9bd72b41e50685a3e8a334ac73b3c54083c369ca07fef952c74e959e9&=&format=webp&quality=lossless&width=1083&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295126061884903566/image.png?ex=670d83a3&is=670c3223&hm=0bbc0e678a472dbf4cbf3e8b5b2c0d035185277d2d1251b7ede7e6580654b6b9&=&format=webp&quality=lossless&width=1162&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295126674983358464/image.png?ex=670d8435&is=670c32b5&hm=ab905a764b3bebf60f48a122c7e800bc07cf9f7c5101c18d85bf67b8580fcf96&=&format=webp&quality=lossless&width=993&height=592)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295127488070160434/image.png?ex=670d84f7&is=670c3377&hm=67998dcc52b1ab4826ca19e480a51b68d6c8ee834e58a13c6c5617516926db6c&=&format=webp&quality=lossless&width=1175&height=592)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295129585977131048/image.png?ex=670d86eb&is=670c356b&hm=2fec19be334bc22b15a784088ba80f23169afbec81bc84f911ea1ceab2af7c21&=&format=webp&quality=lossless&width=1440&height=201)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295130659181957230/image.png?ex=670d87eb&is=670c366b&hm=9f8beeef69ad7f44769c6fc31f527dc60aef7a8bded96db5cad6b11957544b4c&=&format=webp&quality=lossless&width=1177&height=593)
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


