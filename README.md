# BOMkit

打工精英们共同开发的库，提供 BOM 相关的工具
这个项目旨在通过构建一个物料清单（BOM）库，帮助练习 Python 编程和 GitHub 的使用

## 仓库使用的目标

1. 练习使用 GITHUB 协作进行软件开发
2. 代码编写实操，实现整洁的代码和架构
3. 做出一款真正能用的软件

## BOMkit 功能目标

1. 读取不同格式 BOM 数据（如 JSON,CSV,XLS,XLSX,TXT）
2. 对 BOM 信息进行增删改查
3. 导出 BOM 数据为不同格式

## 建议

1. 非必要不依赖其他库

## 文件夹的说明

bomlib/：存放库的核心代码，主要功能模块。
tests/：包含单元测试代码，确保库的功能正常。
docs/：用于存放文档，包括使用说明和开发者指南。
README.md：项目的简要说明，包括如何安装和使用。

## bomlib/主要文件职能

- \_\_init\_\_.py # 包的初始化文件

- core.py # 核心功能模块
  - class BOM # 物料清单管理类
  - class Item # 物料条目类

- utils.py # 辅助工具模块
  - function read_csv # 读取 CSV 文件的函数
  - function write_csv # 写入 CSV 文件的函数

- export.py # 导出功能模块
  - function export_to_json # 将 BOM 导出为 JSON 格式的函数

- import.py # 导入功能模块
  - function import_from_json # 从 JSON 文件导入 BOM 的函数
