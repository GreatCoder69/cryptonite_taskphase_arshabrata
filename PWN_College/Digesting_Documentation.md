# Digesting Documentation
## 1. Learning from Documentation
### Problem :
![s18221010162024](https://a.okmd.dev/md/670fb6fe04fc2.png)
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
![s18223710162024](https://a.okmd.dev/md/670fb7181adba.png)
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
![s18225110162024](https://a.okmd.dev/md/670fb725daa18.png)
![s18230410162024](https://a.okmd.dev/md/670fb73381530.png)
![s18232010162024](https://a.okmd.dev/md/670fb743dcc5a.png)
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
![s18233710162024](https://a.okmd.dev/md/670fb7537e4de.png)
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
![s18235310162024](https://a.okmd.dev/md/670fb764173cc.png)
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
![s18241010162024](https://a.okmd.dev/md/670fb774caf6d.png)
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
![s18244410162024](https://a.okmd.dev/md/670fb79774194.png)
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
