# 删除当前目录下 Output 文件夹 和 out.txt 文件
import os
import shutil

# 获取当前目录路径
current_dir = os.getcwd()

# 删除 Output 文件夹
output_path = os.path.join(current_dir, "Index")
if os.path.exists(output_path):
    try:
        shutil.rmtree(output_path)
        print(f"成功删除目录: {output_path}")
    except Exception as e:
        print(f"删除目录失败: {e}")

# 删除 out.txt 文件
txt_path = os.path.join(current_dir, "out.txt")
if os.path.exists(txt_path):
    try:
        os.remove(txt_path)
        print(f"成功删除文件: {txt_path}")
    except Exception as e:
        print(f"删除文件失败: {e}")
