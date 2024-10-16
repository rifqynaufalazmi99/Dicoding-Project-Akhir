import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_day = pd.read_csv("day.csv")
df_day_2 = df_day.rename(columns={'weathersit':'weather', 'yr':'year', 'mnth':'month', 'hum':'humidity', 'cnt':'count'})
df_day_2 = df_day_2.drop(columns = ['instant' , 'dteday'])

df_hour = pd.read_csv("hour.csv")
df_hour_2 = df_hour.rename(columns={'weathersit':'weather', 'yr':'year', 'mnth':'month', 'hr':'hour','hum':'humidity', 'cnt':'count'})
df_hour_2 = df_hour_2.drop(columns = ['instant' , 'dteday'])

st.title("Bike Sharing Dashboard 🚲")

reg_per_hour = df_hour_2.groupby("hour").registered.sum().sort_values(ascending=False).reset_index()
reg_per_hour.head()

casual_per_hour = df_hour_2.groupby("hour").casual.sum().sort_values(ascending=False).reset_index()
casual_per_hour.head()

st.write("## Total Bike Rentals by Hour")

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(reg_per_hour['hour'], reg_per_hour['registered'], label='Registered', color='blue')
ax.bar(casual_per_hour['hour'], casual_per_hour['casual'], label='Casual', color='orange')
ax.set_xlabel('Hour (in :00)')
ax.set_ylabel('Total Rentals')
ax.legend()

st.pyplot(fig)

st.write("## Registered vs Casual Users in 2011-2012")

fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x='year', y='registered', data=df_day_2, label='Registered Users', color='purple', ax=ax, width=0.5, errorbar=None)
sns.barplot(x='year', y='casual', data=df_day_2, label='Casual Users', color='orange', ax=ax, width=0.5, errorbar=None)
ax.set_xticks([0, 1])
ax.set_xticklabels(['2011', '2012'])
ax.set_xlabel('Year')
ax.set_ylabel('Users Count')
plt.legend()

st.pyplot(fig)

st.caption('© Rifqy Naufal Azmi')
