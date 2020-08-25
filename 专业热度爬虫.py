import json
import requests
import time
import numpy as np
import pandas as pd
#每页获取数据
#https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=1&page=1&request_type=1&signsafe=&size=20&sort=view_total&uri=apidata/api/gk/special/lists
def get_gd_zyhot_one(page_num):
    url="https://api.eol.cn/gkcx/api/"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Origin':'https://gkcx.eol.cn',
        'Referer':'https://gkcx.eol.cn/hotschool?province=%E5%B9%BF%E4%B8%9C',
    }
    data={
        'access_token':"",
        'keyword':"",
        'level1':"1",
        'page':page_num,
        'request_type':1,
        'signsafe':"",
        'size':20,
        'sort':"view_total",
        'uri':"apidata/api/gk/special/lists",
    }
    try:
        response=requests.post(url=url,data=data,headers=headers)
    except Exception as gk:
        print(gk)
        time.sleep(3)
        response=requests.post(url=url,data=data,headers=headers)
    major_hot=json.loads(response.text)['data']['item']
    #专业昵称
    name=[i.get('name') for i in major_hot]
    # 专业类别
    marjor_lb = [i.get('level3_name') for i in major_hot]
    # 学科类别
    xk_type = [i.get('level2_name') for i in major_hot]
    #人气值
    rank_hot=[i.get('view_total') for i in major_hot]
    #专业修读年数limit_year
    limit_year=[i.get('limit_year') for i in major_hot]

    df=pd.DataFrame({
        '专业名称':name,
        '学科类别':xk_type,
        '专业类别':marjor_lb,
        '最少修读年数':limit_year,
        '人气值':rank_hot

    })
    return df
def get_all_page(all_page_num):
    df_all=pd.DataFrame()
    for i in range(all_page_num):
        print(f'正在读取第{i+1}页的数据')
        df_one=get_gd_zyhot_one(page_num=i+1)
        df_all=df_all.append(df_one,ignore_index=True)
        time.sleep(np.random.uniform(2))
    return df_all

showtable_sj=get_all_page(all_page_num=34)
showtable_sj.to_excel('./data/专业热度.xlsx',index=False)

