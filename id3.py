import pandas as pd
import math

class Node:
    def __init__(self,l):
        self.label = l;
        self.branch = {}
        

def entropy(data):
    tot = len(data)
    p_tot = len(data.loc[data[data.columns[-1]] == 'Yes'])
    n_tot = len(data.loc[data[data.columns[-1]] == 'No'])
    en = 0;
    
    if(p_tot > 0):
        en += -(p_tot/float(tot))*(math.log2(p_tot) - math.log2(tot))
    
    if(n_tot > 0):
        en += -(n_tot/float(tot))*(math.log2(n_tot) - math.log2(tot))
        
    return en

def gain(attr,data,en_s):
    
    values = set(data[attr])
    for value in values:
        en_s -= (len(data.loc[data[attr] == value]))/(len(data))*entropy(data.loc[data[attr] == value])
        
    return en_s

def get_attr(data):
    en_s = entropy(data)
    attribute = ''
    max_gn = 0;
    for attr in data.columns[:-1]:
        gn = gain(attr,data,en_s)
        if(gn > max_gn):
            max_gn = gn
            attribute = attr
            
    return attribute
    
    

def decision_tree(data):
    node = Node("NULL")
    
    if(entropy(data) == 0):
        if(len(data.loc[data[data.columns[-1]] == 'Yes']) == len(data)):
            node.label = 'Yes'
        else:
            node.label = 'No'
        
        return node
    
    if(len(data.columns) == 1):
        return
    else:
        attr = get_attr(data)
        node.label = attr
        #print(attr)
        values = set(data[attr])
        
        for value in values:
            node.branch[value] = decision_tree(data.loc[data[attr] == value].drop(attr,axis = 1))
    
    return node;

		

def get_rules(root, rule):
    if not root.branch:
        rule += " => "+root.label
        rules.append(rule)
        return
    
    for val in root.branch:
        nxt = rule
        nxt += root.label + "=" + val + ","
        get_rules(root.branch[val],nxt)
    return
    

def test(root,pres):
    if not root.branch:
        return root.label
    return test(root.branch[str(pres[root.label])] , pres)

data = pd.read_csv("tennis.csv")

#print(data.columns[:-1])
root = decision_tree(data)
print((root.branch['Sunny'].label))

rules = []
get_rules(root,"")

for rule in rules:
    print(rule)

pres = {'Outlook':'Rainy','Temperature':'Hot','Humidity':'Normal','Windy':'Strong'}

    
print(test(root,pres))

