# 觅幂小程序打卡 Docker容器
***在此感谢wanan0red大佬的项目[qlu_mimi_sport](https://github.com/wanan0red/qlu_mimi_sport)，使用此项目打包为docker镜像便于服务器部署*** 
## 构建镜像
```shell
docker build -t="hhhhpaa/nimi_sport:1.0" .
```
## 运行容器
***映射目录为镜像构建目录，这里也可以不做映射***
```shell
docker run -id --name=Nimi_sport -v $PWD:/root/nimi_sport hhhhpaa/nimi_sport:1.0
```