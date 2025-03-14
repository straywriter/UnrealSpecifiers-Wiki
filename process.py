import os
import re
import shutil
from pathlib import Path

def generate_directory_prefix(base_path, current_path):
    """生成基于路径结构的唯一前缀"""
    if base_path == current_path:
        return ""  # 根目录返回空前缀
    relative = current_path.relative_to(base_path)
    return f"{str(relative).replace(os.sep, '_')}_"

def generate_meta_file(file_path, base_path, global_rename_map, is_directory_file=False, original_parent_dir=None):
    """生成元数据文件（改进标签逻辑）"""
    if file_path.suffix.lower() == '.md':
        if is_directory_file:
            # 直接使用目录本身的相对路径
            current_dir = original_parent_dir if original_parent_dir else file_path.parent
            print(f"\n生成目录文件标签: {file_path.name}")
            print(f"当前目录: {current_dir}")
            print(f"基路径: {base_path}")
            
            try:
                dir_relative = current_dir.relative_to(base_path)
                dir_tag = "_".join(dir_relative.parts)
                print(f"相对路径计算成功: {dir_relative.parts} → 标签: {dir_tag}")
            except ValueError as e:
                print(f"路径计算异常: {str(e)}")
                print(f"使用目录名称作为标签: {current_dir.name}")
                dir_tag = current_dir.name
        else:
            # 获取原始文件名（通过反向查找重命名映射）
            original_name = next((k for k, v in global_rename_map.items() if v == file_path.name), file_path.name)
            original_stem = Path(original_name).stem
            
            print(f"\n生成普通文件标签: {file_path.name}（原始名称: {original_name}）")
            print(f"文件父目录: {file_path.parent}")
            print(f"基路径: {base_path}")
            
            parent_dir = file_path.parent

            # 使用原始文件名进行目录名比较
            if original_stem == parent_dir.name and parent_dir != base_path and parent_dir.parent != base_path:
                print(f"检测到原始文件名与目录名相同: {original_stem} == {parent_dir.name}")
                parent_dir = parent_dir.parent  # 使用祖父目录
                print(f"改用祖父目录路径: {parent_dir}")

            try:
                parent_relative = parent_dir.relative_to(base_path)
                dir_tag = "_".join(parent_relative.parts) if parent_relative.parts else ""
                print(f"相对路径计算成功: {parent_relative.parts} → 标签: {dir_tag}")
            except ValueError as e:
                print(f"路径计算异常: {str(e)}")
                dir_tag = ""
                print("使用空标签作为回退方案")
        
        meta_content = f"tags: {dir_tag}\ntitle: {file_path.stem}\ntype: text/x-markdown\n"
    elif file_path.suffix.lower() in ('.png', '.gif', '.jpg', '.jpeg'):
        file_type = {
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg'
        }[file_path.suffix.lower()]
        meta_content = f"tags: Image\ntitle: {file_path.name}\ntype: {file_type}\n"
    else:
        return

    meta_path = file_path.with_suffix(file_path.suffix + '.meta')
    with open(meta_path, 'w', encoding='utf-8') as f:
        f.write(meta_content)

