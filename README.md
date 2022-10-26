# Auto_xray
因为懒所以写了一个菜鸡缝合怪,缝合fofa xray


# 使用
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
python3 Auto_xray -t 5 指定线程,默认10 -f urls.txt路径 -e True 开启邮件推送 -ff True
```

更多详细参数 --help
![](https://raw.githubusercontent.com/chencicici/images/main/202210262248211.png)