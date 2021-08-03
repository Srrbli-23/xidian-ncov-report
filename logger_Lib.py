#!/usr/bin/python3
import os
import platform
import logging
import logging.handlers
"""
从主函数中引用
logger_libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'logger_Lib')
sys.path.append(libdir)
"""

LOG_FORMAT="[%(asctime)s] - %(levelname)s\t: %(message)s"
LFILE_NAME="xdncov_auto.log"

logger = logging.getLogger('NetworkLogger')
logger.setLevel(logging.DEBUG)

def logger_init():
    global logger
    if platform.platform().lower().find('linux') >= 0:
        f_sysinfo = os.popen('uname -a').read()
        if f_sysinfo.find('arm') >= 0 or f_sysinfo.find('aarch64')>=0:
            #说明此时是树莓派系统
            logger_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(logger_dir,LFILE_NAME)

        elif f_sysinfo.find('x86_64') >= 0:
            #说明此时是PC机 , 测试文件放在当前文件夹下
            logger_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(logger_dir,LFILE_NAME)
            
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(logging.Formatter('%(message)s'))
            logger.addHandler(ch)
        if os.path.exists(file_path):
            os.remove(file_path) #删除历史遗留的记录
        fd = logging.handlers.RotatingFileHandler(file_path,mode="a",maxBytes=10*(10**6),backupCount=2)
        fd.setLevel(logging.INFO)
        fd.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(fd)

    elif platform.platform().lower().find('windows') >= 0:
        #windows 平台下 (专门给wcc准备的)

        logger_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(logger_dir,'middleware.log')
        #file_path = 'win_middleware.log'
        print('path =',file_path)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(ch)
        fd = logging.FileHandler(file_path)
        fd.setLevel(logging.INFO)
        fd.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(fd)
    else:
        file_path = None 

logger_init()

if __name__ == "__main__":
    logger.info('===测试程序===')
    print(logger)
    logger.info('info test')
    logger.warning('warning test')
    logger.error('error test')
    for i in range(0,120000):
        logger.info('RotatingFileHandler test')
        logger.info('WCC YYDS')
    pass