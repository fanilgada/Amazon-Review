import pandas as pd 

meta_Ratings_Automobile = pd.read_csv("path\\meta_Ratings_Automobile.csv")

meta_Ratings_Automobile_0_50 = meta_Ratings_Automobile[(meta_Ratings_Automobile['price'] > 0) & (meta_Ratings_Automobile['price'] <= 50)]
meta_Ratings_Automobile_50_200 = meta_Ratings_Automobile[(meta_Ratings_Automobile['price'] > 50) & (meta_Ratings_Automobile['price'] <=200)]
meta_Ratings_Automobile_200_Plus = meta_Ratings_Automobile[meta_Ratings_Automobile['price'] > 200]

meta_Ratings_Automobile_0_50.sort_values(['price'], ascending=[True],inplace=True)
meta_Ratings_Automobile_50_200.sort_values(['price'],ascending=[True],inplace=True)
meta_Ratings_Automobile_200_Plus.sort_values(['price'],ascending=[True],inplace=True)

meta_Ratings_Automobile_0_50.to_csv("path\\meta_Ratings_Automobile_0_50.csv",index=False)
meta_Ratings_Automobile_50_200.to_csv("path\\meta_Ratings_Automobile_50_200.csv",index=False)
meta_Ratings_Automobile_200_Plus.to_csv("path\\meta_Ratings_Automobile_200_Plus.csv",index=False)


meta_Ratings_Automobile_0_50_not_good = meta_Ratings_Automobile_0_50[(meta_Ratings_Automobile_0_50['rating'] == 1) | (meta_Ratings_Automobile_0_50['rating']==2)]
meta_Ratings_Automobile_0_50_very_good = meta_Ratings_Automobile_0_50[(meta_Ratings_Automobile_0_50['rating'] == 4) | (meta_Ratings_Automobile_0_50['rating']==5)]

meta_Ratings_Automobile_50_200_not_good = meta_Ratings_Automobile_50_200[(meta_Ratings_Automobile_50_200['rating'] == 1) | (meta_Ratings_Automobile_50_200['rating']==2)]
meta_Ratings_Automobile_50_200_very_good = meta_Ratings_Automobile_50_200[(meta_Ratings_Automobile_50_200['rating'] == 4) | (meta_Ratings_Automobile_50_200['rating']==5)]

meta_Ratings_Automobile_200_Plus_not_good = meta_Ratings_Automobile_200_Plus[(meta_Ratings_Automobile_200_Plus['rating'] == 1) | (meta_Ratings_Automobile_200_Plus['rating']==2)]
meta_Ratings_Automobile_200_Plus_very_good = meta_Ratings_Automobile_200_Plus[(meta_Ratings_Automobile_200_Plus['rating'] == 4) | (meta_Ratings_Automobile_200_Plus['rating']==5)]


meta_Ratings_Automobile_0_50_not_good.to_csv("path\\Automobile_0_50_NG.csv",index=False)
meta_Ratings_Automobile_0_50_very_good.to_csv("path\\Automobile_0_50_VG.csv",index=False)


meta_Ratings_Automobile_50_200_not_good.to_csv("path\\Automobile_50_200_NG.csv",index=False)
meta_Ratings_Automobile_50_200_very_good.to_csv("path\\Automobile_50_200_VG.csv",index=False)

meta_Ratings_Automobile_200_Plus_not_good.to_csv("path\\Automobile_200_plus_NG.csv",index=False)
meta_Ratings_Automobile_200_Plus_very_good.to_csv("path\\Automobile_200_plus_VG.csv",index=False)