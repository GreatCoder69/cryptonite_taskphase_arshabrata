# Digesting Documentation
## 1. Learning from Documentation
### Problem :
![problem 1](https://media.discordapp.net/attachments/858349899401658398/1293147610227671080/image.png?ex=6706510f&is=6704ff8f&hm=ba10ca3ba2deaad86c0480e1aa1d5f5ae13c387157d6fb9f5a0c4d8e3ecaa2a3&=&format=webp&quality=lossless&width=1440&height=538)
### Solution :
```
/challenge/challenge --giveflag 
```
We access the challenge file in challenge directory by passing --giveflag as an argument. This gives us the flag.
### Flag for the challenge :
```
Correct argument! Here is your flag:
pwn.college{g2fHW-xXTAeDhrLjAfN9i8Wm4Ea.dRjM5QDL4IDO0czW}
```

## 2. Learning Complex Usage
### Problem :
![problem 2](https://media.discordapp.net/attachments/858349899401658398/1293149091903045704/image.png?ex=67065271&is=670500f1&hm=60cd07a46d1476ae6b18cb367d7687d9e76088dfcd993ba03f9611a08b4f504e&=&format=webp&quality=lossless&width=1440&height=517)
### Solution :
```
ls /
```
We search the root directory to look for the flag file and we find it here itself.
```
/challenge/challenge --printfile /flag
```
We run the /challenge/challenge command with --printfile as an argument and the /flag file acts as an argument for the --printfile.  
According to the documentation, this lets us access the file and hence we obtain the flag.
### Flag for the challenge :
```
Correct argument! Here is the /flag file:
pwn.college{MAJyeArR4g_FfhyOfE6pjnMetLL.dVjM5QDL4IDO0czW}
```

## 3. Reading Manuals
### Problem :
![problem 3a](https://media.discordapp.net/attachments/858349899401658398/1293156001234550877/image.png?ex=670658e0&is=67050760&hm=77c5e36e40c5893d98fb7096c8f4cfc2695b624ad3fa873b6005be4406a1c034&=&format=webp&quality=lossless&width=687&height=378)
![problem 3b](https://media.discordapp.net/attachments/858349899401658398/1293156094461345833/image.png?ex=670658f6&is=67050776&hm=81a1ff54d440a2bdc8d9330c5ca05f214817a295d47db7cc90929f963cd57ca3&=&format=webp&quality=lossless&width=868&height=593)
![problem 3c](https://media.discordapp.net/attachments/858349899401658398/1293156165198286848/image.png?ex=67065907&is=67050787&hm=38dc7173cc063f6c6a0f9bb406d5f4b28f22d6880d91d87428be4b709869d20c&=&format=webp&quality=lossless&width=1042&height=593)
### Solution :
```
man challenge
```
We open the manual for the challenge and read it in order to find the command and argument to get the flag.  
We read that : /challenge/challenge --eivxhv NUM : print the flag if NUM is 491
```
/challenge/challenge  --eivxhv 491
```
This gives us the flag.
### Flag for the challenge :
```
Correct usage! Your flag: pwn.college{4E911FEeiv0-x9T-hvnxpy-0z6O.dRTM4QDL4IDO0czW}
```

## 4. Searching Manuals
### Problem :
![problem 4](https://media.discordapp.net/attachments/858349899401658398/1293157170233212959/image.png?ex=670659f7&is=67050877&hm=6ef65c5647d20c05e3898badd712cf1b7ce20840ecee41b6fc7e2b04dc9ad0ea&=&format=webp&quality=lossless&width=1440&height=127)
### Solution :
```
man challenge
```
We open the manual for the challenge and read it in order to find the command and argument to get the flag.  
We search the manual by writing /flag and using n to go to the next search result.  
We read that : /challenge/challenge  --aktvd : This argument will give you the flag!
```
/challenge/challenge --aktvd
```
This gives us the flag
### Flag for the challenge :
```
Initializing...
Correct usage! Your flag: pwn.college{Qv8VbUYY4e6rBecnvMdjx8vRXXr.dVTM4QDL4IDO0czW}
```

## 5. Searching For Manuals
### Problem :
![problem 5](https://media.discordapp.net/attachments/858349899401658398/1293159659858956288/image.png?ex=67065c48&is=67050ac8&hm=4f59ee48b04ef803ef6025d64463c722c10e69bbf50fef1121bdc47e1d9ef032&=&format=webp&quality=lossless&width=1440&height=313)
### Solution :
```
man man
```
We open the manual for the man command and read it in order to find the command and argument to get the flag.  
We search the manual by writing /flag and using n to go to the next search result.  
We read that : man -k printf : Search the short descriptions and manual page names for the keyword printf as regular expression. Print out any matches. Equivalent to apropos printf.
```
man -k challenge
```
We see that ugqxzdxpxu (1) - print the flag!
```
man ugqxzdxpxu
```
We view the manual where we see that /challenge/challenge  --ugqxzd : print the flag if NUM is 882
```
/challenge/challenge  --ugqxzd 882
``` 
This gives us the flag.
### Flag for the challenge :
```
Correct usage! Your flag: pwn.college{8ugqxJzYdO8ExpDxu2NwWO5DkvH.dZTM4QDL4IDO0czW}
```

## 6. Helpful Programs
### Problem :
![problem 6](https://media.discordapp.net/attachments/858349899401658398/1293161647011004437/image.png?ex=67065e22&is=67050ca2&hm=54ca73ef743fe70403863c36e2b11d563205ed29309fc9972af83aaf7b0cfdbb&=&format=webp&quality=lossless&width=1440&height=167)
### Solution :
```
/challenge/challenge --h
```
This gives us steps to get the flag by using --h.
We see that:  
-g GIVE_THE_FLAG, --give-the-flag GIVE_THE_FLAG : get the flag, if given the correct value  
-p, --print-value : print the value that will cause the -g option to give you the flag
```
/challenge/challenge -p
```
We get the secret value which is 956.
```
/challenge/challenge -g 956
```
This gives us the flag.
### Flag for the challenge :
```
Correct usage! Your flag: pwn.college{cZhX9n5Byup_uLQ6VFLZJ4bWEg6.ddjM4QDL4IDO0czW}
```

## 7. Helpful for Builtins
### Problem :
![problem 7](https://media.discordapp.net/attachments/858349899401658398/1293163176442990633/image.png?ex=67065f8f&is=67050e0f&hm=f726bf39328becabd12a18e1d54b1624c5229b460c65ae02ab2e2bd10583866d&=&format=webp&quality=lossless&width=1360&height=593)
### Solution :
```
help challenge
```
Since challenge is a builtin command in this case, we use help to know about its usage.  
We can see that :  
--secret VALUE : prints the flag, if VALUE is correct  
You must be sure to provide the right value to --secret. That value is "E4NLXtpt".
```
challenge --secret E4NLXtpt
```
This gives us the flag.
### Flag for the challenge :
```
Correct! Here is your flag!
pwn.college{E4NLXtptYGx5a2I5TJIntXLVzuD.dRTM5QDL4IDO0czW}
```



