# Practicing Piping
## 1. Redirecting Output
### Problem :
![s18484610162024](https://a.okmd.dev/md/670fbd3987efd.png)
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
![s18490410162024](https://a.okmd.dev/md/670fbd4b264ee.png)
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
![s18492010162024](https://a.okmd.dev/md/670fbd5b03e64.png)
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
![s18493610162024](https://a.okmd.dev/md/670fbd6b570cc.png)
![s18494710162024](https://a.okmd.dev/md/670fbd76aea38.png)
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
![s18500810162024](https://a.okmd.dev/md/670fbd8ae2e1c.png)
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
![s18502310162024](https://a.okmd.dev/md/670fbd9994fbe.png)
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
![s18504010162024](https://a.okmd.dev/md/670fbdab18c8e.png)
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
![s18505410162024](https://a.okmd.dev/md/670fbdb8b8f34.png)
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
![s18510910162024](https://a.okmd.dev/md/670fbdc84b0cc.png)
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
![s18513310162024](https://a.okmd.dev/md/670fbddfa97cf.png)
![s18515310162024](https://a.okmd.dev/md/670fbdf44a215.png)
![s18520510162024](https://a.okmd.dev/md/670fbe0095d4b.png)
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
![s18522510162024](https://a.okmd.dev/md/670fbe14b7926.png)
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
