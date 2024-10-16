# Comprehending Commands
## 1. Cat: Not the Pet, but the Command!
### Problem :
![s18110210162024](https://a.okmd.dev/md/670fb461c7688.png)

### Solution :
```
cat /flag
```
This directly gives the flag as we read the flag written in the flag file in the root directory using cat
### Flag for the challenge :
```
pwn.college{ERLC91ChwnsmvrsYGazM5UTZlwH.dFzN1QDL4IDO0czW}
```

## 2. Catting Absolute Paths
### Problem :
![s18114110162024](https://a.okmd.dev/md/670fb48861e05.png)

### Solution :
```
cat /flag
```
This directly gives the flag as we read the flag written in the flag file in the root directory using cat
### Flag for the challenge :
```
pwn.college{wZmilrpYWv-UQmFvMgSXuURFfnQ.dlTM5QDL4IDO0czW}
```

## 3. More Catting Practice
### Problem :
![s18123910162024](https://a.okmd.dev/md/670fb4c17c7ea.png)

### Solution :
```
cat /usr/share/fish/flag
```
This gives the flag as we read cat the flag file using the absolute path (provided at launch of challenge) without using cd.
### Flag for the challenge :
```
pwn.college{4NUZVfzhrJTmCC1CjebE7ebvc0v.dBjM5QDL4IDO0czW}
```

## 4. Grepping for a Needle in a Haystack
### Problem :
![s18131210162024](https://a.okmd.dev/md/670fb4e3901ff.png)

### Solution :
```
grep pwn.college /challenge/data.txt
```
We use grep to look for a sequence beginning with pwn.college which is the start of every flaf in a data.txt file placed in a challenge directory.
### Flag for the challenge :
```
pwn.college{EcViYf4rBaYMRgTZ-FNjQ_FYYNl.ddTM4QDL4IDO0czW}
```

## 5. Listing Files
### Problem :
![s18133910162024](https://a.okmd.dev/md/670fb4fdd986b.png)

### Solution :
```
cd /challenge
```
We use cd to navigate to the challenge directory.
```
ls
```
We use ls to see all the files in the directory. Here we find the renamed flag file.
```
./3881-renamed-run-31846
```
We run the renamed file in challenge to get the flag.
### Flag for the challenge :
```
Yahaha, you found me! Here is your flag:
pwn.college{My804whfcDKqHpMDBISgTBAuIjT.dhjM4QDL4IDO0czW}
```

## 6. Touching Files
### Problem :
![s18141610162024](https://a.okmd.dev/md/670fb52222339.png)
### Solution :
```
touch /tmp/pwn
```
We create a pwn file in the tmp directory using touch.
```
touch /tmp/college
```
We create a college file in the tmp directory using touch.
```
/challenge/run
```
We run the flag file in challenge directory after creating the two files earlier to obtain the flag.
### Flag for the challenge :
```
Yahaha, you found me! Here is your flag:
pwn.college{My804whfcDKqHpMDBISgTBAuIjT.dhjM4QDL4IDO0czW}
```

## 7. Removing Files
### Problem :
![s18143610162024](https://a.okmd.dev/md/670fb5370bbff.png)

### Solution :
```
rm delete_me
```
Deletes the file to be deleted using rm.
```
/challenge/check
```
Checks if the file has been deleted and gives us the flag if successfully deleted.
### Flag for the challenge :
```
Excellent removal. Here is your reward:
pwn.college{kKmv2pkNiW0cw13uyoyhPdApvfo.dZTOwUDL4IDO0czW}
```

## 8. Hidden Files
### Problem :
![s18145110162024](https://a.okmd.dev/md/670fb545a6719.png)

### Solution :
```
/challenge/run
```
We get the location of the directory where the flag is hidden.
```
cd /
```
We navigate to the root directory using cd.
```
ls -a
```
We see the list of all files, including hidden files, where we find our hidden flag.
```
cat .flag-4375760723586
```
We cat this hidden file to obtain the flag.
### Flag for the challenge :
```
pwn.college{kWCelpptHZlO5AYH-v46DdRkreB.dBTN4QDL4IDO0czW}
```

## 9. An Epic Filesystem Quest
### Problem :
![s18151010162024](https://a.okmd.dev/md/670fb559533f2.png)

### Solution :
```
cd /
```
We go to the root directory as instructed
```
ls
```
We view the contents in the directory which leads us to the file TRACE.
```
cat TRACE
```
We find the location of the next clue in this file.
```
cd  /usr/share/racket/pkgs/db-lib/db/private
```
We change our directory to the path we just obtained.
```
ls -a
```
We search for all files (including hidden) to find the hidden file MESSAGE which contains the next clue.
```
cat .MESSAGE
```
We get the location of the next clue in this file.
```
ls /etc/update-motd.d
```
We check the contents at the location without using cd as instructed. We see the file LEAD-TRAPPED which contains next clue.
```
cat /etc/update-motd.d/LEAD-TRAPPED
```
We obtain the next clue in this file.
```
cd /usr/local/lib/python3.8/dist-packages/numpy/f2py/tests/src/negative_bounds
```
We go to the directory we just got in the clue using cd.
```
ls
```
We view the contents in the directory which leads us to the file CLUE.
```
cat CLUE
```
We find the location of the next clue in this file.
```
cd  /usr/share/racket/pkgs/db-lib/db/private
```
We change our directory to the path we just obtained.
```
ls
```
We search the contents of the directory to find the file NUGGET-TRAPPED.
```
cat NUGGET-TRAPPED
```
We get the location of the next clue in this file.
```
ls /usr/local/lib/python3.8/dist-packages/numpy/_pyinstaller/__pycache__
```
We check the contents at the location without using cd as instructed. We see the file TEASER-TRAPPED which contains next clue.
```
cat /usr/local/lib/python3.8/dist-packages/numpy/_pyinstaller/__pycache__/TEASER-TRAPPED
```
We get the location of the next clue in this file.
```
ls /usr/lib/R/library/graphics/R
```
We check the contents of the directory to find the next clue and find the file SECRET.
```
cat /usr/lib/R/library/graphics/R/SECRET
```
We get the location for the next clue in this file.
```
cd /usr/local/lib/python3.8/dist-packages/pip/_vendor/msgpack/__pycache__
```
We navigate to the obtained directory using cd as instructed.
```
ls
```
We check the contents of the directory and find the file SPOILER.
```
cat SPOILER
```
We get the location of the next clue.
```
cd /opt/linux/linux-5.4/net/ipv6
```
We change directory as instructed.
```
ls -a
```
We check all the files (including hidden) to find the hidden file POINTER.
```
cat .POINTER
```
This gives us the flag.

### Flag for the challenge :
```
CONGRATULATIONS! Your perserverence has paid off, and you have found the flag!
It is: pwn.college{ACEmFq0N1MdemIPQSk7Wm-2hlKH.dljM4QDL4IDO0czW}
```

## 10. Making Directories
### Problem :
![s18161310162024](https://a.okmd.dev/md/670fb598afbbb.png)

### Solution :
```
mkdir /tmp/pwn
```
We create a new directory in the tmp directory using mkdir
```
touch /tmp/pwn/college
```
We create a file named college in the directory we just created.
```
/challenge/run
```
We execute the run file in challenge directory to obtain the flag.
### Flag for the challenge :
```
Success! Here is your flag:
pwn.college{YzJW85fakSiYaYRUt0VmipK1TwP.dFzM4QDL4IDO0czW}
```

## 11. Finding Files
### Problem :
![s18163710162024](https://a.okmd.dev/md/670fb5b080421.png)
![s18165610162024](https://a.okmd.dev/md/670fb5c2c9760.png)

### Solution :
```
find / -name flag
```
We find a file with the name flag starting the search from the root directory.
```
cat /usr/share/racket/pkgs/r5rs-doc/r5rs/compiled/flag
```
We kept on using cat on the files for which we had the permission to access until we got the flag. We get the flag in the third try in the directory mentioned in the command box.
### Flag for the challenge :
```
pwn.college{MAAjN9g13vB0jZHXMOjORIbEzqw.dJzM4QDL4IDO0czW}
```

## 12. Linking Files
### Problem :
![s18172610162024](https://a.okmd.dev/md/670fb5e15c608.png)
![s18174310162024](https://a.okmd.dev/md/670fb5f26fe0e.png)


### Solution :
```
ln -sf /flag /home/hacker/not-the-flag
```
We use ln -s to create a symbolic link between flag and not-the-flag.
We need to do this since /challenge/catflag reads out not-the-flag.
We use -f to force the process since not-the-flag already exists. We remove and replace this file with a symbolic link.
```
/challenge/catflag
```
We obtain the flag for the challenge which we just stored in not-the-flag using the symbolic link.
### Flag for the challenge :
```
About to read out the /home/hacker/not-the-flag file!
pwn.college{or5foLvnyHICLefyg-hE_eQm68e.dlTM1UDL4IDO0czW}
```
