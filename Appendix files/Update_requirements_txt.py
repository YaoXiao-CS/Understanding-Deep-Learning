"""
导出的项目requirements.txt文件包含有一些额外信息,示例如下：
platformdirs @ file:///C:/b/abs_b6z_yqw_ii/croot/platformdirs_1692205479426/work
plotly==5.21.0
prompt-toolkit @ file:///C:/b/abs_6coz5_9f2s/croot/prompt-toolkit_1672387908312/work

其他人在使用pip install -r requirements.txt的时候报错,这里对相应的行进行删除.
"""

# 定义文件路径.
file_path = '../requirements.txt'

# 读取文件内容, 使用utf-8编码.
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except UnicodeDecodeError:
    print("文件编码可能不是UTF-8，请重新检查文件编码。")
    exit()

# 过滤掉包含@符号的行.
filtered_lines = [line for line in lines if '@' not in line]

# 将修改后的内容写回文件, 使用utf-8编码.
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)

print("已删除所有包含@符号的行, 并更新了requirements.txt文件。")
