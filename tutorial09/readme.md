# indi game engine

## Tutorial09
### igefirebase tutorial


- root.py
	- program entry point
- google-services.json
	- your Firebase config file	

### Before running this tutorial, you have to install igefirebase
	[pip install igefirebase]

### Available libraries
	- Admob [ Android / iOS ]
	- Analytics [ Android / iOS ]
	- Authentication [ Android / iOS / Desktop ]
	- Messaging	[ Android / iOS ]

### Functions
#### Firebase
- First, you need to import and init the firebase system
	```
	import igefirebase
	igefirebase.init()
	```
- Release it when everything is done
	```
	igefirebase.release()
	```
#### Firebase Admob
> https://firebase.google.com/docs/admob/cpp/quick-start
- _First, init the firebase admob system_
	- Following the structure : "adMobApp","bannerSize", "gender", "childDirectedTreatment","keywords","birthday", "testDevicesIds"
	- Tuple is supported
	```
	fb_admob = igefirebase.admob()
	fb_admob.init(("ca-app-pub-1009273426450955~3020262852", "ca-app-pub-3940256099942544/6300978111", "ca-app-pub-3940256099942544/1033173712", "ca-app-pub-3940256099942544/2888167318"), (320, 50), 1, 1, ("game", "games", "gamess", "gamesss"), (12, 11, 1988), ("112F1C63CDDE8BAAEE287FDE3BA4C662",))
	```
- _Showing the ads_
	- **Banner**

	| Position | MoveTo Enum |
	| ------- | ------------ |
	| Top of the screen, horizontally centered. | kPositionTop = 0,
	| Bottom of the screen, horizontally centered. | kPositionBottom,
	| Top-left corner of the screen. | kPositionTopLeft,
	| Top-right corner of the screen. | kPositionTopRight,
	| Bottom-left corner of the screen. | kPositionBottomLeft,
	| Bottom-right corner of the screen. | kPositionBottomRight,

	```
	fb_admob.showBanner()
	fb_admob.bannerMoveTo(0)
	fb_admob.bannerMoveTo(1)
	fb_admob.bannerMoveTo(2)
	fb_admob.bannerMoveTo(3)
	fb_admob.bannerMoveTo(4)
	fb_admob.bannerMoveTo(5)
	fb_admob.hideBanner()
	```
	- **Interstitial**
	```
	fb_admob.showInterstitial()
	```
	- **RewardedVideo**
	```
	fb_admob.showRewardedVideo()
	fb_admob.pauseRewardedVideo()
	fb_admob.resumeRewardedVideo()
	```
- _Release it when everything is done_
	```
	fb_admob.release()
	```
#### Firebase Analytics
> https://firebase.google.com/docs/analytics/cpp/events
- _First, init the firebase admob system_
	```
	fb_analytics = igefirebase.analytics()
	fb_analytics.init()
	```
- _Sending the events_
	```
	fb_analytics.setUserProperty("sign_up_method", "google")
	fb_analytics.setUserId("uber_user_510")
	fb_analytics.setCurrentScreen("Firebase Analytics C++ testapp", "testapp")

	fb_analytics.logEvent("login")
	fb_analytics.logEvent("progress", "percent", 0.4)
	fb_analytics.logEvent("post_score", "score", 42)
	fb_analytics.logEvent("join_group", "group_id", "spoon_welders")

	levelUpParameters = (("level", 5), ("character", "mrspoon"), ("hit_accuracy", 3.14))
	fb_analytics.logEvent("level_up", levelUpParameters)
	```
- _Release it when everything is done_
	```
	fb_analytics.release()
	```
#### Firebase Authentication
> https://firebase.google.com/docs/auth/cpp/start
- _First, init the firebase admob system_
	```
	fb_auth = igefirebase.auth()
	fb_auth.init()
	```
- _Authenticate_
	```
	print('signInWithEmailAndPassword : ' + str(fb_auth.signInWithEmailAndPassword("doan.do@indigames.net", "doan.do")))
	print('isPlayerAuthenticated : ' + str(fb_auth.isPlayerAuthenticated()))

	print('signOut : ' + str(fb_auth.signOut()))
	print('isPlayerAuthenticated : ' + str(fb_auth.isPlayerAuthenticated()))

	print('registerWithEmailAndPassword : ' + str(fb_auth.registerWithEmailAndPassword("dodoan.it@gmail.com", "indigames")))
	print('isPlayerAuthenticated : ' + str(fb_auth.isPlayerAuthenticated()))
	```
- _Release it when everything is done_
	```
	fb_auth.release()
	```

#### Firebase Messaging
> https://firebase.google.com/docs/cloud-messaging/cpp/client
- _First, init the firebase messaging system_
	```
	fb_messaging = igefirebase.messaging()
	fb_messaging.init()
	```
- _Sending the messaging(Push Notification) via console
	> https://firebase.google.com/docs/cloud-messaging/cpp/send-with-console
- _Release it when everything is done_
	```
	fb_auth.release()
	```

### Notes
	- Firebase C++ SDK desktop support is a beta feature so only a subset of features supported for now.
		- Authentication
		- Cloud Functions
		- Cloud Storage
		- Realtime Database
		- Remote Config

### Reference
- https://firebase.google.com/docs/cpp/setup?platform=ios 

