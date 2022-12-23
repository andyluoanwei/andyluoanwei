# 如何上传文件夹到GitHub

* [TOC]
+++
#### 1. 如果没有账号要先创建账号(有账号跳过此步骤)
#### 2. 建立一个仓库(有仓库跳过此步骤)
#### 3. 复制仓库地址
![](C:\Users\Andy\Desktop\Image\20221223\复制链接4.bmp)

#### 4. 以下为本地操作
 ###### 4.1 在本地新建一个空文件夹

![](C:\Users\Andy\Desktop\Image\20221223\创建git路径.bmp)

​	空文件夹可以省掉很多麻烦

 ###### 4.2 上传文件
  ###### 	4.2.1 在空文件夹内，右键选择Git Bash Here

![本地操作下的路径](C:\Users\Andy\Desktop\Image\20221223\创建git bash here.bmp)

  ###### 	4.2.2 弹出Git Bash框
  ![](C:\Users\Andy\Desktop\Image\20221223\git bash cmd.bmp)

  ###### 	4.2.3 克隆远程仓库
  github仓库地址
![](C:\Users\Andy\Desktop\Image\20221223\github shh地址.bmp)

​	在克隆仓库时，输入一下命令来连接github仓库上的url： 

> 1 | git clone + "你的仓库地址" 
> 2 | git clone https://github.com/andyluoanwei/re-ository.git		//我输入的是我刚复制自己的地址 

![](C:\Users\Andy\Desktop\Image\20221223\获取git文件.bmp)

![](C:\Users\Andy\Desktop\Image\20221223\bash1.bmp)

![](C:\Users\Andy\Desktop\Image\20221223\bash2.bmp)

![](C:\Users\Andy\Desktop\Image\20221223\python MySQL.bmp)
克隆成功！！！

 ###### 	4.2.4 把需要上传的文件夹放入到远程仓库文件夹内

  ![](C:\Users\Andy\Desktop\Image\20221223\上传1.bmp)

 ###### 	4.2.5 上传
依次输入以下命令：
> cd  andy-repository     //根据自己的远程仓库名输入
> git init
> git add .
> git commit -m “你的提交信息”
> git push

* ###### 命令解释：

  | 命令                                     | 描述                                                         |
  | :--------------------------------------- | :----------------------------------------------------------- |
  | cd + "远程仓库名"                        | 进入到远程仓库内(根据自己的仓库名输入)                       |
  | git init                                 | 初始化Git                                                    |
  | git add + "提交文件夹或文件" / git add . | 将文件区的文件添加到暂存区("."是当前目录下的所有文件，也可以只输入文件夹名称) |
  | git commit -m "提交的信息"               | 将暂存区的文件添加到本地仓库                                 |
  | git push                                 | 提交到远程仓库(可能需要输入账户和密码)                       |

  ![](C:\Users\Andy\Desktop\Image\20221223\上传2.bmp)

  ![](C:\Users\Andy\Desktop\Image\20221223\上传3.bmp)

  ![](C:\Users\Andy\Desktop\Image\20221223\上传4.bmp)

​	上传成功！！！