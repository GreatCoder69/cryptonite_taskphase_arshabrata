# Comprehending Commands
## 1. Cat: Not the Pet, but the Command!
### Problem :
![problem 1](https://media.discordapp.net/attachments/858349899401658398/1292974926445412382/image.png?ex=6705b03c&is=67045ebc&hm=e30ca7d17c998784b203e7d1cc5963e16db65a7421204cbedb34f74e7ea0fc57&=&format=webp&quality=lossless&width=1132&height=593)

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
![problem 2](https://media.discordapp.net/attachments/858349899401658398/1292975988871004170/image.png?ex=6705b13a&is=67045fba&hm=083a4e5fab98ea3563481f7c2d2f155ff225d35b85aa6560957d04527c1e2d05&=&format=webp&quality=lossless&width=1440&height=428)

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
![problem 3](https://media.discordapp.net/attachments/858349899401658398/1292976379813433344/image.png?ex=6705b197&is=67046017&hm=b6cd6e82d1e323c0422c4276b9598ab01d0b2a54aa68b88ee827ec4146d66da0&=&format=webp&quality=lossless&width=1440&height=116)

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
![problem 4](https://media.discordapp.net/attachments/858349899401658398/1292982933694713957/image.png?ex=6705b7b1&is=67046631&hm=b5126679af0df878454ef8e4fba768f922b82b958e4d083d7d697111c3bcd147&=&format=webp&quality=lossless&width=1440&height=438)

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
![problem 5](https://media.discordapp.net/attachments/858349899401658398/1292983692691636224/image.png?ex=6705b866&is=670466e6&hm=75ad2607e8721bc1618bed442ec731b830c4845f2613fa2a58f62e76cdc9f933&=&format=webp&quality=lossless&width=1440&height=558)

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
![problem 6](https://media.discordapp.net/attachments/858349899401658398/1292985750995992658/image.png?ex=6705ba51&is=670468d1&hm=804524dad149df4ed74ed6b668a735e8d676ded18750f49d98b3c386a4e87002&=&format=webp&quality=lossless&width=1440&height=388)

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
![problem 7](https://media.discordapp.net/attachments/858349899401658398/1292986043548569620/image.png?ex=6705ba97&is=67046917&hm=dfce5502b0ebac09ff704e6085134ceec19fbb6b5ac0d294546085e16eac592c&=&format=webp&quality=lossless&width=687&height=236)

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
![problem 8](https://media.discordapp.net/attachments/858349899401658398/1292988398776090726/image.png?ex=6705bcc8&is=67046b48&hm=6265b2414e4d2f52d7d4764e934d9a545761a83674887f8a82b20053f540d16b&=&format=webp&quality=lossless&width=1440&height=403)

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
![problem 9](https://media.discordapp.net/attachments/858349899401658398/1293124354086932491/image.png?ex=67063b67&is=6704e9e7&hm=766972f81fa75762e674ac4970f2e51d740a16d261230fae21eca898797a5ac8&=&format=webp&quality=lossless&width=1278&height=593)

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
![problem 10](https://media.discordapp.net/attachments/858349899401658398/1293134605733335050/image.png?ex=670644f3&is=6704f373&hm=b7e6818619092f369029fc5dbe3c07a7e45ef1bbbfaf07891609d3b4813c775b&=&format=webp&quality=lossless&width=1338&height=593)

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
![problem 11a](https://media.discordapp.net/attachments/858349899401658398/1293135869225734175/image.png?ex=67064620&is=6704f4a0&hm=c9789f78f2cebd0b5faf8f23891afab815062b6b2b84c8ec2fb77a23fabe48b3&=&format=webp&quality=lossless&width=1197&height=593)
![problem 11b](https://media.discordapp.net/attachments/858349899401658398/1293136328006963251/image.png?ex=6706468d&is=6704f50d&hm=251a15701368e907f0eb3e53a0d99dff903c735c1ba49a888ee0223f3c103982&=&format=webp&quality=lossless&width=1333&height=593)

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
![problem 12a](https://media.discordapp.net/attachments/858349899401658398/1293139128501665792/image.png?ex=67064929&is=6704f7a9&hm=e768381b5eb6b0383ea17c88c537fd6867c4621ab2e7a36aed316591d9cb3d0a&=&format=webp&quality=lossless&width=1203&height=593)
![problem 12b](https://media.discordapp.net/attachments/858349899401658398/1293139347985662012/image.png?ex=6706495d&is=6704f7dd&hm=7186ed58ee38473353ce0d909b2ce05fd7569e24f2d0c5215e5517a900289401&=&format=webp&quality=lossless&width=1357&height=593)


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




