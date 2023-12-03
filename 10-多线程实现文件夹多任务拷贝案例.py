import os
from threading import Thread


def copy_file(file_name, sourceDir, destDir):
    # 1.拼接源文件路径和目标文件路径
    source_path = sourceDir + '/' + file_name
    dest_path = destDir + '/' + file_name
    with open(source_path, 'rb') as source_file:
        with open(dest_path, 'wb') as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1.定义源文件夹和目标文件夹
    source_dir = 'C:/Users/admin/Desktop/知识图谱/paper/KnowledgeGraphCourse-master'
    dest_dir = 'C:/Users/admin/Desktop/知识图谱/paper/KnowledgeGraphCourse-master/copy'
    try:
        os.mkdir(dest_dir)
    except NameError:
        print('文件夹已存在')
    for file in os.listdir(source_dir):
        copy_thread = Thread(target=copy_file, args=(file, source_dir, dest_dir))
        copy_thread.start()
