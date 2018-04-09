from twitter import *
t = Twitter(auth=OAuth("Access Token", "Access Token Secret",
                       "Consumer Key", "Consumer Secret"))

# Узнаем последние 5 твитов в ленте @montypython
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)
