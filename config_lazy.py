#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import random

user_name = ["16020110001"]
user_pswd = ["samplepasswordofDemo"]

random.seed()


def geo_generate(select):
    if select==0:
        #98号公寓附近
        Q_range = (34.231275,34.231563)
        R_range = (108.914175,108.914661)
        address = "陕西省西安市雁塔区电子城街道西安电子科技大学北校区学生公寓西区98号"
    elif select==1:
        # 科技楼附近
        Q_range = (34.23134,34.230407)
        R_range = (108.918463,108.91821)
        address = "陕西省西安市雁塔区电子城街道西安电子科技大学科技楼"
    elif select==2:
        # 操场附近
        Q_range = (34.233094,34.231362)
        R_range = (108.920035,108.918649)
        address = "陕西省西安市雁塔区电子城街道西安电子科技大学北校区足球场"
    elif select==3:
        # 主楼附近
        Q_range = (34.234819,34.232729)
        R_range = (108.917716,108.919507)
        address = "陕西省西安市雁塔区电子城街道西安电子科技大学计算机学院"
    else:
        # 教学楼
        Q_range = (34.232796,34.23184)
        R_range = (108.917641,108.921043)
        address = "陕西省西安市雁塔区电子城街道西安电子科技大学北校区教学楼"
    Q_now = str(random.uniform(Q_range[0],Q_range[1]))[0:15] #34
    R_now = str(random.uniform(R_range[0],R_range[1]))[0:16] #108
    lng_now = R_now[0:10]
    lat_now = Q_now[0:9]
    return (Q_now,R_now,lng_now,lat_now,address)

def data_generate():
    Q_now,R_now,lng_now,lat_now,address_now = geo_generate(random.randint(0,4))
    tw_now = random.randint(1,2)
    data = {\
        'sfzx': 1,
        'fxyy': '', 
        'geo_api_info': f'{{"type":"complete","position":{{"Q":{Q_now},"R":{R_now},"lng":{lng_now},"lat":{lat_now} }},"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":40,"isConverted":true,"status":1,"addressComponent":{{"citycode":"029","adcode":"610113","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"光华路","streetNumber":"81号","country":"中国","province":"陕西省","city":"西安市","district":"雁塔区","township":"电子城街道"}},"formattedAddress": "{address_now}","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}}', 
        'address': f'"{address_now}"', 
        'area': '陕西省 西安市 雁塔区', 
        'province': '陕西省', 
        'city': '西安市', 
        'ismoved': 0, 
        'bztcyy': '', 
        'zgfxdq': 0, 
        'tw': f'{tw_now}', 
        'sfcxtz': 0, 
        'sfyyjc': 0, 
        'jcjgqr': 0, 
        'jcjg': '', 
        'sfjcbh': 0, 
        'jcbhlx': '', 
        'jcbhrq': '', 
        'mjry': 0, 
        'csmjry': 0, 
        'sfjcjwry': 0, 
        'sfcyglq': 0, 
        'gllx': '', 
        'glksrq': '', 
        'sfcxzysx': 0, 
        'qksm': '', 
        'remark': ''
    }
    return data

if __name__=="__main__":
    print(data_generate())