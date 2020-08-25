import json
import requests
import time
import numpy as np
import pandas as pd
#每页获取数据
#https://api.eol.cn/gkcx/api/?access_token=&keyword=&page=1&province_id=44&school_type=&signsafe=&size=20&sort=view_total&sorttype=desc&type=&uri=apidata/api/gk/school/lists
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
        'page':page_num,
        'province_id':44,
        'school_type':"",
        'signsafe':"",
        'size':20,
        'sort':"view_total",
        'sorttype':"desc",
        'type':"",
        'uri':"apidata/api/gk/school/lists",
    }
    try:
        response=requests.post(url=url,data=data,headers=headers)
    except Exception as gk:
        print(gk)
        time.sleep(3)
        response=requests.post(url=url,data=data,headers=headers)
    major_hot=json.loads(response.text)['data']['item']
    #高校昵称
    name=[i.get('name') for i in major_hot]
    print(name)
    # 热度排名
    rank = [i.get('rank') for i in major_hot]
    # 高校类别
    type = [i.get('type_name') for i in major_hot]
    #高校热度
    rank_hot=[i.get('view_total') for i in major_hot]

    df=pd.DataFrame({
        '广东高校名称':name,
        '热度总排名':rank,
        '高校类别':type,
        '高校热度量':rank_hot

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

showtable_sj=get_all_page(all_page_num=9)
showtable_sj.to_excel('./data/广东高考大学热度.xlsx',index=False)

