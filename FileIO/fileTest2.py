#coding=utf-8

##传入文件名，并对数据作分割
def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
            return data.strip().split(',')

            
    except IOError as ioErr:
        print "File error: " + str(ioErr)
        return None

##将数据中不同的格式符全部用'.' 代替
def sanitize(data_string):
    if '-' in data_string:
        splitter = '-'
    elif ':' in data_string:
        splitter = ':'
    else:
        return data_string

    (mins, secs) = data_string.split(splitter)
    return (mins + '.' + secs)


##代码主体

james_data = get_coach_data('james.txt')
julie_data = get_coach_data('julie.txt')
mikey_data = get_coach_data('mikey.txt')
sarah_data = get_coach_data('sarah.txt')


##[0:3] 用于取出list中前3位的数据
print sorted(set(sanitize(t) for t in james_data))[0:3]
print sorted(set(sanitize(t) for t in julie_data))[0:3]
print sorted(set(sanitize(t) for t in mikey_data))[0:3]
print sorted(set(sanitize(t) for t in sarah_data))[0:3]


##以下两种方法输出结果完全一样，后者使用了列表推导
####方1
##clean_james_data = []
##for each_time in james_data:
##    clean_james_data.append(sanitize(each_time))
##
##print sorted(clean_james_data)
##
####方2
##print sorted(sanitize(t) for t in james_data)

##set 函数可以创建一个集合，去除其中相同的项
