# coding=utf8
'''爬虫操作类

    包含了爬虫需要的基本操作.
    逐渐添加的功能如下:
    1, 获取某个格式的连接----function-getFormatURLFrom in filterelems.py
    2, 获取最长子串---function-getMaxLengthSubStringBetween in funcs.py
    3, 保存访问过的连接, 保证不会访问到重复的连接----class-HrefSet in datamodels.py
    4, 控制线程, 激发多线程访问, 并且保持稳定-----class-ControlThread in datamodels.py
'''