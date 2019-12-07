# autoApiTestExample
a simple Example for api autotest

#### 一个简单的API自动化测试的项目，可以快速学习回忆一个API自动化测试项目的开发模式。

python3.6 + requests + unittest + BeautifulReport + pymsql + parameterized



### 项目依赖

项目启动依赖，由于导出环境配置前用的是全局配置，所以会多一些与项目无关的依赖包

```
pip install -r requirements.txt
```



依赖包单独安装的话都有以下这些：

```
pip install pymysql
pip install requests
pip install parameterized
```



生成测试报告还需要依赖第三方BeautifulReport

BeautifulReport的下载与使用，请参考<https://github.com/TesterlifeRaymond/BeautifulReport> 

在上面的链接将源码拉下来，解压后修改目录名为BeautifulReport，

将整个目录放置python目录的/lib/site-packages/ 目录下 就可以使用了



#### 项目运行

项目目录下在终端中运行下面命令

```
python run_suite.py
```

生成的测试报告保存在report文件夹中



#### 目录结构

![目录结构](https://github.com/1chott/autoApiTestExample/blob/master/%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)
