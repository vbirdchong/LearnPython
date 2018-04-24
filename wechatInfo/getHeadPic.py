import itchat
import os
from math import sqrt
from PIL import Image

# itchat.auto_login(hotReload=True)
# index = 1
# for friend in itchat.get_friends(update=True)[0:]:
#     #可以用此句print查看好友的微信名、备注名、性别、省份、个性签名（1：男 2：女 0：性别不详）
#     print(index,friend['NickName'],friend['RemarkName'],friend['Sex'],friend['Province'],friend['City'],friend['Signature'])
#     index += 1
#     img = itchat.get_head_img(userName=friend["UserName"])
#     path = "D:\\Code\\\LearnPython\\\wechatInfo\\\pic\\"+friend['NickName']+"("+friend['RemarkName']+").jpg"
#     try:
#         with open(path,'wb') as f:
#             f.write(img)
#     except Exception as e:
#         print(repr(e))
# itchat.run()

def getFriendsInfo():
    male = []
    female = []
    unknow = []
    province = {}
    city = {}
    for friend in itchat.get_friends(update=True)[0:]:
        genderType = int(friend['Sex'])
        if genderType == 1:
            male.append(friend)
        elif genderType == 2:
            female.append(friend)
        else:
            unknow.append(friend)
        province.setdefault(friend['Province'], 0)
        province[friend['Province']] += 1

        city.setdefault(friend['City'],0)
        city[friend['City']] += 1
    return male, female, unknow, province, city

def main():
    itchat.login()
    male, female, unknow, province, city = getFriendsInfo()
    print("male:" + str(len(male)) + ",female:" + str(len(female)) + ",unknow:" + str(len(unknow)))
    print(province)
    print(city)
    itchat.run

if __name__ == '__main__':
    main()

# path = 'D:\\Code\\\LearnPython\\\wechatInfo\\\pic\\'
# pathList = []
# for item in os.listdir(path):
#     imgPath = os.path.join(path,item)
#     pathList.append(imgPath)
# total = len(pathList)#total是好友头像图片总数
# line = int(sqrt(total))#line是拼接图片的行数（即每一行包含的图片数量）
# NewImage = Image.new('RGB', (128*line,128*line))
# x = y = 0
# for item in pathList:
#     try:
#         img = Image.open(item)
#         img = img.resize((128,128),Image.ANTIALIAS)
#         NewImage.paste(img, (x * 128 , y * 128))
#         x += 1
#     except IOError:
#         print("第%d行,%d列文件读取失败！IOError:%s" % (y,x,item))
#         x -= 1
#     if x == line:
#         x = 0
#         y += 1
#     if (x+line*y) == line*line:
#         break
# NewImage.save(path+"final.jpg")