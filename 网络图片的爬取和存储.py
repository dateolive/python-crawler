'''
import requests
path="D:/abc.jpg"
url="http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg"
r=requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
f.close()
'''
import requests
import os
def httpimg(url):
    root='E://py项目//'
    path=root+url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print('文件已存在')
    except:
        print('爬取失败')
if __name__=="__main__":
    url=input()
    print(httpimg(url))