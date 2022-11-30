#删除文件夹下面的所有文件(只删除文件,不删除文件夹)
import os
#python删除文件的方法 os.remove(path)path指的是文件的绝对路径,如：
def del_file(path_data):
    for i in os.listdir(path_data) :# os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "/" + i#当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)

def main():
    path_data1 = r"./static/uploads"
    path_data2 = r"./static/downloads"
    del_file(path_data1)
    del_file(path_data2)
    print("缓存清理完毕！")