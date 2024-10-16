# Pondering Paths
## 1. The Root
### Problem :
![s17592210162024](https://a.okmd.dev/md/670fb1a502ae2.png)

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
![s17594110162024](https://a.okmd.dev/md/670fb1b8902d7.png)

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
![s18002310162024](https://a.okmd.dev/md/670fb1e2aec93.png)

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
![s18004210162024](https://a.okmd.dev/md/670fb1f55cc5f.png)

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
![s18011510162024](https://a.okmd.dev/md/670fb2167b1fb.png)

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
![s18013310162024](https://a.okmd.dev/md/670fb2284cbfc.png)

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
![s18015110162024](https://a.okmd.dev/md/670fb23a97421.png)
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
![s18021010162024](https://a.okmd.dev/md/670fb24d35f63.png)

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
![s18023110162024](https://a.okmd.dev/md/670fb262538ce.png)
![s18024510162024](https://a.okmd.dev/md/670fb27071e80.png)
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
