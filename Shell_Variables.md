# Shell Variables
Before we start executing commands to get the flag, we have to connect to the server using our SSH key. 
The command is as follows : 
```
ssh -i ./key hacker@dojo.pwn.college
```
## 1. Printing Variables
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294662035291770971/image.png?ex=670bd37a&is=670a81fa&hm=35b2488f15da83a9f1ec0816a980c440e06db505e200dd6a7e7257e54120b9f0&=&format=webp&quality=lossless&width=687&height=238)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294662633915682877/image.png?ex=670bd409&is=670a8289&hm=ee5b8965e7c990f34d0211302f8485afc1aa86962f571e5f4aa13c134764a8c3&=&format=webp&quality=lossless&width=1175&height=593)
```
echo $FLAG
```
The value of flag is stored in the variable FLAG.  
We get the flag by printing the value of FLAG using $ and echo.
### Flag for the challenge : 
```
pwn.college{0Gro5dhUKvSEZiubCzG6kNN69Zo.ddTN1QDL4IDO0czW}
```

## 2. Setting Variables
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294663314067951636/image.png?ex=670bd4ab&is=670a832b&hm=7e6df9269501ada3c0f50be7b6065f102775a5c35800f3a4b36cfd81094319ba&=&format=webp&quality=lossless&width=1390&height=592)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294903272896729162/image.png?ex=670cb426&is=670b62a6&hm=965d5a1a784a415e0030ead09269f763f68841cfd0298fd35e9896768835c21e&=&format=webp&quality=lossless&width=1175&height=586)
```
PWN=COLLEGE
```
We store the value COLLEGE in PWN using =. This gives us the flag.
### Flag for the challenge : 
```
pwn.college{k0oPFkoOcwDrlbbHru5GCGNHxaQ.dlTN1QDL4IDO0czW}
```

## 3. Multi-word Variables 
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294895640308088872/image.png?ex=670cad0a&is=670b5b8a&hm=cd42579420526e0cc95816fe1e5e82d938545a29b65937d43dd4ed935de2bdf0&=&format=webp&quality=lossless&width=1440&height=545)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294895932806140008/image.png?ex=670cad50&is=670b5bd0&hm=f16fa8774c41f7207c61e5c0ddc98ee91b9e5d51c4391d253f82f99f7ad6c63b&=&format=webp&quality=lossless&width=1175&height=588)
```
PWN="COLLEGE YEAH"
```
We store the multi-word variable using "". This gives us the flag.
### Flag for the challenge : 
```
pwn.college{Me-TRr1UZu0Iockqk7MnHU6-Sg5.dBjN1QDL4IDO0czW}
```

## 4. Exporting Variables 
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294896445442228224/Screenshot_2024-10-13_110544.png?ex=670cadca&is=670b5c4a&hm=c69fadc2bc13d2e343e783814104c7eae3f12569bdb39237ef1e559bacad7686&=&format=webp&quality=lossless&width=1440&height=588)
![Question](https://media.discordapp.net/attachments/858349899401658398/1294896445094105178/Screenshot_2024-10-13_110553.png?ex=670cadca&is=670b5c4a&hm=34ae02eb0b4b553cd82f0b122f5123d995ff6e019c1a75db8b8ada1e0b5d1cf7&=&format=webp&quality=lossless&width=1440&height=481)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294896657334272160/image.png?ex=670cadfd&is=670b5c7d&hm=6ae2c1cd3945ba8940f0212db6c421640e47a460c7757c2c8011ad0d3255b04f&=&format=webp&quality=lossless&width=1175&height=592)
```
export PWN=COLLEGE
```
We store COLLEGE in the variable and PWN and export it to the new shell.
```
COLLEGE=PWN
```
We store PWN in the variable COLLEGE but do not export it to the new shell.
```
sh
```
This opens up a new shell.
```
/challenge/run $PWN
```
We pass the value of PWN (which we exported) as argument of /challenge/run which gives us the flag.
### Flag for the challenge : 
```
pwn.college{s7dK4RRy6IiH-dWi5afKqJszUOk.dJjN1QDL4IDO0czW}
```

## 5. Printing Exported Variables
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294897511324061837/image.png?ex=670caec8&is=670b5d48&hm=99859d9effd0f624ab07f0c52baed02df11f3b89988db86d371382a24d14d80f&=&format=webp&quality=lossless&width=1440&height=178)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294904080321347605/image.png?ex=670cb4e6&is=670b6366&hm=2c0d14ccee0a865ccefc440b5d654f82ecae0bfc20b33419f2c6536020f00010&=&format=webp&quality=lossless&width=1178&height=593)
```
env | grep pwn.college
```
We pipe the output of grep which gives all exported values in the shell into the grep command with pwn.college to obtain the flag.
### Flag for the challenge : 
```
pwn.college{MWQUeJoGSXtNp1PsOnRqNa2zgPe.dhTN1QDL4IDO0czW}
```

## 6. Storing Command Output
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294898678074576976/image.png?ex=670cafde&is=670b5e5e&hm=172292ddd3abfb570b34f401435e2ca6cae27451abde23742f24d1433905b959&=&format=webp&quality=lossless&width=1440&height=495)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294898853018992670/image.png?ex=670cb008&is=670b5e88&hm=12faea89a39d3d835ea395fdfcfe0244cff00a558e0b479c237e4be3f910e08f&=&format=webp&quality=lossless&width=1175&height=592)
```
PWN=$(/challenge/run)
```
This reads the output of /challenge/run into the variable PWN.
```
echo $PWN
```
This prints out the flag to our terminal.
### Flag for the challenge : 
```
pwn.college{oiLfE2WBpK3AaL1Tl7Ra6G0coye.dVzN0UDL4IDO0czW}
```

## 7. Reading Input
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294899704353783889/Screenshot_2024-10-13_111844.png?ex=670cb0d3&is=670b5f53&hm=dab44c7404909a18377eee0f2f65e71672171e66d6ba8383a5aba786398faae3&=&format=webp&quality=lossless&width=1341&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294899913250963466/image.png?ex=670cb105&is=670b5f85&hm=adbf3ab8bd69733c81b1cf243afab39c128568ee9a2c40bab0af40c2ffd65626&=&format=webp&quality=lossless&width=1175&height=585)
```
read -p "input : " PWN
```
This gives a prompt "input : " and then takes input from user. In this case we enter COLLEGE.  
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{cDzZm-mUg8zKy4pBwNdVg3m-6Kq.dhzN1QDL4IDO0czW}
```

## 8. Reading Files
### Problem : 
![Question](https://media.discordapp.net/attachments/858349899401658398/1294900642048905267/image.png?ex=670cb1b3&is=670b6033&hm=7613768bf2b9b5eef5450717dbbfa1351ac4cc5c4f0627903c5815b2d9b36ca4&=&format=webp&quality=lossless&width=1268&height=593)
### Solution : 
![Solution](https://media.discordapp.net/attachments/858349899401658398/1294900778687008878/image.png?ex=670cb1d3&is=670b6053&hm=4de7097ac5730e16c032b116dbb0e6da79f802eda933924ee13d1c3e10bf9c1c&=&format=webp&quality=lossless&width=687&height=348)
```
read PWN < /challenge/read_me
```
We read the output of /challenge/read_me directly into the variable PWN using < to redirect. 
This gives us the flag.
### Flag for the challenge : 
```
pwn.college{4t8CZtFPFrw40g7furU83yRAtaD.dBjM4QDL4IDO0czW}
```

