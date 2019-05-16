# coding: utf-8
def judge_palindrone(s):
        return s == s[::-1]
judge_palindrone("as")
judge_palindrone("s")
judge_palindrone("sss")
res = [0]*len(s)
s = "babad"
res = [0]*len(s)
res = [1]*len(s)
def get_long_palindrone(s):
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(len_s):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return final_index
s = "a"
get_long_palindrone("s")
def get_long_palindrone(s):
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return final_index
get_long_palindrone("a")
def get_long_palindrone(s):
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return  len_s - final_index
get_long_palindrone("s")
get_long_palindrone("ss")
get_long_palindrone("sss")
get_long_palindrone("ssss")
get_long_palindrone("sas")
get_long_palindrone("ssas")
def get_long_palindrone(s):
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return  len_s - final_index + 1
get_long_palindrone(”s“)
get_long_palindrone("s")
get_long_palindrone("ss")
def get_long_palindrone(s):
    if len(s) == 1:
        return 1
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return  len_s - final_index + 1
get_long_palindrone("s")
get_long_palindrone("sss")
get_long_palindrone("sass")
get_long_palindrone("sasas")
get_long_palindrone("sasas")
def get_long_palindrone(s):
    if len(s) == 1:
        return 1
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s+1):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return  len_s - final_index + 1
get_long_palindrone("sa")
get_long_palindrone("ss")
get_long_palindrone("sss")
def get_long_palindrone(s):
    if len(s) == 1:
        return 1
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s+1):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = i
    return  len_s - final_index 
get_long_palindrone("s")
get_long_palindrone("sss")
get_long_palindrone("ssss")
def get_long_palindrone(s):
    if len(s) == 1:
        return 1
    flag = s[-1]
    len_s = len(s)
    final_index = len_s - 1
    for i in range(1,len_s+1):
        if (s[len_s - i] == flag):
            if judge_palindrone(s[len_s-i:]):
                final_index = len_s - i
    return  len_s - final_index 
get_long_palindrone("ss")
get_long_palindrone("sas")
get_long_palindrone("saas")
get_long_palindrone("sasas")
get_long_palindrone("saasas")
res = [1]* len(s)
for i in range(len(s)):
    res[i] = get_long_palindrone(s[:i])
    
for i in range(len(s)):
    res[i] = get_long_palindrone(s[:i+1])
    
    
get_ipython().run_line_magic('save', '1.py')
sav
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', '"1.py"')
get_ipython().run_line_magic('save', '"./1.py"')
get_ipython().run_line_magic('save', '1')
get_ipython().run_line_magic('save', './1')
get_ipython().run_line_magic('save', '"./1"')
get_ipython().run_line_magic('save', '1')
get_ipython().run_line_magic('save', 'current_session ~0/')
