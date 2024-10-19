# Processes and Jobs
Before we start executing commands to get the flag, we have to connect to the server using our SSH key.
The command is as follows :
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Listing Processes
### Problem :
![s09533710192024](https://a.okmd.dev/md/671381a479328.png)
![s09535210192024](https://a.okmd.dev/md/671381b245c35.png)
![s09540210192024](https://a.okmd.dev/md/671381bd509e8.png)
### Solution :
![s09541510192024](https://a.okmd.dev/md/671381c98b669.png)
```
ps aux
```
This gives a list of all processes running in the terminal.
We look through all the processes for a file running in the challenge directory.
```
cat /challenge/3529-run-11422
```
We find the file and then read its contents which gives us further instructions.
```
/challenge/3529-run-11422
```
We run the file which gives us the flag.
### Flag for the challenge :
```
pwn.college{gmXopKAiGMn9YL4nr9ftUnjcShs.dhzM4QDL4IDO0czW}
```

## 2. Killing Processes
### Problem :
![s09542810192024](https://a.okmd.dev/md/671381d6e889e.png)
### Solution :
![s09544210192024](https://a.okmd.dev/md/671381e4c126d.png)
```
ps aux | grep /challenge/dont_run
```
This gives a list of all processes running in the terminal.
We pipe this output to the grep command to look for the /challenge/dont_run process.
```
kill 73
```
We get the PID of the process from the last command and then we use this PID to kill the process.
```
/challenge/run
```
This gives us the flag.
### Flag for the challenge :
```
pwn.college{kdn4iAJ9ZtxMK36l0yWmGCgHIrr.dJDN4QDL4IDO0czW}
```

## 3. Interrupting Processes
### Problem :
![s09545510192024](https://a.okmd.dev/md/671381f10c3e1.png)
### Solution :
![s09550310192024](https://a.okmd.dev/md/671381f8c14fc.png)
```
/challenge/run
```
This starts the process but we have to manually end the process to get the flag.
```
^C
```
We press Ctrl+C to exit the process and get the flag.
### Flag for the challenge :
```
pwn.college{cdh2Q3DGNXHj3XQJ6a-aOBQsIU3.dNDN4QDL4IDO0czW}
```

## 4. Suspending Processes
### Problem :
![s09551210192024](https://a.okmd.dev/md/67138202081c6.png)
### Solution :
![s09552110192024](https://a.okmd.dev/md/6713820b592ea.png)
```
/challenge/run
```
This starts the process but we have to run the process in background and foreground to get the flag.
```
^Z
```
We press Ctrl+Z to suspend the process.
```
/challenge/run
```
We run the command again to run the /challenge/run again after suspending it once.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{Ig4HQwusYiXMzHDq1jHAHoi6JXd.dVDN4QDL4IDO0czW}
```

## 5. Resuming Processes
### Problem :
![s09553310192024](https://a.okmd.dev/md/671382177eb42.png)
### Solution :
![s09554510192024](https://a.okmd.dev/md/6713822320b1f.png)
```
/challenge/run
```
This starts the /challenge/run process but it does not terminate on its own.
```
^Z
```
We press Ctrl+Z to suspend the process.
```
fg
```
We resume the suspended process and this gives us the flag.
### Flag for the challenge :
```
pwn.college{o4m1DTkwxW7qDtbsl4iHcqoWjrh.dZDN4QDL4IDO0czW}
```

## 6. Backgrounding Processes
### Problem :
![s09555810192024](https://a.okmd.dev/md/6713823085ad1.png)
![s09564710192024](https://a.okmd.dev/md/6713826193132.png)
### Solution :
![s09563810192024](https://a.okmd.dev/md/67138258585a8.png)
```
/challenge/run
```
This starts the /challenge/run process but it does not terminate on its own.
```
^Z
```
We press Ctrl+Z to suspend the process.
```
bg
```
We resume the suspended process in the background.
```
/challenge/run
```
This runs the /challenge/run in the foreground as well.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{Uc3Lg9Zky1M4RxeAfDShQjyAttq.ddDN4QDL4IDO0czW}
```

## 7. Foregrounding Processes
### Problem :
![s09565810192024](https://a.okmd.dev/md/6713826c27439.png)
### Solution :
![s09570810192024](https://a.okmd.dev/md/6713827676eff.png)
```
/challenge/run
```
This starts the /challenge/run process but it does not terminate on its own.
```
^Z
```
We press Ctrl+Z to suspend the process.
```
bg
```
We resume the suspended process in the background.
```
fg
```
We bring the background process to the foreground.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{IRAs0BLLL_xvU8IILvhAjG2qCfz.dhDN4QDL4IDO0czW}
```

## 7. Starting Background Processes
### Problem :
![s09572010192024](https://a.okmd.dev/md/67138281b864e.png)
### Solution :
![s09572810192024](https://a.okmd.dev/md/6713828a8bb91.png)
```
/challenge/run &
```
This starts the /challenge/run process in the background but it does not terminate on its own.
This gives us the flag.
```
^C
```
We press Ctrl+C to kill the process.
### Flag for the challenge :
```
pwn.college{YjJIORWidiHIl2bz4uAHMLzhDkj.dlDN4QDL4IDO0czW}
```

## 8. Process Exit Codes
### Problem :
![s09574510192024](https://a.okmd.dev/md/6713829c27c03.png)
### Solution :
![s09575410192024](https://a.okmd.dev/md/671382a3b7c6f.png)
```
/challenge/get-code
```
Running this gives us an exit code
```
echo $?
```
We print the error code of the process in our terminal.
```
/challenge/submit-code 133
```
We pass the error code as an argument to /challenge/submit-code.
This gives us the flag.
### Flag for the challenge :
```
pwn.college{8TArEd4TXdnEyx6oxOfiLTWq5LO.dljN4UDL4IDO0czW}
```