def process_directory(base_path, dir_path, output_dir, global_rename_map, global_file_map, process_links=False):
    """处理目录的核心逻辑
    :param process_links: 是否处理链接（第二阶段处理）
    """
    # 在输出目录创建对应子目录
    relative_path = dir_path.relative_to(base_path)
    output_path = output_dir / relative_path
    
    if not process_links:  # 第一阶段只需要创建目录一次
        output_path.mkdir(parents=True, exist_ok=True)
    
    prefix = generate_directory_prefix(base_path, dir_path)
    rename_map = {}
    current_dir_map = {}


    if not process_links:  # 只在第一阶段处理文件复制
        # 图片文件处理（支持PNG和GIF）
        for img_file in (list(dir_path.glob("*.[pP][nN][gG]")) + 
                        list(dir_path.glob("*.[gG][iI][fF]")) + 
                        list(dir_path.glob("*.[jJ][pP][gG]")) +
                        list(dir_path.glob("*.[jJ][pP][eE][gG]"))):
            # 复制文件到输出目录
            dest_file = output_path / img_file.name
            dest_file.write_bytes(img_file.read_bytes())
            if img_file.name.startswith(prefix):
                continue

            old_meta = img_file.with_suffix(f'{img_file.suffix}.meta')
            if old_meta.exists():
                old_meta.unlink()

            # 替换文件名中的空格为下划线
            sanitized_name = img_file.name.replace(' ', '_')
            new_name = prefix + sanitized_name
            new_path = output_path / new_name
            
            counter = 1
            while new_path.exists():
                new_name = f"{prefix}{img_file.stem}_{counter}{img_file.suffix}"
                new_path = output_path / new_name
                counter += 1
            
            # 记录原始相对路径到新文件名的映射
            original_relative = img_file.relative_to(base_path).as_posix()
            global_rename_map[original_relative] = new_path.name
            
            dest_file.rename(new_path)
            rename_map[img_file.name] = new_path.name
            print(f"图片文件映射: {original_relative} => {new_path.name}")

    if not process_links:  # 只在第一阶段处理文件复制
        # MD文件处理
        for md_file in dir_path.glob("*.md"):
            # 复制文件到输出目录
            dest_file = output_path / md_file.name
            dest_file.write_bytes(md_file.read_bytes())
            # 生成调整后的前缀（当文件名与目录名相同时使用父目录，且不在根目录）
            if md_file.stem == dir_path.name and dir_path != base_path:
                adjusted_dir = dir_path.parent
                adjusted_prefix = generate_directory_prefix(base_path, adjusted_dir)
            else:
                adjusted_prefix = prefix
                
            if md_file.name.startswith(adjusted_prefix):
                continue

            old_meta = md_file.with_suffix('.md.meta')
            if old_meta.exists():
                old_meta.unlink()

            new_name = adjusted_prefix + md_file.name
            new_path = output_path / new_name
            
            counter = 1
            while new_path.exists():
                new_name = f"{adjusted_prefix}{md_file.stem}_{counter}{md_file.suffix}"
                new_path = output_path / new_name
                counter += 1
            
            dest_file.rename(new_path)
            rename_map[md_file.name] = new_path.name
            global_file_map[md_file.name] = new_path.name  # 添加到全局文件映射
            # 记录全局路径映射（相对根目录的原始路径 -> 新文件名）
            original_relative = md_file.relative_to(base_path)
            # 统一使用POSIX路径格式（正斜杠）
            posix_path = original_relative.as_posix()
            global_rename_map[posix_path] = new_path.name
            current_dir_map[str(original_relative)] = new_path.name

    # 如果是链接处理阶段且不需要处理链接，则直接返回
    if process_links:
        # Markdown内容更新（仅处理图片引用）
        for md_file in output_path.glob("*.md"):
            print(f"\n处理文件: {md_file}")
            with open(md_file, 'r+', encoding='utf-8') as f:
                content = f.read()
                original_content = content
                modified = False
            
                # 初始化当前文件的替换统计
                link_replacements = {}
                
                # 处理图片引用
                def replace_image_link(match, decoded_path):
                    alt_text = match.group(1)
                    img_path = decoded_path.replace('%20', ' ')  # 使用解码后的路径
                    print(f"\n发现图片链接: {img_path}")
                    
                    try:
                        # 获取当前Markdown文件的原始目录路径
                        original_md_dir = md_file.parent.relative_to(output_dir)
                        original_base_dir = base_path / original_md_dir
                        
                        # 构建原始图片的完整路径
                        original_img_path = (original_base_dir / img_path).resolve().relative_to(base_path).as_posix()
                        
                        # 查找映射表
                        new_img_name = global_rename_map.get(original_img_path)
                        
                        if new_img_name:
                            print(f"图片路径映射: {original_img_path} => {new_img_name}")
                            return f'![{alt_text}]({new_img_name})'
                            
                    except Exception as e:
                        print(f"解析图片路径失败: {str(e)}")
                    
                    print(f"保留原始图片链接: {img_path}")
                    return match.group(0)
                
                # 解码URL编码的路径并处理空格
                from urllib.parse import unquote
                
                # 使用正则匹配所有图片链接（支持PNG和GIF），并解码URL编码字符
                content, count = re.subn(
                    r'!\[([^\]]*)\]\(([^\)]+)\)',  # 匹配所有图片链接
                    lambda m: replace_image_link(m, unquote(m.group(2))),  # 解码URL编码后传递
                    content,
                    flags=re.IGNORECASE
                )
                if count > 0:
                    modified = True
                    print(f"共替换 {count} 个图片链接")

                # 打印当前文件的替换汇总
                if link_replacements:
                    print(f"\n文件 {md_file.name} 图片链接替换汇总:")
                    print(f"总替换数: {sum(link_replacements.values())}")
                    for (orig, new), cnt in link_replacements.items():
                        print(f"  · 替换 {orig} => {new} : {cnt} 次")
                    print(f"共完成 {len(link_replacements)} 种不同的图片链接替换")

                # 处理Markdown内部链接
                def replace_link(match):
                    link_text = match.group(1)
                    relative_path = match.group(2)
                    anchor = match.group(3) or ''
                    original_link = match.group(0)
                    
                    print(f"\n匹配到链接: {original_link}")
                    try:
                        # 解析原始文件的绝对路径（规范化路径处理）
                        print(f"原始相对路径: {relative_path}")
                        source_path = md_file.parent.resolve()
                        try:
                            # 先尝试直接解析路径
                            target_path = (source_path / relative_path).resolve()
                            print(f"解析后绝对路径: {target_path}")


                        except FileNotFoundError:
                            # 如果文件不存在，尝试通过路径结构匹配
                            try:
                                normalized_path = Path(relative_path).as_posix().replace('../', '')
                                matches = [k for k in global_rename_map.keys() if k.endswith(normalized_path)]
                                
                                if matches:
                                    relative_to_base = Path(matches[0])
                                    new_name = global_rename_map[str(relative_to_base)]
                                    new_stem = Path(new_name).stem
                                    new_link = f'[{link_text}](#{new_stem}{anchor})'
                                    print(f"通过规范化路径匹配: {original_link} => {new_link}")
                                    return new_link
                                    
                                print(f"未找到匹配路径: {normalized_path}")
                                return match.group(0)
                                
                            except Exception as e:
                                print(f"路径规范化异常: {str(e)}")
                                return match.group(0)
                        
                        # 处理当前文件相对路径
                        try:
                            # 计算原始项目中的正确路径（考虑多级父目录）
                            # 获取当前输出文件对应的原始目录
                            original_output_rel = md_file.parent.relative_to(output_dir)
                            original_source_dir = base_path / original_output_rel
                            
                            # 解析相对路径（支持多级../）
                            target_path = (original_source_dir / relative_path).resolve()
                            
                            # 转换为相对于项目根目录的路径并使用POSIX格式
                            original_path = target_path.relative_to(base_path).as_posix()
                        except (ValueError, FileNotFoundError) as e:
                            print(f"路径转换失败: {str(e)}")
                            # 回退方案：尝试逆向推导原始路径
                            try:
                                # 从输出目录结构反推原始路径
                                original_path = relative_path.relative_to(*relative_path.parts[:4]).as_posix()
                            except ValueError:
                                original_path = relative_path.as_posix()
                        
                        # 清理特殊符号
                        original_path = original_path.replace('./', '')
                        print(f"规范化的原始路径: {original_path} | 当前文件原始位置: {original_output_rel}")
                        # 尝试获取映射并打印调试信息
                        new_name = global_rename_map.get(original_path)
                        print(f"查找映射表: {original_path} => {new_name or '未找到'}")
                        
                        # if not new_name:
                        #     print("\n当前全局重命名映射表:")
                        #     for k, v in global_rename_map.items():
                        #         print(f"{k} => {v}")
                        #     raise SystemExit("终止程序：未找到路径映射")
                        
                        if new_name:
                            new_stem = Path(new_name).stem
                            new_link = f'[{link_text}](#{new_stem}{anchor})'
                            print(f"映射关系: {original_path} => {new_name}")
                            print(f"直接路径替换: {original_link} => {new_link}")
                            return new_link
                    except ValueError as e:
                        print(f"路径解析异常: {str(e)}")
                    print(f"保留原始链接: {original_link}")
                    return match.group(0)

                # 先处理普通链接（排除图片链接）
                content = re.sub(
                    r'(?<!\!)\[([^\]]+)\]\(((?:[^)]+?))(?:#([^)]+))?\)',  # 使用否定回溯匹配非图片链接
                    replace_link,
                    content,
                    flags=re.IGNORECASE
                )

                # 只有内容变化时才写回
                if modified or content != original_content:
                    f.seek(0)  # 重置文件指针到开头
                    f.write(content)
                    f.truncate()  # 截断剩余内容


    # 生成元数据（使用输出目录作为基路径）
    if not process_links:  
        for file in output_path.glob("*"):
            if file.suffix.lower() in ('.md', '.png', '.gif', '.jpg', '.jpeg'):
                generate_meta_file(file, output_dir, global_rename_map)

    # 最后生成目录文件（确保不会覆盖现有文件）
    if not process_links and dir_path != base_path:  # 跳过根目录
        # 生成目录文件名（使用相对路径结构）
        relative_dir = dir_path.relative_to(base_path)
        dir_filename = f"{str(relative_dir).replace(os.sep, '_')}.md"
        dir_filepath = output_path / dir_filename
        
        # 仅在文件不存在时创建
        if not dir_filepath.exists():
            dir_filepath.touch()
            # 使用原始目录路径生成标签
            original_parent_dir = dir_path.parent
            generate_meta_file(dir_filepath, base_path, global_rename_map, is_directory_file=True, original_parent_dir=original_parent_dir)
            print(f"创建目录文件: {dir_filename}")

