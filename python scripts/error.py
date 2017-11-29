import pandas as pd

filename = "test.csv"
df = pd.read_csv(filename,dtype=str)
df = df.fillna(0)
a = df['Q98']
b = df['Q978']
c = df['Q979']
d = df['type']

length = len(d)
error = []

for i in range(length):
    situation = int(d[i])
    ai = int(a[i])
    bi = int(b[i])
    ci = int(c[i])
    if (situation == 1):
        if (ai == 2 and bi == 0 and ci == 0):
            error.append(0)
        else:
            error.append(1)
    elif (situation == 2):
        if (ai == 0 and bi == 2 and ci == 1):
            error.append(0)
        else:
            error.append(1)
    elif (situation == 3):
        if (ai == 0 and bi == 3 and ci == 2):
            error.append(0)
        else:
            error.append(1)
    elif (situation == 4):
        if (ai == 0 and bi == 1 and ci == 2):
            error.append(0)
        else:
            error.append(1)
    elif (situation == 5):
        if (ai == 1 and bi == 0 and ci == 0):
            error.append(0)
        else:
            error.append(1)
    else:
        error.append("?")

df['Error'] = pd.Series(error, index=df.index)
df.to_csv('error.csv', index=False)