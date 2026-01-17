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
load["Adult_category"]=load["adult"].apply(change_adult)
s.sidebar.header("Adult_category")
adult_c=load["adult"].unique().tolist()
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
    s.header("")




    


































































































































































































































































