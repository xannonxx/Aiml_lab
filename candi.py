import pandas as pd
import numpy as np

data = pd.read_csv('Training_examples.csv')

concept = np.array(data[data.columns[:-1]])

print("The concepts to be learned")
print(concept)
target = np.array(data[data.columns[-1]])
print("\nLabels specific to the concepts\n")
print(target)
print("\n")

def learn(concept,target):
    specific_h = concept[0]
    general_h = [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]
    
    
    for i in range(len(concept)):
        h = concept[i] 
        if target[i]=='Yes':
            for j in range(len(specific_h)):
                if h[j]!=specific_h[j]:
                    specific_h[j]='?'
                    general_h[j][j]='?'
        elif target[i]=='No':
            for j in range(len(specific_h)):
                if h[j]!=specific_h[j]:
                    general_h[j][j]=specific_h[j]
                else:
                    general_h[j][j]='?'
    
    
    return specific_h,general_h


s_final, g_final = learn(concept,target)
print("Final S: ", s_final)


for val in g_final:
    flag = 0
    for ele in val:
        if(ele != '?'):
            flag = 1
    
    if(flag == 1):
        print(val)
