# 齐鲁工业大学 觅幂小程序打卡

操作有点复杂 不过一次操作 一直方便 系统不重启可以用两年 当然用模拟器也是可以的

用到的软件我都传到了 百度网盘 如果不放心软件 可以自行下载安装 其中的poc.exe 中有 .py源码 可以以源码形式运行 

还不会的可以联系我(有想学网安的也可以哦) 1498032121@qq.com 

```
链接：https://pan.baidu.com/s/1n87lwccvtU0EtjBditlJ6g?pwd=r4ru 
提取码：r4ru
```

首先我们需要先下载一个电脑版的微信

![image-20230406142347001](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/202304061646408.png)

我们首先需要安装 burpsuite

https://portswigger.net/burp/releases 可以去官网下载

一定要选择社区版

![image-20230406145907520](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406145907520.png)

![image-20230406150221885](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406150221885.png)

双击安装 一直下一步就行了

![image-20230406150418015](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406150418015.png)

没有给我们创建快捷方式 我们点击开始菜单打开

![image-20230406150452236](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406150452236.png)

![image-20230406150526007](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406150526007.png)

![image-20230406150535598](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406150535598.png)

![image-20230406150546307](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406150546307.png)

成功启动 接着我们 点击proxy 点击 intercept 接着点击 open brower 在打开的浏览器里面输入 打开一个网站之后 点击 ca certificate

```
http://burpsuite/
```

![image-20230406151624169](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406151624169.png)

接着我们双击 按照这个der

![image-20230406151747240](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406151747240.png)

![image-20230406151800222](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406151800222.png)

![image-20230406151846783](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406151846783.png)

接着点击完成 点是即可

安装 proxifier.exe 

双击proxifier.exe  安装一直下一步就行

![image-20230406154440723](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406154440723.png)

接着打开 proxifier  选择代理服务器

![image-20230406154818332](file:///D:/MyCtf/img/image-20230406154818332.png?lastModify=1680768738)

![image-20230406161440752](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406161440752.png)

依次填入即可

接着点击代理规则

![image-20230406161611882](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406161611882.png)

这里选择 直接连接 接着点击添加

![image-20230406161548981](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406161548981.png)

接着填入下面的域名 然后确定即可

```
admin.report.mestallion.com
```

![image-20230406161709116](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406161709116.png)

最后的代理规则

![image-20230406161925726](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406161925726.png)

接着我们来登录微信 

搜索觅幂并打开

![image-20230406154611874](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406154611874.png)

这样当我们打开 小程序的时候就能发现我们抓到了 admin.report.mestallion.com 这个域名下的包

我们需要点击proxy 点击 http history 接着我们只需要复制出来 token 的值就可以了

![image-20230406162259399](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406162259399.png)

比如我这里就是

```
c74c8e1aa5********6c86126e60c
```

接着我们打开token 这个文件然后填入信息

![image-20230406164517538](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406164517538.png)

接着双击poc.exe 即可 不要关闭窗口  之后我们每天双击 一个poc.exe 就可以了

![image-20230406164546649](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/image-20230406164546649.png)

如果对你有点用的话可以请我喝杯奶茶(*╹▽╹*)

<center class="half">
    <img src="https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/202304061700223.png" width="210"/>
    <img src="https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/_20220902205127.jpg" width="200"/>
</center>

