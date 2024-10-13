# Perceiving Permissions
Before we start executing commands to get the flag, we have to connect to the server using our SSH key. 
The command is as follows : 
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Changing File Ownership
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295035785724035154/image.png?ex=670d2f8f&is=670bde0f&hm=a17f3dc3e1bc3532d8e40d57c966d1d8082165cbb1c049aa9d87551a513668e4&=&format=webp&quality=lossless&width=1063&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295036007204524263/image.png?ex=670d2fc4&is=670bde44&hm=c486b2c140a17d3929e8b6685e7d9cf18cb9d0db0300a6f862df7e447520a6bf&=&format=webp&quality=lossless&width=970&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295036358083088476/image.png?ex=670d3018&is=670bde98&hm=efe87467b069e7899656212c72c06afec45aa0c357a56f4f4d682d14f51e7bda&=&format=webp&quality=lossless&width=1170&height=593)
```
chown hacker /flag
```
This turns the user hacker into the owner of the file flag.
```
ls -l /flag
```
This shows us the access permissions of the file flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{0ULfKrMc6k8WMzuw9Fc2WQnVJZg.dFTM2QDL4IDO0czW}
```

## 2. Groups and Files
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295037031394574437/image.png?ex=670d30b8&is=670bdf38&hm=4f4efaf49c1448a65c6c6567218a8e6cfdcf72334edcf413e6b89e6b633853bd&=&format=webp&quality=lossless&width=1040&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295037114307837982/image.png?ex=670d30cc&is=670bdf4c&hm=0b814ea9d5c60d470b7872f2c9714fb8ae9f5231f22827e517d9477dbf535f7b&=&format=webp&quality=lossless&width=1212&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295037161569124352/image.png?ex=670d30d7&is=670bdf57&hm=f8dd1fb36eb9e201ec7ae922944032bcc15b803a9a11670c68684141260231f9&=&format=webp&quality=lossless&width=687&height=226)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295037555246497842/image.png?ex=670d3135&is=670bdfb5&hm=883a0eecd337656dab654f9c1a0ad8d56c1094ac6482522309936b1c16c4c8a8&=&format=webp&quality=lossless&width=1175&height=586)
```
chgrp hacker /flag
```
This turns the group hacker into the owner of the file flag.
```
ls -l /flag
```
This shows us the access permissions of the file flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{ISMqecrnbLLLWdwpI8Zlku5W5rF.dFzNyUDL4IDO0czW}
```

## 3. Fun with Group Names
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295056522954670210/image.png?ex=670d42e0&is=670bf160&hm=6dcc05cca57404ecfa5b25b19322b74e84b4e1a5a632154afd1abec87dc29adf&=&format=webp&quality=lossless&width=1440&height=276)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295066974501605446/image.png?ex=670d4c9b&is=670bfb1b&hm=0b1a498410162ea93d426ba4876552db73e9fe7ab76906d78d44c8999eda5107&=&format=webp&quality=lossless&width=1165&height=593)
```
id
```
We find the name of the group our user is part of.
```
chgrp grp18355 /flag
```
This grants access of the flag to the grp18355 group and our user is part of this group.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{AWr34PADkBam92h_IQDKuhYKepu.dJzNyUDL4IDO0czW}
```

## 4. Changing Permissions
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295056522954670210/image.png?ex=670d42e0&is=670bf160&hm=6dcc05cca57404ecfa5b25b19322b74e84b4e1a5a632154afd1abec87dc29adf&=&format=webp&quality=lossless&width=1440&height=276)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295067808551403561/image.png?ex=670d4d62&is=670bfbe2&hm=835910ede8de3609e01c5b9d6ef93d3e9e56a35d1bf20d5d990e1a5001647de5&=&format=webp&quality=lossless&width=687&height=337)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295067876021112852/image.png?ex=670d4d72&is=670bfbf2&hm=153e4d0646dc95946228309d10776372903db177a379320ed5ce8d63b2e5175e&=&format=webp&quality=lossless&width=1243&height=593)
![Question](https://media.discordapp.net/attachments/858349899401658398/1295067919910309940/image.png?ex=670d4d7d&is=670bfbfd&hm=2e84b0dd0ea104fda68f7f0d7ddd4ed37e45936d50613f3beab2b137141e8ea2&=&format=webp&quality=lossless&width=1440&height=567)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295094674121556038/image.png?ex=670d6668&is=670c14e8&hm=eeea8abe0ca9403f23b3f860f08db235c78afe8bda97b33eab9753b67ad0fbc6&=&format=webp&quality=lossless&width=1141&height=593)
```
ls -l /flag
```
This shows us the access permissions of the file flag.
```
chmod o+r /flag
```
We change the permission for other users (like us) to be able to read the flag.
```
ls -l /flag
```
This shows us the updated access permissions of the file flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{AOTCEjOYGYoVCBG00sRj4IrGqCa.dNzNyUDL4IDO0czW}
```

