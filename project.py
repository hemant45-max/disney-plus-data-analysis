from turtle import color

import pandas as pd
import numpy as nt
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Satyam\AppData\Local\Temp\disney_plus_shows.csv")

print(df.columns)
df = df.dropna(subset=['type','released_at','rated','country','runtime'])


df = df.dropna(subset=['type','released_at','rated','country','runtime'])

type_count=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values, color=['skyblue','orange'])
plt.title('number of movies vs shows on disney')
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('disney_type_distribution.png')
#plt.show()

rated_count=df['rated'].value_counts()
plt.figure(figsize=(8,9))
plt.pie(rated_count.values, labels=rated_count.index, autopct='%1.1f%%',startangle=90)
plt.title('Distribution of Ratings on Disney+')
plt.tight_layout()
plt.savefig('disney_ratings_distribution.png')
#plt.show()

movie_df = df[df['type'] == 'movie'].copy()
movie_df['duration_int'] = movie_df['runtime'].str.replace(' min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'] , bins=30, color='green', edgecolor='black')
plt.title('Distribution of Movie Durations on Disney+')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('disney_movie_duration_distribution.png')
#plt.show()

release_counts =df['year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values, color='red')
plt.plot(release_counts.index,release_counts.values,color='blue')
plt.title('Number of Releases per Year on Disney+')
plt.xlabel('Year')
plt.ylabel('Number of Releases')
plt.tight_layout()
plt.savefig('disney_releases_per_year.png')
#plt.show()


country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(10,6) )
plt.barh(country_counts.index,country_counts.values,color='teal')
plt.title('Top 10 Countries with Most Content on Disney+')
plt.xlabel('Number of Shows/Movies')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('disney_top_countries.png')
#plt.show()

content_by_year = df.groupby(['year','type']).size().unstack().fillna(0)

fig, ax=plt.subplots(1,2,figsize=(12,5))

movie_col = content_by_year.columns[0]
tv_col = content_by_year.columns[1]

ax[0].plot(content_by_year.index, content_by_year[movie_col], color='blue')
ax[0].set_title('Movies released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

ax[1].plot(content_by_year.index, content_by_year[tv_col], color='orange')
ax[1].set_title('TV Shows released per year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

plt.suptitle('Content Released on Disney+ Over the Years')
plt.tight_layout()
plt.savefig('disney_content_over_years.png')
plt.show()

