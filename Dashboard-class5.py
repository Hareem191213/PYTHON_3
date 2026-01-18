import pandas as pd
import streamlit as s
import matplotlib.pyplot as plt

#loading
load=pd.read_csv("movies_df.csv")




#sidebar
s.sidebar.header("MENU FOR MOVIES!!!")
s.sidebar.info("This would help you find any type of movie from below, for example , the movies with high revenue, also can be said as money")
choice=s.sidebar.radio("Go to:",["Home" ,"Graphs"])
s.sidebar.divider()#separator


#FILTERS:
#DESIGNING A FILTER FOR ADULT CATEGORY
#just a normal function to convert boolean(TRUE\FALSE)into normal words
def change_adult(x):
    if x==True:
        return  "adult_movies"
    else:
        return  "non-adult_movies"
#designing....
load["Adult_category"]=load["Adult_category"].apply(change_adult)
s.sidebar.header("Adult_category")
adult_c=load["Adult_category"].unique().tolist()
adult_c.insert(0,"ALL MOVIES🎥")
saved_ad=s.sidebar.selectbox("Select for exploring the adult_category",adult_c)
#DESIGNING A FILTER FOR REVENUE CATEGORY💵
s.sidebar.divider()
s.sidebar.header("Revenue_category")
revenue_c=load["revenues_category"].unique().tolist()
revenue_c.insert(0,"ALL MOVIES🎥")
saved_rev=s.sidebar.selectbox("Select for exploring the revenue_category",revenue_c)
#DESIGNING A FILTER FOR RATING CATEGORY
s.sidebar.divider()
s.sidebar.header("Rating_category")
rating_c=load["rating_category"].unique().tolist()
rating_c.insert(0,"ALL MOVIES🎥")
saved_rati=s.sidebar.selectbox("Select for exploring the rating_category",rating_c)
filter_data=load.copy()


#CONDITIONS:
#condition for if not all movies so (in revenue category)...
if saved_rev !="ALL MOVIES🎥":
    filter_data=filter_data[filter_data["revenues_category"]==saved_rev].reset_index(drop=True)
#condition for if not all movies so(rating_category)...
if saved_rati !="ALL MOVIES🎥":
    filter_data=filter_data[filter_data["rating_category"]==saved_rati].reset_index(drop=True)
#condition for if not all movies so(adult_category)...
if saved_ad !="ALL MOVIES🎥":
    filter_data=filter_data[filter_data["Adult_category"]==saved_ad].reset_index(drop=True)


#PAGES:
if choice =="Home":
    #heading/starting
    s.title("MOVIES FOREVER!!!🎥")
    # little comment doesn't hurt anyone
    s.write(f"Showing {len(filter_data)} movies out of {len(load)} total movies")

    #posters
    for i in range( 0,filter_data.shape[0],3):
        rows = filter_data.iloc[i:i+3]
        cols = s.columns(3)

        for idx , movies in rows.iterrows():
            colum = cols[idx % 3]
            with colum:
                s.image(f"https://image.tmdb.org/t/p/w500{movies['poster_path']}", use_container_width=True)
                s.write(movies['title'])


elif choice =="Graphs":
    #heading
    s.title("Plotting data")
    s.header("Movies vs Runtime⌚")#bar graph
    #making a bar graph
    movies=pd.read_csv("movies_df.csv")
    runtime=movies["runtime"].head(5)
    title=movies["title"].head(5)
    fig1,x1=plt.subplots(figsize=(10,6))
    x1.bar(title, runtime, color=["lightgray","dimgray","gainsboro","gray","silver"])
    x1.set_xlabel("MOVIES", fontsize=14, color="black")
    x1.set_ylabel("RUNTIME", fontsize=14, color="black")
    x1.set_title("MOVIE vs RUNTIME", fontsize=16, color="black")
    x1.grid()
    s.pyplot(fig1)
    s.text("This graph compares movies and their runtime.Each bar shows how long a movie is.Interstellar is the longest, and The Avengers is the shortest. ")
    #making a line graph
    movies=pd.read_csv("movies_df.csv")
    s.divider()
    s.header("Movies vs Popularity🟥")
    popularity=movies["popularity"].tail(4)
    title=movies["title"].tail(4)
    fig2,x2=plt.subplots(figsize=(8,6))
    x2.plot(title, popularity, color="saddlebrown", marker="o", linestyle="--")
    x2.set_xlabel("MOVIES", fontsize=14, color="sienna")
    x2.set_ylabel("POPULARITY", fontsize=14, color="sienna")
    x2.set_title("MOVIE vs POPULARITY", fontsize=16, color="sienna")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    x2.grid()
    s.pyplot(fig2)
    s.text("This line graph shows the popularity of each movie.")
    #making a pie chart
    movies = pd.read_csv("movies_df.csv")
    s.divider()
    s.header("Movies by Decades⏳")
    # convert release_date to datetime
    movies["release_date"] = pd.to_datetime(movies["release_date"])
    # create decades
    movies["year"] = movies["release_date"].dt.year
    movies_1990s = movies[(movies["year"] >= 1990) & (movies["year"] <= 1999)].shape[0]
    movies_2000s = movies[(movies["year"] >= 2000) & (movies["year"] <= 2009)].shape[0]
    movies_2010s = movies[(movies["year"] >= 2010) & (movies["year"] <= 2019)].shape[0]
    # data for pie chart
    labels = ["1990s", "2000s", "2010s"]
    sizes = [movies_1990s, movies_2000s, movies_2010s]
    # dark blue shades
    colors = ["whitesmoke", "ivory", "floralwhite"]
    # plot
    fig, x = plt.subplots(figsize=(10, 6))
    x.pie(sizes, labels=labels,colors=colors,autopct="%1.1f%%",startangle=90)
    x.set_title("MOVIES BY DECADES", color="black", fontsize=16)
    s.pyplot(fig)
    s.text("This pie chart shows that out of 1813 movies , how many were released at which year.")

        
        





        


































































































































































































































































