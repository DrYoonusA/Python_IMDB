# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:53:30 2024

@author: yabrahams
"""

import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

#data cleaning dropping empty cells
df = pd.read_csv("C:/Users/yabrahams/CSS2024/Project/movie_dataset.csv")
df2 = df.dropna()
df_sort = df2.sort_values("Metascore")

#Question 1
print (df.loc[df["Title"].str.contains("Trolls")])
print (df.loc[df["Title"].str.contains("Rogue One")])
print (df.loc[df["Title"].str.contains("Jason Bourne")])
print (df.loc[df["Title"].str.contains("The Dark Knight")])

#Question 2 average revenue calculations
avg_revenue = sum(df_sort["Revenue (Millions)"]) / len(df_sort["Revenue (Millions)"])

#Question 3
df_15_17 = df_sort[df["Year"].between(2015, 2017)]
avg_revenue_2015plus = sum(df_15_17["Revenue (Millions)"]) / len(df_15_17["Revenue (Millions)"])

#Question 4
df_16 = df[df["Year"].between(2016,2016)]
print(len(df_16))

#Question 5
df_nolan = df[df["Director"].str.contains("Christopher Nolan")]
print(df_nolan)
print(len(df_nolan))

#Question 6
df_8plus = df[df["Rating"].between(8.0, 10.0)]
print(df_8plus)
print(len(df_8plus))

#Question 7
nolan_score = np.array([8.5, 8.5, 8.6, 8.8, 9])
print(np.median(nolan_score))

#Question 8
rate_sum_year = df.groupby(df["Year"]).sum()
count_year = df.groupby(df["Year"]).count()
print(rate_sum_year["Rating"])
print(count_year["Rating"])

#Question 9
avg_rate_year = rate_sum_year["Rating"] / count_year["Rating"]
print(avg_rate_year)

movie_incr = ((297 / 44)*100)
movie_incr2 = (count_year.iloc[10]/ count_year.iloc[0])*100
print(movie_incr)
print(movie_incr2)

#Question 10
print (df.loc[df["Actors"].str.contains("Mark Wahlberg")])
print (df.loc[df["Actors"].str.contains("Matthew McConaughey")])
print (df.loc[df["Actors"].str.contains("Chris Pratt")])
print (df.loc[df["Actors"].str.contains("Bradley Cooper")])

mark_w = df.loc[df["Actors"].str.contains("Mark Wahlberg")]
matt_m = df.loc[df["Actors"].str.contains("Matthew McConaughey")]
chris_p = df.loc[df["Actors"].str.contains("Chris Pratt")]
bradley_c = df.loc[df["Actors"].str.contains("Bradley Cooper")]

print(mark_w.count())
print(matt_m.count())
print(chris_p.count())
print(bradley_c.count())

#Question 11
count_genre  = df["Genre"].str.split(',').map(Counter).sum()
print(count_genre)

#Question 12 - has extra calculations included

comedy = df[df["Genre"].str.contains("Comedy")]
adventure = df[df["Genre"].str.contains("Adventure")]
drama = df[df["Genre"].str.contains("Drama")]
action = df[df["Genre"].str.contains("Action")]

avg_comedy = comedy["Revenue (Millions)"].sum() / len(comedy)
avg_action = action["Revenue (Millions)"].sum() / len(action)
avg_adventure = adventure["Revenue (Millions)"].sum() / len(adventure)
avg_drama = drama["Revenue (Millions)"].sum() / len(drama)
print((avg_comedy/avg_drama)*100)
print((avg_adventure/avg_action)*100)

sns.set(color_codes=True)
ax = sns.scatterplot(x=df2["Metascore"], y=df2["Revenue (Millions)"])
plt.show()
bx = sns.scatterplot(x=df2["Runtime (Minutes)"], y=df2["Revenue (Millions)"])
plt.show()
cx = sns.scatterplot(x=df2["Rating"], y=df2["Revenue (Millions)"])
plt.show()

rev_sum_year = df.groupby(df["Year"]).sum("Revenue (Millions)")
count_year = df.groupby(df["Year"]).count()
print(rev_sum_year["Rating"])
print(count_year["Rating"])
avg_rev_year = rev_sum_year["Revenue (Millions)"] / count_year["Revenue (Millions)"]
print(avg_rev_year)