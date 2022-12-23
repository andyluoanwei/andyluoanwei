# Git学习

+++

### 1.  什么是git？

### 2. git的安装

### 3. git的使用

  ##### 	3.1 git的工作流程
  ##### 	3.2 git初始化配置

* 配置用户名

  ```python
  1 | git config --global user.name "Andy LA Wei" 			# 该名字是上传代码的用户名
  ```
  
* 配置用户邮箱
  
	```python
	# 该邮箱是其他作者联系你的邮箱
	1 | git config --global user.email "anan2001vip@163.com"	# 和你的代码托管中心没有任何关系
	```
	
* 配置大小写敏感
	
	```python
	1 ｜ git config --global core.ignorecase false
	```

* 查看Git配置信息可以用下面的命令

  ```python
  1 | git config --list
  ```

* 创建本地仓库

  ```pyhton
  1 | git init
  ```

  你需要在一个文件夹里创建一个本地仓库，在该文件夹里输入该命令。会出现如下信息：

  ```python
  # git bash cmd input
  (base) weianan@Andys-MacBook-Air ~ % mkdir dataset
  (base) weianan@Andys-MacBook-Air ~ % cd dataset
  (base) weianan@Andys-MacBook-Air dataset % mkdir gitset01 
  (base) weianan@Andys-MacBook-Air dataset % ls
  gitset01
  (base) weianan@Andys-MacBook-Air dataset % cd gitset01/
  (base) weianan@Andys-MacBook-Air gitset01 % git init
  # 提示信息：
  	hint: Using 'master' as the name for the initial branch. This default branch name
    hint: is subject to change. To configure the initial branch name to use in all
    hint: of your new repositories, which will suppress this warning, call:
    hint: 
    hint: 	git config --global init.defaultBranch <name>
    hint: 
    hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
    hint: 'development'. The just-created branch can be renamed via this command:
    hint: 
    hint: 	git branch -m <name>
    # 初始化完成！
    Initialized empty Git repository in /Users/weianan/dataset/gitset01/.git/
  ```
   * ###### 我们所有的工作文件都需要放在该文件目录下

##### 3.3 向本地仓库中添加文件

##### 3.4 查看历史版本

##### 3.5 版本的前进和后退

##### 3.6 删除本地库文件

##### 3.7 比较文件

### 4. 分支

### 5. 连接GitHub远程仓库



