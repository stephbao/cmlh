import pandas as pd
import numpy as np

filename = "coding.csv"
df = pd.read_csv(filename, encoding = "ISO-8859-1")
new = pd.DataFrame()
f_c = []
t_c = []
e_c = []
f_t = []
t_t = []
e_t = []
f = []
t = []
e = []
f_id = []
t_id = []
e_id = []
f_OR = []
t_OR = []
e_OR = []

for i in range(0, len(df)):
    c = str(df['fairness code'][i])
    c_list = c.split(',')
    for l in c_list:
        f_c.append(l.strip())
        f_t.append(df['20 types'][i])
        f.append(df['fairness'][i])
        f_id.append(df['ID'][i])
        f_OR.append(df['fairness OR'][i])

    c = str(df['trust code'][i])
    c_list = c.split(',')
    for l in c_list:
        t_c.append(l.strip())
        t_t.append(df['20 types'][i])
        t.append(df['trust'][i])
        t_id.append(df['ID'][i])
        t_OR.append(df['trust OR'][i])

    c = str(df['emotion code'][i])
    c_list = c.split(',')
    for l in c_list:
        e_c.append(l.strip())
        e_t.append(df['20 types'][i])
        e.append(df['emotion'][i])
        e_id.append(df['ID'][i])
        e_OR.append(df['emotion OR'][i])

new['fairness ID'] = pd.Series(f_id)
new['20 types fairness'] = pd.Series(f_t)
new['fairness'] = pd.Series(f)
new['fairness code'] = pd.Series(f_c)
new['fairness OR'] = pd.Series(f_OR)

new['trust ID'] = pd.Series(t_id)
new['20 types trust'] = pd.Series(t_t)
new['trust'] = pd.Series(t)
new['trust code'] = pd.Series(t_c)
new['trust OR'] = pd.Series(t_OR)

new['emotion ID'] = pd.Series(e_id)
new['20 types emotion'] = pd.Series(e_t)
new['emotion'] = pd.Series(e)
new['emotion code'] = pd.Series(e_c)
new['emotion OR'] = pd.Series(e_OR)



new.to_csv('split_recode.csv', index=False)