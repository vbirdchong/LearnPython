#coding:utf-8

##data = open('info.txt')

##for each_line in data:
##    if each_line.find(':') != -1: #在这里增加判断
##        (role, line_spoken) = each_line.split(':', 1)
##        print '%s said: %s' % (role, line_spoken)
##





##使用异常保护的方法来实现
##for each_line in data:
##    try:
##        (role, line_spoken) = each_line.split(':', 1)
##        print '%s said: %s' % (role, line_spoken)
##    except:
##        pass

##data.close()







##增加更多的错误检查
##import os
##
##if os.path.exists('info.txt'):
##    data = open('info.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':', 1)
##            print '%s said: %s' % (role, line_spoken)
##        except:
##            pass
##    data.close()
##else:
##    print('The file is missing!')







##用以下方法会更加的简洁明了
##try:
##    data = open('info.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':', 1)
##            print ('%s said: %s') % (role, line_spoken)
##        except:
##            pass
##except:
##    print ('The file is missing')








##功能增强

##man = []
##other = []
##
##try:
##    data = open('info.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':', 1)
##            line_spoken = line_spoken.strip()
##            if role == 'Man':
##                man.append(line_spoken)
##            elif role == 'Other Man':
##                other.append(line_spoken)
##        except ValueError:
##            pass
##    data.close()
##except IOError as err:
##    print("Open file error: " + str(err))

##
##try:
##    man_data = open('man_data.txt', 'w')
##    other_data = open('other_data.txt', 'w')
##
####    将数据保存到文件中
##    for data_man in man:
##        man_data.write(data_man)
##    for data_other in other:
##        other_data.write(data_other)
####    下面的是3.0的方法    
##    #print (man,file=man_data)
##    #print (other,file=other_data)
##
##except IOError as err:
##    print('File error: ' + str(err))
##
#### finally 无论如何 程序都会执行
##finally:
##    if 'man_datas' and 'other_data'in locals():
##        print("Close the files!")
##        man_data.close()
##        other_data.close()
##    else:
##        print("Close file error")
        





##文件打开关闭异常处理，通常使用 try/except/finally，这里面需要增加错误情况的处理
##用高级点的with 操作可以省去异常处理代码

##高级货
man = []
other = []
try:
    with open('info.txt') as data:
    #data = open('info.txt')
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
        
except IOError as err:
    print("Open file error: " + str(err))

##finally:
##    if 'data' in locals():
##        print("Close info file success!")
##        data.close()
##    else:
##        print("File error!")


try:
##    方法一
##    man_data = open('man_data.txt', 'w')
##    other_data = open('other_data.txt', 'w')
##
####    将数据保存到文件中
##    for data_man in man:
##        man_data.write(data_man)
##    for data_other in other:
##        other_data.write(data_other)

##    方法二
    with open('man_data.txt', 'w') as man_file:
        for data_man in man:
            man_file.write(data_man)
    with open('other_data.txt', 'w') as other_file:
        for data_other in other:
            other_file.write(data_other)
except IOError as err:
    print("File error: " + str(err))

finally:
    if 'man_datas' and 'other_data'in locals():
        print("Close the files!")
        man_data.close()
        other_data.close()
    else:
        print("Close file error")


