# File Globbing
## 1. Matching with *
### Problem :
![problem 1a](https://media.discordapp.net/attachments/858349899401658398/1293147610227671080/image.png?ex=6706510f&is=6704ff8f&hm=ba10ca3ba2deaad86c0480e1aa1d5f5ae13c387157d6fb9f5a0c4d8e3ecaa2a3&=&format=webp&quality=lossless&width=1440&height=538)
![problem 1b](https://media.discordapp.net/attachments/858349899401658398/1293566638641381429/image.png?ex=6707d74f&is=670685cf&hm=54a49dcd65a9d57c73875356609d5e25f01f03645ebcdba6695085eb46a0ac97&=&format=webp&quality=lossless&width=1418&height=593)
### Solution :
```
cd /c*
```
We change directory to challenge by using c* where * acts as a wildcard and finds all possible matches for directories with any sequence of characters after c.   
We also don't exceed the limit of 4 characters.
```
./r*
```
We use file globbing to match all files beginning with r in the challenge direcory. This gives us the flag.
### Flag for the challenge :
```
You ran me with the working directory of /challenge! Here is your flag:
pwn.college{Q-5_uhAhsL-stJP0gM90PzYEl3M.dFjM4QDL4IDO0czW}
```

## 2. Matching with ?
### Problem :
![problem 2](https://media.discordapp.net/attachments/858349899401658398/1293570097402871818/image.png?ex=6707da88&is=67068908&hm=8cccd7ba94e82fa02db1ac3af6c22670260ce2cb31df742deeb4937c4c2f010f&=&format=webp&quality=lossless&width=1440&height=467)
### Solution :
```
cd /?ha??enge
```
We change directory to challenge by using ?ha??enge where ? acts as a single character wildcard which searches for all possible matches for combinations at the places containing ?.
```
./run
```
We get the flag by checking the run file after using cd to navigate to challenge.
### Flag for the challenge :
```
You ran me with the working directory of /challenge! Here is your flag:
pwn.college{45Z_S9oVajYxk4Si-V1EZrT2zTv.dJjM4QDL4IDO0czW}
```

## 3. Matching with []
### Problem :
![problem 3](https://media.discordapp.net/attachments/858349899401658398/1293570097402871818/image.png?ex=6707da88&is=67068908&hm=8cccd7ba94e82fa02db1ac3af6c22670260ce2cb31df742deeb4937c4c2f010f&=&format=webp&quality=lossless&width=1440&height=467)
### Solution :
```
cd /challenge/files/
```
Navigate to files directory in challenge directory using cd.
```
/challenge/run file_[bash]
```
We use the /challenge/run command using file_[bash] as argument where the [] acts as a form of ?.  
Here the characters inside [] are the only characters which are searched for in the substitution of a single character.
### Flag for the challenge :
```
You got it! Here is your flag!
pwn.college{sqnyw_z1Fll4U7R_xlSwDQKHekl.dNjM4QDL4IDO0czW}
```

## 4. Matching Paths with []
### Problem :
![problem 4](https://media.discordapp.net/attachments/858349899401658398/1293572444451242097/image.png?ex=6707dcb8&is=67068b38&hm=c92daa73a56760c69087661e03acebe976449965099f79cf3a272267ba120a37&=&format=webp&quality=lossless&width=687&height=192)
### Solution :
```
 /challenge/run /challenge/files/file_[bash]
```
We use the /challenge/run command using the absolute path of some files in /challenge/files directory as argument.  
file_[bash] is used where the [] acts as a form of ?.  
Here the characters inside [] are the only characters which are searched for in the substitution of a single character.
### Flag for the challenge :
```
You got it! Here is your flag!
pwn.college{oZ1dNNSG43efqHOc6RAKEdmQwuE.dRjM4QDL4IDO0czW}
```

## 5. Mixing globs
### Problem :
![problem 5](https://media.discordapp.net/attachments/858349899401658398/1293573007318450256/image.png?ex=6707dd3e&is=67068bbe&hm=055364cb4568af1041171ce82d1577cca45d1ceb4baf0666d20c907b62a11226&=&format=webp&quality=lossless&width=1440&height=112)
### Solution :
```
ls /challenge/files/
```
We check the contents of the files directory in challenge.  
We notice a pattern that all files start with different letters. We are only concerned with the files beginning with c,e and p.
```
/challenge/run [cep]*
```
We pass [cep]* as an argument to /challenge/run.  
Here we restrict the first letter of the file to c, e or p using [].  
We use * as a wildcard to autofill the rest of the characters in the filename as and when it finds a match.  
Running this command gives us the flag.
### Flag for the challenge :
```
You got it! Here is your flag!
pwn.college{Ev_VXLfpip9HH5UeckVXIGWU-WW.dVjM4QDL4IDO0czW}
```

## 6. Exclusionary Globbing
### Problem :
![problem 6](https://media.discordapp.net/attachments/858349899401658398/1293574625229406323/image.png?ex=6707dec0&is=67068d40&hm=38d6accdb578c0fdaf4d2063316126eed89546a8034dacf7bc15475a39707baf&=&format=webp&quality=lossless&width=1283&height=593)
### Solution :
```
cd /challenge/files/
```
We change working directory to files directory inside challenge directory.
```
/challenge/run [^pwn]*
```
We pass [^pwn]* as an argument to /challenge/run.  
Here we restrict the first letter of the file to all letters excluding p,w and n using [^].  
We use * as a wildcard to autofill the rest of the characters in the filename as and when it finds a match.  
Running this command gives us the flag.
### Flag for the challenge :
```
You got it! Here is your flag!
pwn.college{gBeiQ4XOG4cjSf-onbxAD_MJCuJ.dZjM4QDL4IDO0czW}
```



