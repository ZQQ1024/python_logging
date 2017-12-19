# encoding=UTF8
import logging
import time


# #first step：直接输出
#
# logging.debug("display debug")
# logging.info("display info")
# logging.warning("display warning")
# logging.error("display error")
# logging.critical("display critical")

# WARNING:root:display warning
# ERROR:root:display error
# CRITICAL:root:display critical
# 默认输出到控制台，默认级别为WARNING。

# #second step：basicConfig
# second = str(int(time.time()))
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)s %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='identify.log',
#                     filemode='w') #a or w
# logging.debug("basicConfig debug")
# logging.error("basicConfig error")

#调用basicConfig其实是给root logger添加了一个handler，经测试之前有了就失效了。
#这样当你的程序和别的使用了 logging的第三方模块一起工作时，会影响第三方模块的logger行为。
#这是由logger的继承特性决定的。

# #third step：为了解决上述问题,学习Logger、Handler（Filter、Formatter）
logger = logging.getLogger() #root

#定义handler、formatter，决定输出位置和输出格式
fh = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filter = logging.Filter('mylogger')  #所有孩子的能显示的
fh.addFilter(filter)
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.error('Handler error')

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)


logger2 = logging.getLogger('mylogger.child') #会继承所有父类的handler、level等

logger1.error('logger1')
logger2.debug('child debug')

# # 是一个树状结构
# # Logger       对象提供应用程序可直接使用的接口，
# # Handler      发送日志到适当的目的地，
# # Filter       提供了过滤日志信息的方法，只显示什么，
# # Formatter   指定日志显示格式。
# # http://blog.csdn.net/z_johnny/article/details/50740528

#基本知识就完了。

##其他：
#1.将配置写到配置文件里

#2.多模块使用：
#在同一个python解释器内调用多次调用logging.getLogger('log_name')都会返回同一个logger实例，
#即使是在多个模块的情况下。其实这样设计就是方便多模块使用日志。
#在一个模块里初始化，其他模块使用这个logger就行了，使用返回的，或者直接getLogger
