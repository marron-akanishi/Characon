import os
import datetime
import time
import tweepy as tp
import urllib.request
import oauth

# 誕生日一覧の読み込み
birthlist = {}
iconlist = {}
with open("birth.csv","r",encoding="utf-8") as csv:
    for line in csv:
        birthlist[line.split(',')[1]] = line.split(',')[0]
        iconlist[line.split(',')[1]] = line.split(',')[2][:-1]

auth = oauth.get_oauth()
api = tp.API(auth)
date = datetime.date.today().strftime("%m/%d")

try:
    name = birthlist[date]
    icon = iconlist[date]
    # アイコン回収
    if not os.path.exists("./icon.jpg"):
        urllib.request.urlretrieve(api.me().profile_image_url.replace("normal","400x400"),"./icon.jpg")
    # アイコン変更
    api.update_profile_image(icon)
    api.update_with_media(icon.replace("icon","original"), "本日は{}の誕生日です".format(name))
except:
    if os.path.exists("./icon.jpg"):
        api.update_profile_image("./icon.jpg")
        os.remove("./icon.jpg")