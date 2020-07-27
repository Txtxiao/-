# import语句
def is_import(s: str):
    return s.strip().startswith("import")


# 去除短注释
def rm_short_annotation(s: str):
    index = s.find("#")
    if index == -1:
        return s
    if index == 0:
        return ""
    return s[0:index]


# 空行
def is_blank_line(s: str):
    return s.strip() == ""


# 去除不必要的空格
def rm_blanks(s):
    if s.strip() == "":
        return ""
    return s.rstrip()


def modify_py(f, file_path):
    new_f = open(file_path, 'w')
    # 检测长注释
    is_long_anno = False
    while True:
        l = f.readline()
        if l == "":
            break
        if l.strip().startswith('\"\"\"'):
            is_long_anno = not is_long_anno
            continue
        if is_long_anno:
            continue
        if is_import(l) or is_blank_line(l):
            continue
        else:
            l = rm_short_annotation(l)
            l = rm_blanks(l)
            if len(l) == 0:
                continue
            else:
                new_f.write(l + "\n")


if __name__ == '__main__':
    file_path = "../../data/code/test4.py"
    file_path2 = "../../data/code/test5.py"
    modify_py(open(file_path, encoding="utf8"), file_path2)
