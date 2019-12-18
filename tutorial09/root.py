"""
"""
import igefirebase
import time

def AdmobListener(adsType, amount, reward):
    print('AdmobListener ads=' + adsType + ' amount=' + str(amount) +' reward=' + str(reward))

igefirebase.init()
fb_analytics = igefirebase.analytics()
fb_analytics.init()

fb_admob = igefirebase.admob()
fb_admob.init(android=(("ca-app-pub-1009273426450955~3020262852", "ca-app-pub-3940256099942544/6300978111", "ca-app-pub-3940256099942544/1033173712", "ca-app-pub-3940256099942544/2888167318"), (320, 50), 1, 1, ("game", "games", "gamess", "gamesss"), (12, 11, 1988), ("112F1C63CDDE8BAAEE287FDE3BA4C662",)), ios=(("ca-app-pub-1009273426450955~8681696761", "ca-app-pub-3940256099942544/2934735716", "ca-app-pub-3940256099942544/4411468910", "ca-app-pub-3940256099942544/6386090517"), (320, 50), 1, 1, ("game", "games", "gamess", "gamesss"), (12, 11, 1988), ("112F1C63CDDE8BAAEE287FDE3BA4C662",)))
fb_admob.registerEventListener(AdmobListener)

fb_auth = igefirebase.auth()
fb_auth.init()

fb_messaging = igefirebase.messaging()
fb_messaging.init()

# firebase analytics testcase
fb_analytics.setUserProperty("sign_up_method", "google")
fb_analytics.setUserId("uber_user_510")
fb_analytics.setCurrentScreen("Firebase Analytics C++ testapp", "testapp")

fb_analytics.logEvent("login")
fb_analytics.logEvent("progress", "percent", 0.4)
fb_analytics.logEvent("post_score", "score", 42)
fb_analytics.logEvent("join_group", "group_id", "spoon_welders")

levelUpParameters = (("level", 5), ("character", "mrspoon"), ("hit_accuracy", 3.14))
fb_analytics.logEvent("level_up", levelUpParameters)

# firebase admob testcase
fb_admob.showBanner()
fb_admob.bannerMoveTo(0)
fb_admob.bannerMoveTo(1)
fb_admob.bannerMoveTo(2)
fb_admob.bannerMoveTo(3)
fb_admob.bannerMoveTo(4)
fb_admob.bannerMoveTo(5)
fb_admob.hideBanner()

fb_admob.showInterstitial()

fb_admob.showRewardedVideo()
fb_admob.pauseRewardedVideo()
fb_admob.resumeRewardedVideo()

# firebase auth testcase
print('signInWithEmailAndPassword : ' + str(fb_auth.signInWithEmailAndPassword("doan.do@indigames.net", "doan.do")))
print('isPlayerAuthenticated : ' + str(fb_auth.isPlayerAuthenticated()))

print('signOut : ' + str(fb_auth.signOut()))
print('isPlayerAuthenticated : ' + str(fb_auth.isPlayerAuthenticated()))

print('registerWithEmailAndPassword : ' + str(fb_auth.registerWithEmailAndPassword("dodoan.it@gmail.com", "indigames")))
print('isPlayerAuthenticated : ' + str(fb_auth.isPlayerAuthenticated()))

# release the resource
fb_analytics.release()
fb_admob.release()
fb_auth.release()
fb_messaging.release()

igefirebase.release()

# Wait for 5 seconds
time.sleep(5)