import pandas as pd

df = pd.read_csv(r'D:/task/tackoverflow_qa.csv')
df["creationdate"] = pd.to_datetime(df["creationdate"])
df_before_2014=df[df['creationdate']<"2014-01-01"]
df_more_50=df[df['score']>50]
df_between_50_100=df[(df["score"] >= 50) & (df["score"] <= 100)]
df_scot=df[df['ans_name']=='Scott Boston']
top5_users = df['ans_name'].value_counts().head(5).index.tolist()
df_top5 = df[df['ans_name'].isin(top5_users)]
df_6_task=df[(df['creationdate']>="2014-03-01") &
             (df['creationdate']<"2014-11-01") &
             (df['ans_name'].str.lower()=="unutbu") &
             (df['score']<5)
             ]
df_7_task=df[
    ((df['score']>5) &
    (df['score']<10)) |
    (df['viewcount']>10000) 
    ]
df_not_scot=df[df['ans_name']!='Scott Boston']

print(df_not_scot.head())

titanic_df = pd.read_csv(r'D:/task/titanic.csv')
df_female_class1_20_30=titanic_df[
    (titanic_df['Pclass']==1) &
    (titanic_df['Age']>20) &
    (titanic_df['Age']<30) &
    (titanic_df['Sex']=='female')
    ]
df_paid_100=titanic_df[
    titanic_df['Fare']>100
    ]
df_alone=titanic_df[
    (titanic_df['SibSp']==0) &
    (titanic_df['Parch']==0) &
    (titanic_df['Survived']==1)
    ]
df_c_50=titanic_df[
    (titanic_df['Embarked'].str.lower()=='c') &
    (titanic_df['Fare']>50)
    ]
df_sibsp_parch=titanic_df[
    (titanic_df['SibSp']!=0) &
    (titanic_df['Parch']!=0)
    ]
df_15_notsurvive=titanic_df[
    (titanic_df['Age']<15) &
    (titanic_df['Survived']==0)
    ]
df_cabin_200=titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare']>200)
    ]
df_odd=titanic_df[
    (titanic_df['PassengerId']%2==0) 
    ]
ticket_counts = titanic_df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
df_unique_ticket = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]

df_miss_class1=titanic_df[
    (titanic_df['Pclass']==1) &
    (titanic_df['Sex']=='female') &
    (titanic_df['Name'].str.lower().str.contains('miss'))
    ]



print(df_miss_class1.head())
