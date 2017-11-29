import pandas as pd
import numpy as np

#change second Q69 to Q69 2
#delete 2nd & 3rd rows
#delete empty rows

filename = "1400.csv"
df = pd.read_csv(filename, encoding = "ISO-8859-1")
new_df = pd.read_csv('empty_table.csv',dtype=str)
#new_df = pd.DataFrame()
df = df.fillna(0)

task = df['task']
situation = df['type']
length = len(task)

#make lists for each column for new table
#ID TASK    TYPE    FAIRNESS    FAIRNESS OR HAPPY   JOYFUL  PROUD   DISAPPOINTED    ANGRY   FRUSTRATED  TRUST   EMOTION EMOTION OR  TRUST   TRUST OR    MC1 MC2                                     
ID = []
fairness = []
fairness_OR = []
happy = []
joyful = []
proud = []
disappointed = []
angry = []
frustrated = []
#emotion = []
emotion_OR = []
trust = []
trust_OR = []
mc = []
mc2 = []
#mc3 = []
#Q69 Q67 Q64 Q69 Q73
demo1 = []
demo2 = []
demo3 = []
demo4 = []
demo5 = []
alg = []
error = list(np.zeros(length))
error1 = list(np.zeros(length))

for i in range(length):
    t = int(task[i])
    s = int(situation[i])
    ID.append(df['ResponseId'][i])
    demo1.append(df['Q69'][i])
    demo2.append(df['Q67'][i])
    demo3.append(df['Q64'][i])
    demo4.append(df['Q69 2'][i])
    demo5.append(df['Q73'][i])
    alg.append(df['Q867'][i])
    toggle = False

    if (s >= 2 and s <= 4):
        mc.append(df['Q1861'][i])
        mc2.append(df['Q1862'][i])
    else:
        mc.append(df['Q98'][i])
        mc2.append('0')

    '''if (toggle):
        mc2.append(df['Q234'][i])
        mc3.append(df['Q235'][i])
        toggle = False'''

    if (s == 1 or s == 5):
        if (int(mc[i]) != s):
            error[i]+= 1
    
    else:
        if (int(mc[i]) != 3):
            error[i]+=1


    #assign-algo
    if (t==1 and s==1):
        fairness.append(df['Q1684'][i])
        fairness_OR.append(df['Q1685'][i])
        happy.append(df['Q1686_1'][i])
        joyful.append(df['Q1686_2'][i])
        proud.append(df['Q1686_3'][i])
        disappointed.append(df['Q1686_4'][i])
        angry.append(df['Q1686_5'][i])
        frustrated.append(df['Q1686_6'][i])
        #emotion = (df['Q1686_1'][i] + df['Q1686_2'][i] + df['Q1686_3'][i] + 24 - df['Q1686_4'][i] - df['Q1686_5'][i] - df['Q1686_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1687'][i])
        trust.append(df['Q1688'][i])
        trust_OR.append(df['Q1689'][i])

        if (int(df['Q1690'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1

    #schedule-algo
    elif (t==2 and s==1):
        fairness.append(df['Q1694'][i])
        fairness_OR.append(df['Q1695'][i])
        happy.append(df['Q1696_1'][i])
        joyful.append(df['Q1696_2'][i])
        proud.append(df['Q1696_3'][i])
        disappointed.append(df['Q1696_4'][i])
        angry.append(df['Q1696_5'][i])
        frustrated.append(df['Q1696_6'][i])
        #emotion = (df['Q1696_1'][i] + df['Q1696_2'][i] + df['Q1696_3'][i] + 24 - df['Q1696_4'][i] - df['Q1696_5'][i] - df['Q1696_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1697'][i])
        trust.append(df['Q1698'][i])
        trust_OR.append(df['Q1699'][i])

        if (int(df['Q1700'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1

    #hiring-algo
    elif (t==3 and s==1):
        fairness.append(df['Q1704'][i])
        fairness_OR.append(df['Q1705'][i])
        happy.append(df['Q1706_1'][i])
        joyful.append(df['Q1706_2'][i])
        proud.append(df['Q1706_3'][i])
        disappointed.append(df['Q1706_4'][i])
        angry.append(df['Q1706_5'][i])
        frustrated.append(df['Q1706_6'][i])
        #emotion = (df['Q1706_1'][i] + df['Q1706_2'][i] + df['Q1706_3'][i] + 24 - df['Q1706_4'][i] - df['Q1706_5'][i] - df['Q1706_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1707'][i])
        trust.append(df['Q1708'][i])
        trust_OR.append(df['Q1709'][i])

        if (int(df['Q1710'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #eval-algo
    elif (t==4 and s==1):
        fairness.append(df['Q1714'][i])
        fairness_OR.append(df['Q1715'][i])
        happy.append(df['Q1716_1'][i])
        joyful.append(df['Q1716_2'][i])
        proud.append(df['Q1716_3'][i])
        disappointed.append(df['Q1716_4'][i])
        angry.append(df['Q1716_5'][i])
        frustrated.append(df['Q1716_6'][i])
        #emotion = (df['Q1716_1'][i] + df['Q1716_2'][i] + df['Q1716_3'][i] + 24 - df['Q1716_4'][i] - df['Q1716_5'][i] - df['Q1716_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1717'][i])
        trust.append(df['Q1718'][i])
        trust_OR.append(df['Q1719'][i])

        if (int(df['Q1720'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #assign-a2h
    elif (t==1 and s==2):
        fairness.append(df['Q1724'][i])
        fairness_OR.append(df['Q1725'][i])
        happy.append(df['Q1726_1'][i])
        joyful.append(df['Q1726_2'][i])
        proud.append(df['Q1726_3'][i])
        disappointed.append(df['Q1726_4'][i])
        angry.append(df['Q1726_5'][i])
        frustrated.append(df['Q1726_6'][i])
       #emotion = (df['Q1726_1'][i] + df['Q1726_2'][i] + df['Q1726_3'][i] + 24 - df['Q1726_4'][i] - df['Q1726_5'][i] - df['Q1726_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1727'][i])
        trust.append(df['Q1728'][i])
        trust_OR.append(df['Q1729'][i])

        if (int(df['Q1730'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #schedule-a2h
    elif (t==2 and s==2):
        fairness.append(df['Q1757'][i])
        fairness_OR.append(df['Q1758'][i])
        happy.append(df['Q1759_1'][i])
        joyful.append(df['Q1759_2'][i])
        proud.append(df['Q1759_3'][i])
        disappointed.append(df['Q1759_4'][i])
        angry.append(df['Q1759_5'][i])
        frustrated.append(df['Q1759_6'][i])
        #emotion = (df['Q1759_1'][i] + df['Q1759_2'][i] + df['Q1759_3'][i] + 24 - df['Q1759_4'][i] - df['Q1759_5'][i] - df['Q1759_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1760'][i])
        trust.append(df['Q1761'][i])
        trust_OR.append(df['Q1762'][i])

        if (int(df['Q1763'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #hiring-a2h
    elif (t==3 and s==2):
        fairness.append(df['Q1787'][i])
        fairness_OR.append(df['Q1788'][i])
        happy.append(df['Q1789_1'][i])
        joyful.append(df['Q1789_2'][i])
        proud.append(df['Q1789_3'][i])
        disappointed.append(df['Q1789_4'][i])
        angry.append(df['Q1789_5'][i])
        frustrated.append(df['Q1789_6'][i])
        #emotion = (df['Q1789_1'][i] + df['Q1789_2'][i] + df['Q1789_3'][i] + 24 - df['Q1789_4'][i] - df['Q1789_5'][i] - df['Q1789_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1790'][i])
        trust.append(df['Q1791'][i])
        trust_OR.append(df['Q1792'][i])

        if (int(df['Q1793'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #eval-a2h
    elif (t==4 and s==2):
        fairness.append(df['Q1817'][i])
        fairness_OR.append(df['Q1818'][i])
        happy.append(df['Q1819_1'][i])
        joyful.append(df['Q1819_2'][i])
        proud.append(df['Q1819_3'][i])
        disappointed.append(df['Q1819_4'][i])
        angry.append(df['Q1819_5'][i])
        frustrated.append(df['Q1819_6'][i])
        #emotion = (df['Q1819_1'][i] + df['Q1819_2'][i] + df['Q1819_3'][i] + 24 - df['Q1819_4'][i] - df['Q1819_5'][i] - df['Q1819_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1820'][i])
        trust.append(df['Q1821'][i])
        trust_OR.append(df['Q1822'][i])

        if (int(df['Q1823'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1

     #assign-rules
    elif (t==1 and s==3):
        fairness.append(df['Q1734'][i])
        fairness_OR.append(df['Q1735'][i])
        happy.append(df['Q1736_1'][i])
        joyful.append(df['Q1736_2'][i])
        proud.append(df['Q1736_3'][i])
        disappointed.append(df['Q1736_4'][i])
        angry.append(df['Q1736_5'][i])
        frustrated.append(df['Q1736_6'][i])
        #emotion = (df['Q1736_1'][i] + df['Q1736_2'][i] + df['Q1736_3'][i] + 24 - df['Q1736_4'][i] - df['Q1736_5'][i] - df['Q1736_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1737'][i])
        trust.append(df['Q1738'][i])
        trust_OR.append(df['Q1739'][i])

        if (int(df['Q1740'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
  
    #schedule-rules
    elif (t==2 and s==3):
        fairness.append(df['Q1767'][i])
        fairness_OR.append(df['Q1768'][i])
        happy.append(df['Q1769_1'][i])
        joyful.append(df['Q1769_2'][i])
        proud.append(df['Q1769_3'][i])
        disappointed.append(df['Q1769_4'][i])
        angry.append(df['Q1769_5'][i])
        frustrated.append(df['Q1769_6'][i])
        #emotion = (df['Q1769_1'][i] + df['Q1769_2'][i] + df['Q1769_3'][i] + 24 - df['Q1769_4'][i] - df['Q1769_5'][i] - df['Q1769_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1770'][i])
        trust.append(df['Q1771'][i])
        trust_OR.append(df['Q1772'][i])

        if (int(df['Q1773'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #hiring-rules
    elif (t==3 and s==3):
        fairness.append(df['Q1797'][i])
        fairness_OR.append(df['Q1798'][i])
        happy.append(df['Q1799_1'][i])
        joyful.append(df['Q1799_2'][i])
        proud.append(df['Q1799_3'][i])
        disappointed.append(df['Q1799_4'][i])
        angry.append(df['Q1799_5'][i])
        frustrated.append(df['Q1799_6'][i])
        #emotion = (df['Q1799_1'][i] + df['Q1799_2'][i] + df['Q1799_3'][i] + 24 - df['Q1799_4'][i] - df['Q1799_5'][i] - df['Q1799_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1800'][i])
        trust.append(df['Q1801'][i])
        trust_OR.append(df['Q1802'][i])

        if (int(df['Q1803'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #eval-rules
    elif (t==4 and s==3):
        fairness.append(df['Q1827'][i])
        fairness_OR.append(df['Q1828'][i])
        happy.append(df['Q1829_1'][i])
        joyful.append(df['Q1829_2'][i])
        proud.append(df['Q1829_3'][i])
        disappointed.append(df['Q1829_4'][i])
        angry.append(df['Q1829_5'][i])
        frustrated.append(df['Q1829_6'][i])
        #emotion = (df['Q1829_1'][i] + df['Q1829_2'][i] + df['Q1829_3'][i] + 24 - df['Q1829_4'][i] - df['Q1829_5'][i] - df['Q1829_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1830'][i])
        trust.append(df['Q1831'][i])
        trust_OR.append(df['Q1832'][i])

        if (int(df['Q1833'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #assign-h2a
    elif (t==1 and s==4):
        fairness.append(df['Q1744'][i])
        fairness_OR.append(df['Q1745'][i])
        happy.append(df['Q1746_1'][i])
        joyful.append(df['Q1746_2'][i])
        proud.append(df['Q1746_3'][i])
        disappointed.append(df['Q1746_4'][i])
        angry.append(df['Q1746_5'][i])
        frustrated.append(df['Q1746_6'][i])
        #emotion = (df['Q1746_1'][i] + df['Q1746_2'][i] + df['Q1746_3'][i] + 24 - df['Q1746_4'][i] - df['Q1746_5'][i] - df['Q1746_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1747'][i])
        trust.append(df['Q1748'][i])
        trust_OR.append(df['Q1749'][i])
 
        if (int(df['Q1750'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #schedule-h2a
    elif (t==2 and s==4):
        fairness.append(df['Q1777'][i])
        fairness_OR.append(df['Q1778'][i])
        happy.append(df['Q1779_1'][i])
        joyful.append(df['Q1779_2'][i])
        proud.append(df['Q1779_3'][i])
        disappointed.append(df['Q1779_4'][i])
        angry.append(df['Q1779_5'][i])
        frustrated.append(df['Q1779_6'][i])
        #emotion = (df['Q1779_1'][i] + df['Q1779_2'][i] + df['Q1779_3'][i] + 24 - df['Q1779_4'][i] - df['Q1779_5'][i] - df['Q1779_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1780'][i])
        trust.append(df['Q1781'][i])
        trust_OR.append(df['Q1782'][i])

        if (int(df['Q1783'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #hiring-h2a
    elif (t==3 and s==4):
        fairness.append(df['Q1807'][i])
        fairness_OR.append(df['Q1808'][i])
        happy.append(df['Q1809_1'][i])
        joyful.append(df['Q1809_2'][i])
        proud.append(df['Q1809_3'][i])
        disappointed.append(df['Q1809_4'][i])
        angry.append(df['Q1809_5'][i])
        frustrated.append(df['Q1809_6'][i])
        #emotion = (df['Q1809_1'][i] + df['Q1809_2'][i] + df['Q1809_3'][i] + 24 - df['Q1809_4'][i] - df['Q1809_5'][i] - df['Q1809_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1810'][i])
        trust.append(df['Q1811'][i])
        trust_OR.append(df['Q1812'][i])

        if (int(df['Q1813'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #eval-h2a
    elif (t==4 and s==4):
        fairness.append(df['Q1837'][i])
        fairness_OR.append(df['Q1838'][i])
        happy.append(df['Q1839_1'][i])
        joyful.append(df['Q1839_2'][i])
        proud.append(df['Q1839_3'][i])
        disappointed.append(df['Q1839_4'][i])
        angry.append(df['Q1839_5'][i])
        frustrated.append(df['Q1839_6'][i])
       # emotion = (df['Q1839_1'][i] + df['Q1839_2'][i] + df['Q1839_3'][i] + 24 - df['Q1839_4'][i] - df['Q1839_5'][i] - df['Q1839_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1840'][i])
        trust.append(df['Q1841'][i])
        trust_OR.append(df['Q1842'][i])

        if (int(df['Q1843'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #assign-human
    elif (t==1 and s==5):
        fairness.append(df['Q1644'][i])
        fairness_OR.append(df['Q1645'][i])
        happy.append(df['Q1646_1'][i])
        joyful.append(df['Q1646_2'][i])
        proud.append(df['Q1646_3'][i])
        disappointed.append(df['Q1646_4'][i])
        angry.append(df['Q1646_5'][i])
        frustrated.append(df['Q1646_6'][i])
        #emotion = (df['Q1646_1'][i] + df['Q1646_2'][i] + df['Q1646_3'][i] + 24 - df['Q1646_4'][i] - df['Q1646_5'][i] - df['Q1646_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1647'][i])
        trust.append(df['Q1648'][i])
        trust_OR.append(df['Q1649'][i])

        if (int(df['Q1650'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #schedule-human
    elif (t==2 and s==5):
        fairness.append(df['Q1654'][i])
        fairness_OR.append(df['Q1655'][i])
        happy.append(df['Q1656_1'][i])
        joyful.append(df['Q1656_2'][i])
        proud.append(df['Q1656_3'][i])
        disappointed.append(df['Q1656_4'][i])
        angry.append(df['Q1656_5'][i])
        frustrated.append(df['Q1656_6'][i])
        #emotion = (df['Q1656_1'][i] + df['Q1656_2'][i] + df['Q1656_3'][i] + 24 - df['Q1656_4'][i] - df['Q1656_5'][i] - df['Q1656_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1657'][i])
        trust.append(df['Q1658'][i])
        trust_OR.append(df['Q1659'][i])

        if (int(df['Q1660'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #hiring-human
    elif (t==3 and s==5):
        fairness.append(df['Q1664'][i])
        fairness_OR.append(df['Q1665'][i])
        happy.append(df['Q1666_1'][i])
        joyful.append(df['Q1666_2'][i])
        proud.append(df['Q1666_3'][i])
        disappointed.append(df['Q1666_4'][i])
        angry.append(df['Q1666_5'][i])
        frustrated.append(df['Q1666_6'][i])
        #emotion = (df['Q1666_1'][i] + df['Q1666_2'][i] + df['Q1666_3'][i] + 24 - df['Q1666_4'][i] - df['Q1666_5'][i] - df['Q1666_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1667'][i])
        trust.append(df['Q1668'][i])
        trust_OR.append(df['Q1669'][i])

        if (int(df['Q1670'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
    #eval-human
    elif (t==4 and s==5):
        fairness.append(df['Q1674'][i])
        fairness_OR.append(df['Q1675'][i])
        happy.append(df['Q1676_1'][i])
        joyful.append(df['Q1676_2'][i])
        proud.append(df['Q1676_3'][i])
        disappointed.append(df['Q1676_4'][i])
        angry.append(df['Q1676_5'][i])
        frustrated.append(df['Q1676_6'][i])
        #emotion = (df['Q1676_1'][i] + df['Q1676_2'][i] + df['Q1676_3'][i] + 24 - df['Q1676_4'][i] - df['Q1676_5'][i] - df['Q1676_6'][i])/6
        #emotion.append(emotion)
        emotion_OR.append(df['Q1677'][i])
        trust.append(df['Q1678'][i])
        trust_OR.append(df['Q1679'][i])

        if (int(df['Q1680'][i]) <= 2):
            error1[i] += 0
        else:
            error1[i] += 1
 
happy = list(map(int, happy))
joyful = list(map(int, joyful))
proud = list(map(int, proud))
disappointed = list(map(int, disappointed))
angry = list(map(int, angry))
frustrated = list(map(int, frustrated))
emotion = []

for i in range(len(happy)):
    emotion.append((happy[i]+joyful[i]+proud[i]+(8-disappointed[i])+(8-angry[i])+(8-frustrated[i]))/6)

#ID TASK    TYPE    FAIRNESS    FAIRNESS OR HAPPY   JOYFUL  PROUD   DISAPPOINTED    ANGRY   FRUSTRATED  TRUST   EMOTION EMOTION OR  TRUST   TRUST OR    MC1 MC2                                     

new_df['ID'] = pd.Series(ID, index=df.index)
new_df['task'] = pd.Series(task, index=df.index)
new_df['decision maker'] = pd.Series(situation, index=df.index)
new_df['HitL mc'] = pd.Series(mc, index=df.index)
new_df['MC Human OR'] = pd.Series(mc2, index=df.index)
#new_df['MC Algo OR'] = pd.Series(mc3, index=df.index)
new_df['mc error'] = pd.Series(error, index=df.index)
new_df['reading check error'] = pd.Series(error1, index=df.index)
new_df['fairness'] = pd.Series(fairness, index=df.index)
new_df['fairness_OR'] = pd.Series(fairness_OR, index=df.index)
new_df['happy'] = pd.Series(happy, index=df.index)
new_df['joyful'] = pd.Series(joyful, index=df.index)
new_df['proud'] = pd.Series(proud, index=df.index)
new_df['disappointed'] = pd.Series(disappointed, index=df.index)
new_df['angry'] = pd.Series(angry, index=df.index)
new_df['frustrated'] = pd.Series(frustrated, index=df.index)
new_df['emotion'] = pd.Series(emotion, index=df.index)
new_df['emotion_OR'] = pd.Series(emotion_OR, index=df.index)
new_df['trust'] = pd.Series(trust, index=df.index)
new_df['trust_OR'] = pd.Series(trust_OR, index=df.index)
new_df['programming exp'] = pd.Series(demo1, index=df.index)
new_df['age'] = pd.Series(demo2, index=df.index)
new_df['gender'] = pd.Series(demo3, index=df.index)
new_df['education'] = pd.Series(demo4, index=df.index)
new_df['ethnicity'] = pd.Series(demo5, index=df.index)
new_df['algorithm definition'] = pd.Series(alg, index=df.index)


new_df.to_csv('1400_table.csv', index=False)