## 5. Executable Files
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295096697344491623/image.png?ex=670d684a&is=670c16ca&hm=d769ed29164311d5fd19f18c863393e92e4dc9a28a07119bb0c2bef5bfb435f7&=&format=webp&quality=lossless&width=1120&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295096817922605076/image.png?ex=670d6867&is=670c16e7&hm=9b8e0c04e9dbdec91e99f092410e6c52639c68904a6ee01f9ae5fb37b54ac2f1&=&format=webp&quality=lossless&width=1157&height=593)
```
ls -l /challenge/run
```
This shows us the access permissions of the file.
```
chmod a+x /challenge/run
```
We change the permission for all users (including us) to be able to execute the file.
```
ls -l /challenge/run
```
This shows us the updated access permissions of the file.
```
/challenge/run
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{cIIVxNas4haF7HX5pfK8iCoDKA9.dJTM2QDL4IDO0czW}
```

## 6. Permission Tweaking Practice
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295097718254862432/image.png?ex=670d693d&is=670c17bd&hm=9c19943ff5159df61afa9fac21093eda4bf65b44174f3c109207e890f95a110a&=&format=webp&quality=lossless&width=1440&height=198)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295098094098317444/image.png?ex=670d6997&is=670c1817&hm=96419117c889214a9f40813c6658dad94f71d3d1ee7836ab70e2ce7d19f81b81&=&format=webp&quality=lossless&width=1175&height=587)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295098145314836550/image.png?ex=670d69a3&is=670c1823&hm=b26563b95e965ad087764f9e2430122fbcde52cddbcfaec4117105e3644823cb&=&format=webp&quality=lossless&width=1175&height=551)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295098178819068064/image.png?ex=670d69ab&is=670c182b&hm=a0cbd2a52269325fbf2ef7e10c45e7871ccbca5ee444a7f2d0f220600e1c9005&=&format=webp&quality=lossless&width=1175&height=547)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295098214214664352/image.png?ex=670d69b4&is=670c1834&hm=8a3de63a3457317fe52c38baf80a1b8d47519ab9780d65dd9540ea1e263ca5ac&=&format=webp&quality=lossless&width=1175&height=547)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295098243931308133/image.png?ex=670d69bb&is=670c183b&hm=24763f19ee76e3e0a140c46a976c04a33356d0d73d34fe75cce95164362f5dfc&=&format=webp&quality=lossless&width=1175&height=505)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295098291737989261/image.png?ex=670d69c6&is=670c1846&hm=5b119585ce722cd392f69257935a8bd9a91f0c1bce94f7621007344df76abbf0&=&format=webp&quality=lossless&width=1175&height=453)
We keep following the instructions provided at every round and changing the permissions accordingly.  
Once all rounds have been successfully cleared, we get the flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{4KZif2wvd8OGj4QaGvS8GfR7dVS.dBTM2QDL4IDO8czW}
```

## 7. Permission Setting Practice
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295101651400654920/image.png?ex=670d6ce7&is=670c1b67&hm=ed425c266b0875b45d057a03cdb68377a5964eacc53d2e5e9b16bb8e4653bb82&=&format=webp&quality=lossless&width=1197&height=592)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295101893370052783/image.png?ex=670d6d21&is=670c1ba1&hm=76509b45c9bd9c6bff883684386e845dd8dc294b813100787e69276fb82c527f&=&format=webp&quality=lossless&width=1175&height=583)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295101927234867341/image.png?ex=670d6d29&is=670c1ba9&hm=b4659c0e5c51fe78dd3ea00207d84e412cc930ec2c227788f71b0116ceb9bb38&=&format=webp&quality=lossless&width=687&height=321)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295101946256162892/image.png?ex=670d6d2d&is=670c1bad&hm=05c87c0734250f4bab37e4f35276c2b8763db814b065ddf790ff6ef38e268db0&=&format=webp&quality=lossless&width=687&height=295)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295101971828838480/image.png?ex=670d6d33&is=670c1bb3&hm=2d175f69648108974997e1ff224dd8e27b4769c3f8689428ea19ad4583dfa284&=&format=webp&quality=lossless&width=1175&height=550)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295102001763319849/image.png?ex=670d6d3b&is=670c1bbb&hm=55d3c4197c7269ba76a65347808b4ea9693e4037207ed9ed21bd3da64cbd18b3&=&format=webp&quality=lossless&width=687&height=300)
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295102031152939059/image.png?ex=670d6d42&is=670c1bc2&hm=be8449fce978607d93c0529b5c6647867c4cdc03a9f517bf7ee9c84a8ed9213b&=&format=webp&quality=lossless&width=1175&height=438)
We keep following the instructions provided at every round and changing the permissions accordingly.  
Once all rounds have been successfully cleared, we get the flag.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{ED6h8wNKM2I175PYZAm_7Y_fRD2.dNTM5QDL4IDO0czW}
```

## 8. The SUID Bit
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1295103109068230806/image.png?ex=670d6e43&is=670c1cc3&hm=9833a158d3110a9461d68519c251a826cb9b287f4226aa1f1cf935331d86efc4&=&format=webp&quality=lossless&width=1116&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1295103287225221121/image.png?ex=670d6e6d&is=670c1ced&hm=5875dde0ea977e3b732cc10b95cb0d289f997d6bf135c4ed0e1e6cc7840bf159&=&format=webp&quality=lossless&width=1175&height=592)
```
ls -l /challenge/getroot
```
This shows us the access permissions of the file.
```
chmod a+s /challenge/getroot
```
We change the permission for all users (including us) to be able to execute the file.
```
/challenge/getroot
```
This sets the SUID bit for the program and let us run it as root.
```
cat /flag
```
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{EJKb2ZwYvcV4uUioIZk_bmPOsDi.dNTM2QDL4IDO0czW}
```
