import os
import shutil
from pathlib import Path

def move_media_files(current_dir):
    # 支持的媒体文件扩展名
    media_exts = {'.png', '.jpg', '.gif'}
    
    # 遍历当前目录及其子目录
    for root, dirs, files in os.walk(current_dir, topdown=False):
        root_path = Path(root)
        
        # 处理每个文件
        for filename in files:
            file_path = root_path / filename
            ext = file_path.suffix.lower()
            
            # 检查是否是媒体文件或对应的meta文件
            is_media = ext in media_exts
            is_meta = file_path.suffixes[-2:] == [ext, '.meta']
            
            if is_media or is_meta:
                # 构建目标路径
                if is_meta:
                    # 获取对应的媒体文件名（去掉.meta后缀）
                    media_filename = file_path.stem
                    target_name = media_filename
                else:
                    target_name = filename
                
                # 生成唯一的目标路径
                target_path = Path(current_dir) / target_name
                counter = 1
                while target_path.exists():
                    stem = target_path.stem
                    suffix = target_path.suffix
                    # 处理带数字后缀的情况
                    if stem.endswith(f"_{counter-1}"):
                        stem = stem.rsplit("_", 1)[0]
                    target_path = Path(current_dir) / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                # 移动文件
                print(f"移动 {file_path} -> {target_path}")
                shutil.move(str(file_path), str(target_path))
                
                # 如果是媒体文件，尝试移动对应的meta文件
                if is_media:
                    meta_file = file_path.with_suffix(file_path.suffix + '.meta')
                    if meta_file.exists():
                        meta_target = target_path.with_suffix(target_path.suffix + '.meta')
                        print(f"移动 {meta_file} -> {meta_target}")
                        shutil.move(str(meta_file), str(meta_target))

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"开始整理目录：{current_dir}")
    move_media_files(current_dir)
    print("整理完成！")
