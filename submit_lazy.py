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
        logger.info(f'程序开始运行 pid={os.getpid()}\n\tCreated by Lsr')
        task_tick = 1
        while True:
            hour = int(time.strftime("%H"))
            if 8<=hour<=13:
                if task_tick > 0:
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
                            logger.info(f'== 用户 {name_now} 成功填报本次疫情通 ==')
                            logger.info(f'{data["address"]} {data["tw"]}    {data["geo_api_info"]}')
                        
                        #休眠以错开时间
                        time.sleep(random.randint(10,25)*60+random.randint(0,55))
                    logger.info('填报结束')
                else:
                    task_tick = 0 # 今天填报完成了
            else:
                # 填报时间未到
                task_tick = task_tick+1
                if task_tick%4 == 1:
                    logger.info('alive')
                time.sleep(25*60)
    except KeyboardInterrupt:
        logger.info('程序手动退出 ...')
        exit(0)
    except Exception as exc:
        logger.error(f"{exc}")
        exit(1)