def main():
    root_path = Path.cwd()
    output_dir = root_path / "Index"
    global_rename_map = {}  # 路径映射
    global_file_map = {}    # 文件名映射
    
    # 清空并创建输出目录
    if output_dir.exists():
        for f in output_dir.glob("*"):
            if f.is_file():
                f.unlink()
            elif f.is_dir():
                shutil.rmtree(f)
    output_dir.mkdir(exist_ok=True)
    
    print(f"开始处理根目录：{root_path}")

    # 先处理子目录再处理根目录
    dirs = sorted([d for d in root_path.rglob("*") if d.is_dir() and d != output_dir], 
                 key=lambda x: len(x.parts), reverse=True)
    dirs.append(root_path)  # 最后处理根目录
    
    # 第一阶段：生成全局映射表
    for dir_path in dirs:
        process_directory(root_path, dir_path, output_dir, global_rename_map, global_file_map)
        
    # 打印全局重命名映射表
    # 打印图片专用映射表
    print("\n图片文件映射表:")
    png_mappings = {k: v for k, v in global_rename_map.items() if k.endswith('.png')}
    for orig_path, new_name in png_mappings.items():
        print(f"{orig_path.ljust(60)} => {new_name}")
    
    print("\n全局重命名映射表:")
    for orig_path, new_name in global_rename_map.items():
        if not orig_path.endswith('.png'):  # 过滤掉非图片的映射
            print(f"{orig_path} => {new_name}")
    
    # 第二阶段：处理所有链接（使用完整的全局映射表）
    print("\n开始处理所有Markdown文件链接...")
    for dir_path in dirs:
        process_directory(root_path, dir_path, output_dir, global_rename_map, global_file_map, process_links=True)


    # 处理README文件
    readme = root_path / "README.md"
    if readme.exists():
        dest_readme = output_dir / "README.md"
        dest_readme.write_bytes(readme.read_bytes())
        generate_meta_file(dest_readme, output_dir, global_rename_map)

    print(f"处理完成 ✓ 输出目录：{output_dir}")

if __name__ == "__main__":
    main()