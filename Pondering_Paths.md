# Pondering Paths
## 1. The Root
### Problem :
![problem 1](https://media.discordapp.net/attachments/858349899401658398/1292958918661636199/image.png?ex=6705a154&is=67044fd4&hm=290a4424caff9abf97e20d68482d4d92ae198ce93bd4588afa73852f9b797fc4&=&format=webp&quality=lossless&width=1440&height=322)

### Solution :
```
/pwn
```
This directly gives the flag as pwn is a program which is directly navigated to from the root directory by using /pwn.
### Flag for the challenge :
```
BOOM!!!
Here is your flag:
pwn.college{IvvLGr0OlGWmbJCGMyUwgflohgr.dhzN5QDL4IDO0czW}
```

## 2. Program and Absolute Paths
### Problem :
![problem 2](https://media.discordapp.net/attachments/858349899401658398/1292959519147687936/image.png?ex=6705a1e3&is=67045063&hm=793703d07d587b74bdfd936c590a98ec4a92eb753bf0fcb9600539c3b4b833d5&=&format=webp&quality=lossless&width=1440&height=256)

### Solution :
```
/challenge/run
```
This directly gives the flag as challenge is a directory in the root which contains a program run. We go to challenge from root using /challenge and we access run file using the /run.
### Flag for the challenge :
```
Correct!!!
/challenge//run is an absolute path! Here is your flag:
pwn.college{43Z3Vaefdwgmosxx_49g8OO9Ez6.dVDN1QDL4IDO0czW}
```

## 3. Position Thy Self
### Problem :
![problem 3](https://media.discordapp.net/attachments/858349899401658398/1292960414602104975/image.png?ex=6705a2b8&is=67045138&hm=a50b870761c14c7f53576e8f8959d7e7aefb739055ca27f461cea92e81faba12&=&format=webp&quality=lossless&width=1440&height=407)

### Solution :
```
/challenge/run
```
This shows us the path where we need to navigate to in order to run the run program in challenge directory.
```
cd /proc/67
```
We change the directory to the path we were just given.
```
/challenge/run
```
This gives us the flag as we run this from the correct path as provided.
### Flag for the challenge :
```
Correct!!!
/challenge/run is an absolute path, invoked from the right directory!
Here is your flag:
pwn.college{4C7e36t4Ar4gSlkyuN0eFWsUWnc.dZDN1QDL4IDO0czW}
```

## 4. Position Elsewhere
### Problem :
![problem 4](https://media.discordapp.net/attachments/858349899401658398/1292960414602104975/image.png?ex=6705a2b8&is=67045138&hm=a50b870761c14c7f53576e8f8959d7e7aefb739055ca27f461cea92e81faba12&=&format=webp&quality=lossless&width=1440&height=407)

### Solution :
```
/challenge/run
```
This shows us the path where we need to navigate to in order to run the run program in challenge directory.
```
cd /usr/share/build-essential
```
We change the directory to the path we were just given.
```
/challenge/run
```
This gives us the flag as we run this from the correct path as provided.
### Flag for the challenge :
```
Correct!!!
/challenge/run is an absolute path, invoked from the right directory!
Here is your flag:
pwn.college{A1pCWxRszDncIN-I8qBc2Fckjzz.ddDN1QDL4IDO0czW}
```

## 5. Position Yet Elsewhere
### Problem :
![problem 5](https://media.discordapp.net/attachments/858349899401658398/1292962410302541924/image.png?ex=6705a494&is=67045314&hm=1735214c03a02a4a1a48e0e761dfc5382fa78b3cd10d44ab0fed3caea5d4e090&=&format=webp&quality=lossless&width=1440&height=397)

### Solution :
```
/challenge/run
```
This shows us the path where we need to navigate to in order to run the run program in challenge directory.
```
cd /usr/share/zoneinfo/posix/Asia
```
We change the directory to the path we were just given.
```
/challenge/run
```
This gives us the flag as we run this from the correct path as provided.
### Flag for the challenge :
```
Correct!!!
/challenge/run is an absolute path, invoked from the right directory!
Here is your flag:
pwn.college{IFwRw9cdfUuSUni_DQ1A3YakusP.dhDN1QDL4IDO0czW}
```

## 6. Implicit Relative Paths, From /
### Problem :
![problem 6](https://media.discordapp.net/attachments/858349899401658398/1292963738676105297/image.png?ex=6705a5d1&is=67045451&hm=20eaf0cf581a5a97d4d5615b4556430322e313ed2b180a1efd77e2d5b0a87edd&=&format=webp&quality=lossless&width=1431&height=593)

### Solution :
```
/challenge/run
```
This shows us the path where we need to navigate to in order to run the run program in challenge directory.
```
cd /
```
We change the directory to the path we were just given (root directory).
```
challenge/run
```
This gives us the flag as we run this from the correct path (relative path) as provided.
### Flag for the challenge :
```
Correct!!!
challenge/run is a relative path, invoked from the right directory!
Here is your flag:
pwn.college{0MiYdNQ9ajxh8pfn63aAABUXMRL.dlDN1QDL4IDO0czW}
```

## 7. Explicit Relative Paths, From /
### Problem :
![problem 7](https://media.discordapp.net/attachments/858349899401658398/1292964681388130436/image.png?ex=6705a6b2&is=67045532&hm=609bb1599d209364b9d0ad07856a599a259250f490c572a36d2d173d5b08376c&=&format=webp&quality=lossless&width=1238&height=592)
### Solution :
```
/challenge/run
```
This shows us the path where we need to navigate to in order to run the run program in challenge directory.
```
cd /
```
We change the directory to the path we were just given (root directory).
```
./challenge/run
```
This gives us the flag as we run this from the correct path (relative path) as provided.
### Flag for the challenge :
```
Correct!!!
./challenge/run is a relative path, invoked from the right directory!
Here is your flag:
pwn.college{0hl9neOOxHDzBrO6AMXA-n3CRwo.dBTN1QDL4IDO0czW}
```

## 8. Implicit Relative Paths
### Problem :
![problem 8](https://media.discordapp.net/attachments/858349899401658398/1292965437457563668/image.png?ex=6705a766&is=670455e6&hm=d32edf36d47c97ad353b4b528bb71e105520bf02445d622c12ba027babee0563&=&format=webp&quality=lossless&width=687&height=283)

### Solution :
```
cd /challenge
```
We change the directory to the challenge directory as instructed
```
./run
```
This gives us the flag as we run this from the challenge directory by using "./run" so as to search for the run program in the current working directory.
### Flag for the challenge :
```
Correct!!!
./run is a relative path, invoked from the right directory!
Here is your flag:
pwn.college{YtFDaY-LXA52g8A5eSrOA5BhHkG.dFTN1QDL4IDO0czW}
```

## 9. Home Sweet Home
### Problem :
![problem 9_a](https://media.discordapp.net/attachments/858349899401658398/1292966362934935552/image.png?ex=6705a843&is=670456c3&hm=0574135545814aca0d36bd78b21e46675260b1d0a358139198ab59487619a159&=&format=webp&quality=lossless&width=1221&height=593)
![problem 9_b](https://media.discordapp.net/attachments/858349899401658398/1292966690904215593/image.png?ex=6705a891&is=67045711&hm=d7e3d300a83db26560422b4160c380e11844f3ebb5f4da0b11c10dcc17c9b578&=&format=webp&quality=lossless&width=1440&height=456)
### Solution :
```
cd /home/hacker/
```
This takes us to the hacker directory in home.
```
ls
```
We check the contents in the directory where we find a file named "a" to which we can append our flag
```
/challenge/run ~/a
```
This gives us the flag as we run /challenge/run with an arguement with less than equal to 3 characters using ~ to signify our current working directory/
### Flag for the challenge :
```
Correct!!!
Writing the file to /home/hacker/a!
... and reading it back to you:
pwn.college{Eg4L2EJgTlUi9z4PvemV2ckfC6A.dNzM4QDL4IDO0czW}
```
