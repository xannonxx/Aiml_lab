import pandas as pd

data = pd.read_csv('data.csv')
nt = len(data)
np = len(data.loc[data[data.columns[-1]] == 'Yes'])
nn = nt - np

train = data.sample(frac=0.75)

test = pd.concat([data, train]).drop_duplicates(keep=False)

print("Training Set : ", train)
print("Test Set : ", test)

prob = {}


for col in train.columns[:-1]:
    prob[col] = {}

    st = set(train[col])
    for val in st:
        tval = train.loc[train[col] == val]
        pt = len(tval.loc[tval[tval.columns[-1]] == 'Yes'])
        nt = pt - len(tval)
        prob[col][val] = [pt/np, nt/nn]


prediction = []
right_dec = 0

for i in range(len(test)):
    row = test.iloc[i]
    fpp = np/nt
    fpn = nn/nt

    for col in test.columns[:-1]:
        fpp *= prob[col][row[col]][0]
        fpn *= prob[col][row[col]][1]

    if(fpp > fpn):
        prediction.append('Yes')
    else:
        prediction.append('No')

    if(prediction[i] == row['PlayTennis']):
        right_dec += 1


print("prediction : ", prediction)
print("Prediction", right_dec/len(test))
