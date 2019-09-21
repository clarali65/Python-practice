def get_text():
    '''
    读取文本：将特殊字符换成空格后通过split函数返回词列表
    '''
    filename_read = '罗密欧与朱丽叶(英文版)莎士比亚.txt'
    f = open(filename_read, 'r', encoding='unicode_escape')
    text = f.read().lower()
    for m in '!@#$%^&*()_-+=<>""~:;,./\?':
        text = text.replace(m, ' ')
    return text.split()

ori_list = get_text()
counts = {}
arr_tuple = ()
for i in ori_list:
    counts[i] = counts.get(i, 0) + 1  # 统计词频
arr_tuple = sorted(counts.items(), key=lambda d: d[1], reverse=True)  # 给无序的字典排序后赋给元祖

for j in arr_tuple:
    print(j)