***
# OpenCV-Python环境创建
* ##### 源码编译

* ##### pip命令

## 方法一、编译源码
​		最近打算学习一下Opencv，就去官网下了最新版的opencv-python的安装文件。说是安装文件，其实是个自解压缩文件，解压完后需要手动复制相关文件到指定的位置。OpenCV本身是用C++写的，但支持python绑定，所以我也只是打算在Python下学习OpenCV。官方的安装包里面只有针对Python2.7的预编译包，而我使用的是python3.9.3，这使我怀疑OpenCV只支持Python2系列，多少有点郁闷，用惯了Python3就不想用回到Python2了，但上网一查得知，OpenCV从3.0系列就支持Python3了，只是官方的预编译包没有自带而已，需要用户亲自编译，真的是郁闷...
​		我是在Anaconda下用的Python，所以就想Anaconda会不会带有OpenCV，但查了一下，结果是没有的。又上网查了下，发现pip可以安装Opencv的Python版本
(https://pypi.python.org/pypi/opencv-python)，于是就在Anaconda的命令行下输入：

> pip install opencv-python

​		这里的"安装"倒是顺利（其实也只是复制一个预编译包到Pyhton目录），但在Python中用```***import***```命令的话就会出现"未找到dll文件"的错误。上网查了下这个问题，很多回答是未安装Visual C++ 2015运行时导致的，可是我已经安装了Visual Studio 2015，所以不是这个方面的dll找不到。于是我用Dependency Walker工具查了下OpenCV的Pyhton模块（cv2.cp39-win_amd64.pyd)，发现它需要一个名为"Pyhton3.dll"的库文件。开始我以为Pyhton3.dll同Python39.dll是等价的，但把Python39.dll复制一份并把文件名改为Python3.dll以后，在Python中导入OpenCV时Pyhton会崩溃，看起来这个预编译包做得并不好，它引用了一个在正常安装中不会出现的dll文件。
​		PIP的方式无法安装后就只好回到编译OpenCV源文件的老路上了。OpenCV源文件是用CMake构建的，这还算比较方便。下载并安装好CMake，在cmake-gui中设定好文件目录和一下选项后进行"Configure"。这里又遇到一个蛋疼的问题，CMake在Configure中需要下载ffmpeg的dll，可是这一步总是"网络超时"，查看CMake配置的源文件，也找不到能直接下到该dll的网址。网上有人说可以到OpenCV的GitHub主页上下载，可我在OpenCV的GitHUb主页上并没看到有这个dll的下载。又网上搜了半天，发现OpenCV的GitHub上还有一个名为***opencv_3rdparty***的目录，在该目录下的"Branch"里选择***ffmpeg/master_"当前版本日期"***，然后进入```ffmpeg```目录就留意看到opencv_ffmpeg.dll和opencv_ffmpeg.dll两个文件了，从这里可以直接下载。下载后将文件复制到OpenCV源代码目录中的相应的位置，按CMake的配置要求，需要在"3rdparty/ffmpeg/dowloads"目录下建立以各个文件MD5码为名为目录，并把相应的文件复制进去。接下来还有一个需要下载的模块ippicv也是同理。
​		解决好了以上两个模块的下载问题,后面的构建和编译过程就十分的顺利了,生成的OpenCV-Python模块可以在Pyhton3,9环境下正常导入使用。

* ```python
  $python
  >>>import cv2
  ```

***

 ## 方法二、国内镜像安装opencv(pyhton)(国内pip镜像源)

* 偶尔网络爆炸，几十兆都下载不下来......，知道为什么你的下载速度犹如乌龟一样慢吗？嘿嘿..，pip的时候默认使用域外地址下载的第三方库，解决方法有两种：

  1. 使用代理，拥有域外冲浪环境；
  
  2. 将域外地址修改成国内地址，国内的pip源，如下：
  
     * 阿里云 [http://mirrors.aliyun.com/pypi/simple/](http://mirrors.aliyun.com/pypi/simple/)
     * 中国科技大学 [https://pypi.mirrors.ustc.edu.cn/simple/](https://pypi.mirrors.ustc.edu.cn/simple/)
     * 豆瓣(douban) [http://pypi.douban.com/simple/](http://pypi.douban.com/simple/)
     * 清华大学 [http://pypi.douban.com/simple/](http://pypi.douban.com/simple/)
     * 中国科学技术大学 [http://pypi.douban.com/simple/](http://pypi.douban.com/simple/)
     

在python中安装包出现Retrying(Retry(total=4,connect=None,read=None,redirect=None,status=None)

*  > ```pip install opencv-contrib-python -i https://pypi.mirrors.ustc.edu.cn/simple```

* #### 解决方法：
	 > ``` pip install keras -r https://pypi.douban.com/simple --trusted-host pypi.dpuban.com```
	
    	(其中的keras是需要自己下载的，根据自己需求自行更改)
    	例：
    	
    	> ```pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/```

