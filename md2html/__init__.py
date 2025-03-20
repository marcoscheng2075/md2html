import sys
import markdown
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def get_template_dir() -> Path:
    """
    获取模板目录的路径
    
    Returns:
        Path: 模板目录的路径
    """
    return Path(__file__).parent / 'templates'

def check_environment() -> bool:
    """
    检查运行环境和依赖
    
    Returns:
        bool: 环境检查是否通过
    """
    # 检查模板目录
    template_dir = get_template_dir()
    if not template_dir.exists():
        print("错误: 未找到模板目录")
        print("请确保已正确安装包：")
        print("uv pip install -e .")
        return False
    
    # 检查必要的依赖
    try:
        import markdown
        import jinja2
    except ImportError as e:
        print(f"错误: 缺少必要的依赖包: {str(e)}")
        print("请确保已安装所有依赖：")
        print("uv pip install -e .")
        return False
    
    return True

def convert_markdown_to_html(md_file: str | Path, output_dir: str | Path = "output") -> Path:
    """
    将 Markdown 文件转换为 HTML
    
    Args:
        md_file: Markdown 文件路径
        output_dir: 输出目录
    
    Returns:
        Path: 生成的 HTML 文件路径
    """
    # 检查环境
    if not check_environment():
        sys.exit(1)
    
    # 转换路径为 Path 对象
    md_path = Path(md_file)
    output_path = Path(output_dir)
    
    # 创建输出目录
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 读取 Markdown 文件
    md_content = md_path.read_text(encoding='utf-8')
    
    # 转换 Markdown 为 HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    
    # 设置 Jinja2 环境
    template_dir = get_template_dir()
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('base.html')
    
    # 生成 HTML
    title = md_path.stem
    html_output = template.render(
        title=title,
        content=html_content
    )
    
    # 保存 HTML 文件
    output_file = output_path / f"{title}.html"
    output_file.write_text(html_output, encoding='utf-8')
    
    return output_file

def main():
    if len(sys.argv) < 2:
        print("使用方法: md2html <markdown文件路径>")
        print("或者: python -m md2html <markdown文件路径>")
        sys.exit(1)
    
    md_file = Path(sys.argv[1])
    if not md_file.exists():
        print(f"错误: 文件 {md_file} 不存在")
        sys.exit(1)
    
    try:
        output_file = convert_markdown_to_html(md_file)
        print(f"转换成功！HTML 文件已保存到: {output_file}")
    except Exception as e:
        print(f"转换过程中出现错误: {str(e)}")
        sys.exit(1)

__all__ = ['main', 'convert_markdown_to_html']

if __name__ == "__main__":
    main()
