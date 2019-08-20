import os
import pandas as pd
import numpy as np

allpath=[]
allname=[]

def getallfile(path):
    allfilelist=os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath=os.path.join(path,file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname


if __name__ == "__main__":
    rootdir = "D:\\实验室工作\\整理后报表"
    files, names = getallfile(rootdir)
    for file in files:
        print(file)
    content_list = []
    for f in files:
        content_list.append(f.split('\\'))
    content_list_new = []
    for con in content_list:
        con[-1] = os.path.splitext(con[-1])[0]
        content_list_new.append(con[4:])
print(content_list_new)
df = pd.DataFrame(content_list_new)
df.to_csv('zhongjiao.csv',encoding='gbk',index = False)