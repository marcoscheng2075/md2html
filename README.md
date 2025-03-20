# Markdown 转 HTML 工具

这是一个简单但功能强大的 Markdown 转 HTML 工具，可以将 Markdown 文件转换为美观的 HTML 页面。最新版本 0.2.0 采用了莫兰迪风格设计，提供更优雅的阅读体验。

作者：Marcos Cheng

## 功能特点

- 支持标准 Markdown 语法
- 支持表格、代码块等扩展语法
- 响应式设计，适配各种屏幕尺寸
- 莫兰迪风格设计，提供优雅的阅读体验
- 支持代码高亮
- 支持中文编码

## 安装说明

### 前置要求

- Python 3.12 或更高版本
- uv 包管理工具

### 安装步骤

1. 克隆项目：
   ```bash
   git clone <项目地址>
   cd <项目目录>
   ```

2. 创建并激活虚拟环境：
   ```bash
   uv venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. 安装项目依赖：
   ```bash
   uv pip install -e .
   ```

## 使用方法

### 方式一：使用批处理文件（推荐）

直接运行批处理文件，它会自动处理虚拟环境：
```bash
.\md2html <markdown文件路径>
```

### 方式二：通过 Python 模块运行

1. 首先激活虚拟环境：
   ```bash
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

2. 然后运行转换命令：
   ```bash
   python -m md2html <markdown文件路径>
   ```

注意：如果不激活虚拟环境直接运行 `python -m md2html`，程序会显示警告信息，但仍可能继续运行（取决于系统环境配置）。建议始终在虚拟环境中运行以确保所有依赖都可用。

### 方式三：作为系统命令使用

安装后可以直接使用：
```bash
md2html <markdown文件路径>
```

3. 查看结果：
   - 转换后的 HTML 文件将保存在 `output` 目录下
   - 文件名与输入的 Markdown 文件名相同，但扩展名改为 `.html`

## 项目结构

```
project/
├── md2html/            # 主程序包
│   ├── __init__.py    # 包初始化文件
│   └── __main__.py    # 程序入口点
├── templates/          # HTML 模板目录
│   └── base.html      # 基础 HTML 模板
├── output/            # 输出目录
├── .venv/             # 虚拟环境目录
├── pyproject.toml     # 项目配置文件
├── .gitignore         # Git 忽略配置
├── .python-version    # Python 版本配置
├── md2html.bat        # Windows 批处理入口
└── README.md          # 项目说明文档
```

## 配置说明

### 依赖管理

项目依赖定义在 `pyproject.toml` 文件中：
```toml
[project]
name = "md2html"
version = "0.1.0"
dependencies = [
    "markdown>=3.5.2",
    "jinja2>=3.1.3",
]
```

### 样式定制

可以通过修改 `templates/base.html` 文件中的 CSS 来自定义输出页面的样式。

## 开发说明

### 虚拟环境管理

- 激活虚拟环境：
  ```bash
  .\.venv\Scripts\activate  # Windows
  source .venv/bin/activate  # Linux/Mac
  ```

- 退出虚拟环境：
  ```bash
  deactivate
  ```

### 添加新功能

1. 在 `md2html` 目录下添加新的 Python 模块
2. 在 `__init__.py` 中导出新功能
3. 更新 `pyproject.toml` 中的依赖（如果需要）

## 常见问题

1. **找不到模块**
   - 确保已激活虚拟环境
   - 确保已安装所有依赖

2. **中文显示问题**
   - 确保 Markdown 文件使用 UTF-8 编码
   - 确保系统支持中文显示

3. **样式问题**
   - 检查 `templates/base.html` 中的 CSS 配置
   - 确保浏览器支持使用的 CSS 特性

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License
