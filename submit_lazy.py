#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import requests
import re
import os
import time
import random
import config_lazy as conf
from logger_Lib import logger

if __name__ == '__main__':
    try:
        if os.path.exists('xdncov_auto.log'):
            os.remove('xdncov_auto.log')
        logger.info(f'程序开始运行\n\tCreated by Lsr')
        while True:
            hour = int(time.strftime("%H"))
            if 8>hour>13:
                time.sleep(random.randint(30,75)*60+random.randint(0,55))
                logger.info('开始填报疫情通')
                for name_now,pswd_now in zip(conf.user_name,conf.user_pswd):
                    data = conf.data_generate()
                    conn = requests.Session()
                    result = conn.post('https://xxcapp.xidian.edu.cn/uc/wap/login/check',data={'username':name_now,'password':pswd_now})
                    if result.status_code != 200 or '操作成功' not in result.content.decode():
                        logger.error(f'登录失败 用户名 {name_now}')
                        continue
                    else:
                        logger.info(f'用户 {name_now} 登录成功')
                    result = conn.get('https://xxcapp.xidian.edu.cn/ncov/wap/default/index')
                    if result.status_code != 200:
                        logger.error(f'获取疫情通网页失败 用户名 {name_now}')
                        continue

                    if os.path.exists("last_get.html"):
                        os.rename("last_get.html","last_get.html.1")

                    with open("last_get.html","w") as fd:
                        fd.write(result.text)

                    predef = json.loads(re.search('var def = ({.*});',result.text).group(1))
                    try:
                        del predef['jrdqtlqk']
                        del predef['jrdqjcqk']
                    except:
                        pass
                    predef.update(data)
                    result = conn.post('https://xxcapp.xidian.edu.cn/ncov/wap/default/save',data=predef)
                    if '已经填报' in result.text:
                        logger.warning(f'用户 {name_now} 已经填报过本次疫情通')
                    elif '1' in result.text:
                        logger.error(f'用户 {name_now} 填报出错')
                        logger.error(f'==附加消息== \n{result.text}')
                    else:
                        logger.info(f'!Ha! 用户 {name_now} 成功填报本次疫情通 =======')
                    
                    #休眠以错开时间
                    time.sleep(random.randint(10,25)*60+random.randint(0,55))
            else:
                # 填报时间未到
                logger.info('alive')
                time.sleep(90*60)
    except KeyboardInterrupt:
        logger.info('程序手动退出 ... make exit()')
        exit(0)