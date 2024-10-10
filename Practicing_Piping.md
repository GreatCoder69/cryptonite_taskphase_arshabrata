# Practicing Piping
## 1. Redirecting Output
### Problem :
![problem 1](https://media.discordapp.net/attachments/858349899401658398/1293576862290804808/image.png?ex=6707e0d5&is=67068f55&hm=46a08e3020edf4474b781ca57e3ba801313bff085975900d0c526c959a033299&=&format=webp&quality=lossless&width=1440&height=388)
### Solution :
```
echo PWN > COLLEGE
```
This redirects the standard output of echo PWN (which is PWN) to be stored in the COLLEGE file.   
This gives us the flag.
### Flag for the challenge :
```
Correct! You successfully redirected 'PWN' to the file 'COLLEGE'! Here is your
flag:
pwn.college{Mr0UFWDLeGdwKQYJVdbDT1cuPht.dRjN1QDL4IDO0czW}
```

## 2. Redirecting More Output
### Problem :
![problem 2](https://media.discordapp.net/attachments/858349899401658398/1293577569387417682/image.png?ex=6707e17e&is=67068ffe&hm=842b44d65ae3f6ba7baf5854f077b9e38ab4a39b6bfe7c804275b3174c36ac82&=&format=webp&quality=lossless&width=1440&height=233)
### Solution :
```
/challenge/run > myflag
```
We redirect the standard output of /challenge/run to be stored in the myflag file.
```
cat myflag
```
We read the contents of the myflag file which now contains the standard output of /challenge/run which gives us our flag.
### Flag for the challenge :
```
[FLAG] Here is your flag:
[FLAG] pwn.college{Uxi3lROBOxnW0e5_G-wzCQpECU9.dVjN1QDL4IDO0czW}
```

## 3. Appending Output
### Problem :
![problem 3](https://media.discordapp.net/attachments/858349899401658398/1293578496852885585/image.png?ex=6707e25b&is=670690db&hm=120083344cb44cc5f10a5a1524a555baa80d269f9f6a17640426eb1537f54b5e&=&format=webp&quality=lossless&width=1411&height=593)
### Solution :
```
/challenge/run >> /home/hacker/the-flag
```
This appends the second part of the flag from run to the-flag file.
```
cat /home/hacker/the-flag
```
This gives us the flag.
### Flag for the challenge :
```
 |
\|/ This is the first half:
 v
pwn.college{Y7tXU_8ZrA1K6SuOgzu7KFQqT1W.ddDM5QDL4IDO0czW}
                              ^
     that is the second half /|\
                              |
```

## 4. Redirecting Errors
### Problem :
![problem 4a](https://media.discordapp.net/attachments/858349899401658398/1293632147181277205/image.png?ex=67081452&is=6706c2d2&hm=c6c2ee26b02a5ffc2f383f1e75972f1892c2459260d009e10176ead2b5d27a0b&=&format=webp&quality=lossless&width=1425&height=593)
![problem 4b](https://media.discordapp.net/attachments/858349899401658398/1293632306396794900/image.png?ex=67081478&is=6706c2f8&hm=1188e6c3d454ed71ff4dd84941339906bdb938cdd5c37327b09e6f2e5c48e521&=&format=webp&quality=lossless&width=1440&height=356)
### Solution :
```
/challenge/run > myflag 2> instructions
```
We redirect the standard output of /challenge/run to myflag using > and the standard errors to instructions using 2> .
```
cat myflag
```
This gives us the flag.
### Flag for the challenge :
```
[FLAG] Here is your flag:
[FLAG] pwn.college{IwPp9d-Bn1_yTvwfWzLBSnGDMFV.ddjN1QDL4IDO0czW}
```

## 5. Redirecting Input
### Problem :
![problem 5](https://media.discordapp.net/attachments/858349899401658398/1293861851377041468/image.png?ex=6708ea40&is=670798c0&hm=7a493989ad76365afbc591d269495e1cf75a538393b7812ece600b33329a4342&=&format=webp&quality=lossless&width=687&height=200)
### Solution :
```
echo COLLEGE > PWN
```
The standard output of echo COLLEGE is stored in PWN.
```
/challenge/run < PWN
```
We redirect the input of /challenge/run to be the output of PWN using < .
### Flag for the challenge :
```
Correct! You have redirected the PWN file into my standard input, and I read
the value 'COLLEGE' out of it!
Here is your flag:
pwn.college{EZy8k8bsYPLh2Wvo44wEEHqsFuR.dBzN1QDL4IDO0czW}
```

## 6. Grepping Stored Result
### Problem :
![problem 6](https://media.discordapp.net/attachments/858349899401658398/1293864412553412638/image.png?ex=6708eca2&is=67079b22&hm=1bab5cf7a0366be24b610a176e10a131d6fa05e102d19331abaef82e3ef31aa2&=&format=webp&quality=lossless&width=1440&height=270)
### Solution :
```
/challenge/run > /tmp/data.txt
```
We redirect the standard output of /challenge/run to be stored in /tmp/data.txt.
```
grep pwn.college /tmp/data.txt
```
We use grep to find the flag in the file. The flag starts with pwn.college.
### Flag for the challenge :
```
pwn.college{cCy31dna3io12GWjhZMlWlxuCoE.dhTM4QDL4IDO0czW}
```

## 7. Grepping Live Output
### Problem :
![problem 7](https://media.discordapp.net/attachments/858349899401658398/1293866580308135946/image.png?ex=6708eea7&is=67079d27&hm=d3e31fc43523dd6ffbbf279e1c66ff98ea52cf404531ffe4f415072653e98e29&=&format=webp&quality=lossless&width=1440&height=445)
### Solution :
```
/challenge/run | grep pwn.college
```
We redirect the standard output of /challenge/run to the standard input of grep using | and search for the flag beginning with pwn.college.
### Flag for the challenge :
```
[PASS] Success! You have satisfied all execution requirements.
pwn.college{IYR2Nos_Tg2beRJkIB9Ge7N05Yj.dlTM4QDL4IDO0czW}
```

## 8. Grepping Errors
### Problem :
![problem 8](https://media.discordapp.net/attachments/858349899401658398/1293867858396450816/image.png?ex=6708efd8&is=67079e58&hm=36722389eb164b246f7ce4e2502f905e64d97bc710526ad59696a2f8ebcda496&=&format=webp&quality=lossless&width=1440&height=460)
### Solution :
```
/challenge/run 2>&1 | grep pwn.college
```
We change the standard error of /challenge/run to standard output using 2>&1 which can now be piped into the standard input of grep using | and then search for the flag.
### Flag for the challenge :
```
[PASS] You have passed the checks on the process on the other end of my stderr!
[PASS] Success! You have satisfied all execution requirements.
pwn.college{EqNzXjn2yHH_G75xSUohJzmr3gV.dVDM5QDL4IDO0czW}
```

## 9. Duplicating Piped Data with Tee
### Problem :
![problem 9](https://media.discordapp.net/attachments/858349899401658398/1293870347346509824/image.png?ex=6708f229&is=6707a0a9&hm=073547dedb8c96cc93cebf4cdb38f2f37c39127e964c1898ee2729ceb386e80d&=&format=webp&quality=lossless&width=977&height=593)
### Solution :
```
/challenge/pwn | tee a | /challenge/college
```
We pipe the standartd output of /challenge/pwn to a file named "a" along with which we pass it to the standard input of /challenge/college using tee.  
The file "a" now contains how to obtain the flag.
```
cat a
```
We see that:  
Usage: /challenge/pwn --secret [SECRET_ARG]  
SECRET_ARG should be "cY10leta"
```
/challenge/pwn --secret cY10leta | /challenge/college
```
We pass the argument we just obtained and pipe the output to the inpur of /challenge/college.  
This gives us the flag.
### Flag for the challenge :
```
Correct! Passing secret value to /challenge/college...
Great job! Here is your flag:
pwn.college{cY10letawmGyhnqqjNY3Nuj7geu.dFjM5QDL4IDO0czW}
```

## 10. Writing to Multiple Programs
### Problem :
![problem 10a](https://media.discordapp.net/attachments/858349899401658398/1293871434711433278/image.png?ex=6708f32d&is=6707a1ad&hm=28e83a5d6deedb523523ea4414383105fa965f92a06da7cfc4f6ffeda00ed77b&=&format=webp&quality=lossless&width=1183&height=593)
![problem 10b](https://media.discordapp.net/attachments/858349899401658398/1293871614345084959/Screenshot_2024-10-10_151319.png?ex=6708f357&is=6707a1d7&hm=1f9e8134f150c7551325daf2034d190df2c13a1c7fea2ea8cb4f5e01268c0e2f&=&format=webp&quality=lossless&width=687&height=332)
![problem 10c](https://media.discordapp.net/attachments/858349899401658398/1293871636532957255/image.png?ex=6708f35d&is=6707a1dd&hm=aaa0bc317655dab1824febd6b49f0641117980710cb4ee32ad59ae597c9a0343&=&format=webp&quality=lossless&width=687&height=177)
### Solution :
```
/challenge/hack | tee >(/challenge/the) >(/challenge/planet)
```
The standard output of /challenge/hack is duplicated as input into the /challenge/the and /challenge/planet using tee along >().
### Flag for the challenge :
```
Congratulations, you have duplicated data into the input of two programs! Here
is your flag:
pwn.college{0tcwVfbT_i-30cwH3boPlwyANdX.dBDO0UDL4IDO0czW}
```

## 11. Split-piping stderr and stdout
### Problem :
![problem 11](https://media.discordapp.net/attachments/858349899401658398/1293885749569130517/image.png?ex=67090081&is=6707af01&hm=60dd1c57303adfa2bcfae7fb0928d93922b66f5be0ebc77c0f5b1acbafec598e&=&format=webp&quality=lossless&width=687&height=235)
### Solution :
```
/challenge/hack 2> >( /challenge/the ) | tee >( /challenge/planet )
```
We redirect the standard error of /challenge/hack to /challenge/the using 2> for getting the error and then > for the redirection.  
We then pipe the standard output of /challenge/hack to the standard input of /challenge/plannet using tee.  
This gives us the flag.
### Flag for the challenge :
```
Congratulations, you have learned a redirection technique that even experts
struggle with! Here is your flag:
pwn.college{w3sdCI1ExuFMJnii6qSUbNGsIJP.dFDNwYDL4IDO0czW}
```




