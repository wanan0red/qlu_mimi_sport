FROM python:3.8.12
WORKDIR /root/nimi_sport
COPY  main.py requirements.txt ./
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip3 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python","./main.py"]
