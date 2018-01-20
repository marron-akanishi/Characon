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
is_birth = False
old_date = datetime.date.today().strftime("%m/%d")

# 監視
while(1):
    if old_date != datetime.date.today().strftime("%m/%d"):
        old_date = datetime.date.today().strftime("%m/%d")
        try:
            name = birthlist[old_date]
            icon = iconlist[old_date]
            if not is_birth:
                urllib.request.urlretrieve(api.me().profile_image_url.replace("normal","400x400"),"./icon.jpg")
            api.update_profile_image(icon)
            api.update_status("本日は{}の誕生日です".format(name))
            is_birth = True
        except KeyError:
            api.update_profile_image("./icon.jpg")
            is_birth = False
    time.sleep(60)