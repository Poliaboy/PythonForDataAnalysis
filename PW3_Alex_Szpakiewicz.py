import pandas as pd
import numpy as np
def Ex1():
    voiture = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/be2191a6-a7cd-446f-a9fc-8d698688eb9e")
    print(voiture.shape)#the dataframe has 9 columns and 101924 rows
    print(voiture.info())#dtypes: float64(5), int64(3), object(1)
    print("the means of the numeric columns are:\n",voiture.mean(numeric_only=True))#the mean of the dataframe
    print("the max value for each numeric column is:\n",voiture.max(numeric_only=True))#the max of the dataframe
    print("the min value for each numeric column is:\n",voiture.min(numeric_only=True))#the min of the dataframe
    print(voiture.describe())#the description of the dataframe, it shows the count, mean, std, min, max, 25%, 50%, 75% for each column
    print(voiture.head(30))#the first 30 rows of the dataframe
    print(voiture.tail(30))#the last 30 rows of the dataframe

def Ex2():
    voiture = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/be2191a6-a7cd-446f-a9fc-8d698688eb9e")
    # the columns of the dataframe
    print(voiture.columns)
    voiture.columns = ["Num_Acc", "sens_de_Circulation", "catV","nb_occupants", "obstacle_fixe", "obstacle_mobile", "choc", "manoeuvre" , "num_vehicule" ]
    # the columns of the dataframe after renaming them
    print(voiture.columns)
    # the number of null values in each column
    print(voiture.isna().sum())
    # the percentage of null values in each column
    print(voiture.isna().sum()*100/len(voiture))
    # the column obstacle_fixe, the returned value is a dataframe
    print(voiture[["obstacle_fixe"]])
    # the column obstacle_fixe, the returned value is a numpy array
    obstacle_fixe_np = np.array(voiture["obstacle_fixe"])
    obstacle_fixe_np = obstacle_fixe_np[~np.isnan(obstacle_fixe_np)]
    # the max value of the column obstacle_fixe
    print(obstacle_fixe_np.max())
    #the columns sens_de_Circulation and catV, the returned value is a dataframe
    multcoll = voiture[["sens_de_Circulation", "catV"]]
    print(multcoll)
    #the columns containing the word obstacle, the returned value is a dataframe
    filtcoll = voiture.filter(like="obstacle")
    print(filtcoll)
    #the rows containing null values, the returned value is a dataframe
    sens_de_Circulation = voiture["sens_de_Circulation"]
    nullrows = sens_de_Circulation[sens_de_Circulation.isnull()]
    print(nullrows)
    #the dataframe sorted by Num_Acc and then by catV
    sortcoll = voiture.sort_values(by=["Num_Acc"])
    print(sortcoll)
    sortcollalt = voiture.sort_values(by=["Num_Acc", "catV"])
    print(sortcollalt)
    #the diffrence between getting the row with the index 4153 and the 4153rd row is
    # for the row with the index 4153 we get the row with the index 4153 and for the 4153rd row we get the row with
    # the index 4154
    sprow = voiture.iloc[4153]
    sprowalt = voiture.loc[4153]
    print(sprow)
    print(sprowalt)




Ex2()