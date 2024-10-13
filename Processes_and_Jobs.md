# Processes and Jobs
Before we start executing commands to get the flag, we have to connect to the server using our SSH key. 
The command is as follows : 
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Listing Processes
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294906105117282344/Screenshot_2024-10-13_114349.png?ex=670cb6c9&is=670b6549&hm=31c3d04e5f30271e9ca7bdbcc2515176b4516228b2e44feefba0a52c9a6801fa&=&format=webp&quality=lossless&width=1027&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1294906104844648458/Screenshot_2024-10-13_114407.png?ex=670cb6c9&is=670b6549&hm=b3965960cf28cedba308996f62aab9f695bac92024b411904cbc25df23496c61&=&format=webp&quality=lossless&width=1376&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1294906104534401095/Screenshot_2024-10-13_114417.png?ex=670cb6c9&is=670b6549&hm=0ef30c4ed198c7ef7455218d6709d0465955c78c36f4daaeb09deadc59c410bf&=&format=webp&quality=lossless&width=1058&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294906493782589551/image.png?ex=670cb726&is=670b65a6&hm=a18a7a56cd5245dc48858eb141e33622bc1bb009a8192847b0350a4977b24302&=&format=webp&quality=lossless&width=1157&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1294912250712293417/image.png?ex=670cbc82&is=670b6b02&hm=107acb53a43bc2086283496f7768ba8b9975d46ddf85085841df6703dd5c1b6b&=&format=webp&quality=lossless&width=687&height=331)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294912546855190569/image.png?ex=670cbcc9&is=670b6b49&hm=71243ae93f2d8943b230251fdb4bf8a3c8ee7ed2b79f9c5e121d8f569de6f2e9&=&format=webp&quality=lossless&width=1170&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1294913528087576631/image.png?ex=670cbdb3&is=670b6c33&hm=e9bab21ac1512563ddc608672e7fcb3289992ed13c6144c50897f6b00a45dded&=&format=webp&quality=lossless&width=1440&height=273)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294913750775889920/image.png?ex=670cbde8&is=670b6c68&hm=4c722cb39f24d85bc57d4ef749a1e5ab028a6af183883c31d09a22019bdf279f&=&format=webp&quality=lossless&width=1175&height=592)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1294914200941891675/image.png?ex=670cbe53&is=670b6cd3&hm=68b65629da8d8c4c58648c9cf28fc4ef343101c876a6bfe0ae8c4d9b963c7e16&=&format=webp&quality=lossless&width=1440&height=212)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295020900290400276/image.png?ex=670d21b2&is=670bd032&hm=2000046149964d0f01c9c9aeb0436c4b1aef64d63ee751aa32ac4bb1f1898fde&=&format=webp&quality=lossless&width=1175&height=486)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295021828246339734/image.png?ex=670d2290&is=670bd110&hm=6d1349c0b630624b9f8d1472f3d8309cd68843de3725e1ef225e2b86058225c2&=&format=webp&quality=lossless&width=1440&height=167)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295023505653497876/image.png?ex=670d2420&is=670bd2a0&hm=93e2e2e140473195d2ce0dd0357bb641d3634d4535f8aca48b009fcfe51c67cb&=&format=webp&quality=lossless&width=1178&height=592)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295024367519924306/image.png?ex=670d24ed&is=670bd36d&hm=eb90251bb8af3603096925b70a0bef555814661f735e1d4113e1caf428329dd4&=&format=webp&quality=lossless&width=1440&height=580)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295024497019322419/image.png?ex=670d250c&is=670bd38c&hm=a21d93b47195a2ce7d12722bf30ad8574827df1218a7cdb1994b1be6d93029b8&=&format=webp&quality=lossless&width=1193&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295024798476537856/image.png?ex=670d2554&is=670bd3d4&hm=d3b9e500987e1a7ca981d0699f7458779bce6b0b9207ac4dd0254fffac7bbd16&=&format=webp&quality=lossless&width=1136&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295025808980705291/image.png?ex=670d2645&is=670bd4c5&hm=4ad4319d0491f037f7997d1868dcf78cf3fbe8f21da034c12bcf9d7cf7327282&=&format=webp&quality=lossless&width=1440&height=111)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295025957010411580/image.png?ex=670d2668&is=670bd4e8&hm=5612f2a9bdfe5886b2f60a7a8afc92e6810894263af5bd1792b5bb92512e7dab&=&format=webp&quality=lossless&width=1170&height=593)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295027069859659838/image.png?ex=670d2771&is=670bd5f1&hm=ff2b70714bc2dffd62a05c49050631fc58aac798903d31ca13805d576c122c87&=&format=webp&quality=lossless&width=1440&height=446)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295027314727587992/image.png?ex=670d27ac&is=670bd62c&hm=417f3461e1cfc5f447623b28e9f583cbe19f83c52e9a281c9907235295b29187&=&format=webp&quality=lossless&width=687&height=348)
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
![Question](https://media.discordapp.net/attachments/858349899401658398/1295028271356051487/image.png?ex=670d2890&is=670bd710&hm=73325f264c8cc06bfcb2df210b82a40915745456f950bf457cb808eb3428e361&=&format=webp&quality=lossless&width=1286&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295028064295850004/image.png?ex=670d285e&is=670bd6de&hm=9937c3a7f38afac0a8fe4f4be02dd29caf2bd8d39b012f7240eaaa3fa9ba8947&=&format=webp&quality=lossless&width=1167&height=593)
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

