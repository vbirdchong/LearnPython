import itchat
import os
from math import sqrt
from PIL import Image
import csv
import jieba.analyse

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

def get_friends_info():
    male = []
    female = []
    unknow = []
    signature = []
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
        signature.append(friend['Signature'])
    base_info = {}
    base_info['male_info'] = male
    base_info['female_info'] = female
    base_info['province_info'] = province
    base_info['city_info'] = city
    base_info['signature_info'] = signature
    return base_info

def save_to_file(friends_info):
    with open('friends_province.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Province', 'Number'])
        provinces_info = friends_info['province_info']
        print(provinces_info)
        for item in provinces_info.items():
            csv_writer.writerow([item[0], item[1]])

    with open('signature.txt', 'w', encoding='utf-8') as f:
        signature_info = friends_info['signature_info']
        for i in signature_info:
            f.write(i + '\n')

def read_signature_file():
    with open('signature.txt', 'rb') as f:
        content = f.read()
        tags = jieba.analyse.extract_tags(content, topK=20)
        print(','.join(tags))

def main():
    # itchat.login()
    # friends_info = get_friends_info()
    # save_to_file(friends_info)
    # itchat.run
    read_signature_file()

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