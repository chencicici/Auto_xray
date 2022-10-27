# Auto_xray
因为懒所以写了一个菜鸡缝合怪,缝合fofa xray

和fofa2xray差不多,但是我自己在mac端使用fofa2xray体验不是很好,mac端也调用cmd -c,应该是作者调试的时候忘记改了,同时挂服务器上经常跑着跑着就卡住了没反应,不知道是不是我没配置好,索性自己造了个轮子

建议部署在linux上,因为windows上的路径文件名和编码可能会导致文件保存出错和乱码

# 使用
自带 mac版的xray1.9.3,其他系统自行替换

支持直接使用xray多线程批量扫描指定url列表文件和fofa语法寻找目标扫描需要配置fofa.py中的邮箱 key 搜索语法
![](https://raw.githubusercontent.com/chencicici/images/main/202210262249314.png)

扫描完成后邮件提醒.需要配置my_email.py中的邮件地址和key
![](https://raw.githubusercontent.com/chencicici/images/main/202210262250753.png)


## 1.
直接扫描url列表
```bash
python3 Auto_xray -t 5 指定线程,默认10 -f urls.txt路径 -e True 开启邮件推送
```

## 2.
使用fofa批量抓取目标
```bash
python3 Auto_xray -t 5 指定线程,默认10 -f urls.txt路径 -e True 开启邮件推送 -ff True 开启fofa批量
```

## 3.
部署到后台持久化
```bash
sudo nohup python3 ./Auto_xray.py  -e True  -ff True &  
```

更多详细参数 --help
![](https://raw.githubusercontent.com/chencicici/images/main/202210262248211.png)

一些默认配置可以修改
![](https://raw.githubusercontent.com/chencicici/images/main/202210262341074.png)
