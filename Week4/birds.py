import pandas as pd

# birddata = pd.read_csv("bird_tracking.csv")
# # birddata.info()
# a = birddata.loc[birddata['bird_name'] == "Sanne"]
# a = str(a)
# birddata = str(birddata)
# print(a)
# print(birddata.find("2013-08-15 00:20:45"))
# print(birddata.find("2013-08-15 00:01:08"))
# print(birddata.find("2013-08-15 00:03:25"))
# print(birddata.find("2013-08-15 00:18:08"))
# print("2013-08-15 00:20:45" in birddata)
# print("2013-08-15 00:01:08" in birddata)
# print("2013-08-15 00:03:25" in birddata)
# print("2013-08-15 00:18:08" in birddata)

import pandas as pd
data = pd.Series([1,2,3,4])
data = data.iloc[[3,0,1,2]]

print(data[0])