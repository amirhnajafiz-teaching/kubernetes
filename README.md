# WebBlocker

<p align="center">
  <img src="https://github.com/amirhnajafiz/WebBlocker/blob/master/logo.webp" width=200 /><br />
  <img src="https://camo.githubusercontent.com/4684cf2ad01026750084556a0abacb1cd99e4820884133184fe9968dc3e2a011/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6c6f636b2e737667" width=20 />
  <img src="https://camo.githubusercontent.com/c100a44b540f6bcea3f7bae169d5f75b44e8994a83deeaf2e9b7e7f9523c8bd3/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f7562756e74752e737667" width=20 />
  <img src="https://camo.githubusercontent.com/060acf7e46293144e29fca9e750d2d73af82c51bcb2d7340eb3ff24e9e03c6f0/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f64656269616e2e737667" width=20 />
  <img src="https://camo.githubusercontent.com/875b2967090ac970937698e92e1bfeefdc6168b9afb428aabfe321e19d549d74/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f6c696e75782e737667" width=20 />
  <img src="https://camo.githubusercontent.com/aa96ee3a3352c9c3c2161d3e95698d0885a277ab85d617fe77912627d37a3959/68747470733a2f2f6564656e742e6769746875622e696f2f537570657254696e7949636f6e732f696d616765732f7376672f707974686f6e2e737667" width=20 />
</p>

## Intro
<p>
  <b>Web Blocker</b> is an Linux application based on <i>python3</i>.<br />
  This script gets some websites urls and will block them , until you set theme free.<br />
</p>

## How to use ?
<p>
  First of all clone the project by : 
  
  ```shell
  git clone https://github.com/amirhnajafiz/WebBlocker.git
  ```
  Then write the web urls that you want to block in the <b>"data.txt"</b> in single lines.

  After that just execute the python file ( make sure you are using <i>python3</i> ):
  
  ```shell
  python3 script.py
  ```
  
  This script has an update time to unblock the website if neccesury.<br />
  For setting that time just execute file like this: ( in seconds )
  
  ```shell
  python3 script.py 3600 
  ```
</p>


## Warning
This program easily blocks any website you want, but be sure not to delete the "backup" file that creates
by the program.

Cause when we want to block the websites we make some changes to your system and for reseting everything
back to its normal we use the "backup" file.

For reseting the program just use following code:<br/>
```python
  python3 script.py RESET
```
