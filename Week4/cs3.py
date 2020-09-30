from collections import Counter
def frequency(chars):
    values=chars.values()
    return(Counter(values))

def chance_homophily(chars):
      import numpy as np
      total_N=len(chars.keys())
      f=list(frequency(favorite_colors).values())
      f=np.array(f)
      p=f/total_N
      return(sum(p**2))

#Test case
favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(f'color_homophily: {color_homophily}')

import pandas as pd
df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df1 = df.loc[df['village'] == 1]
df2 = df.loc[df['village'] == 2]

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df1)

#set index to pid
df11=df1.set_index('pid')
df22=df2.set_index('pid')

#transform to dictionary with method .to_dict()
sex1=df11.resp_gend.to_dict()
caste1=df11.caste.to_dict()
religion1 =df11.religion.to_dict()


sex2=df22.resp_gend.to_dict()
caste2=df22.caste.to_dict()
religion2 =df22.religion.to_dict()

# print(caste2)
print("Village 1 chance of same sex:", chance_homophily(sex1))
# Enter your code here.
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))

print("Village 2 chance of same sex:", chance_homophily(sex2))

print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties=num_ties+1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties=num_same_ties+1
    return (num_same_ties / num_ties)

pid1  = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0)
pid2  = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0)

#Exercise 7--------------------
print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1))
print("Village 1 observed proportion of same religion:", homophily(G1, religion1, pid1))

print("Village 1 chance of homophilyhily by same sexe:",chance_homophily(sex1))
print("Village 1 chance of homophily by same caste:",chance_homophily(caste1))
print("Village 1 chance of homophily by same religion:",chance_homophily(religion1))



print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2))
print("Village 2 observed proportion of same religion:", homophily(G2, religion2, pid2))


print("Village 2 chance of homophilyhily by same sexe:",chance_homophily(sex2))
print("Village 2 chance of homophily by same caste:",chance_homophily(caste2))
print("Village 2 chance of homophily by same religion:",chance_homophily(religion2))