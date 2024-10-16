# File Globbing
## 1. Matching with *
### Problem :
![s18275810162024](https://a.okmd.dev/md/670fb85924808.png)
![s18281410162024](https://a.okmd.dev/md/670fb86977a5d.png)
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
![s18283010162024](https://a.okmd.dev/md/670fb87903d0c.png)
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
![s18325910162024](https://a.okmd.dev/md/670fb985eeffa.png)
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
![s18314110162024](https://a.okmd.dev/md/670fb937ac0d0.png)
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
![s18311510162024](https://a.okmd.dev/md/670fb91e0084b.png)
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
![s18304510162024](https://a.okmd.dev/md/670fb900c6c87.png)
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
