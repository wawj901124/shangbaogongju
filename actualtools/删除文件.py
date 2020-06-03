
import os

file_name_full_path = "D:\pycharmproject\shangbaogongju\media/Dev/1_哈希分析仪/哈希分析仪.dev"
is_exist = os.path.exists(file_name_full_path)
if is_exist:  # 如果存在，则删除文件
    os.remove(file_name_full_path)
    print("删除文件")