# Project5 Mapping Covid Hotspots
Group project 5 - Mapping Covid Hotspots

 ## Contributors
Dana Hackel, Jenny James, Emmanuel Akindele, Zakaria Zerhouni

 ## Problem Statement
The data released regarding instances of the COVID-19 pandemic is aggregated before it is released to (legally and ethically) protect the privacy of those involved. Unfortunately, this takes away some of the utility of the data. Using social media, the location of cases can be narrowed further while still protecting privacy rights. Social media data can provide a heat map for potential COVID-19 risk.

We decided to create a COVID19 heat map for the state of Texas because it had many large metropolitan areas we could pull tweets from.

 ## Data Collection
We equally split 35 cities in Texas among the group members to scrape for tweets. We used the [GetOldTweets3 API](https://github.com/Mottl/GetOldTweets3) to pull up to 14,000 tweets for each city between 08-30-2020 and 09-05-2020. We chose to use the GetOldTweets3 API instead of Twitter's own API because GetOldTweets3 had less limitations, including time and number of tweets scraped.

 ## Data Cleaning and Exploration

We created a dataframe for the tweets from each city. We were able to get a count of the number of tweets containing 'covid' or 'coronavirus' any where within the text. We did not use other terms, like 'virus' or 'corona' as they could represent other meanings, like another virus, or Corona beer and we did not want that included in our data. For each city dataframe, we checked for the total number of tweets (sometimes there was not a full 14,000 because some of the smaller cities did not reach the maximum) and for the correct data types for each column. We also looked for null values, but decided to keep them in the data, as it still represented a tweet which did not mention 'covid' or 'coronavirus'.

[A bar chart of the counted 'covid' or 'coronavirus' mentions can be seen here](https://public.tableau.com/profile/dana.hackel#!/vizhome/covid_bar_chart_final/Sheet3?publish=yes)

 ## Creating a HeatMap
We used Tableau to create a heat map and a bar graph of the number of COVID mentions per city. Data including the number of mentions, latitude, and longitude were complied into an excel document in order to easily be used in Tableau. The heat map was created by first graphing the latitude and longitude of each city, and then circles were created with various sizes and color shades to represent the number of COVID mentions in tweets for that respective city.

[The heat map can be seen here](https://public.tableau.com/profile/dana.hackel#!/vizhome/covid_heat_map_final/Sheet2?publish=yes)
 ## Conclusions
[Actual Texas COVID19 Case Heatmap](https://public.tableau.com/profile/emmanuel.akindele#!/vizhome/TexasCovid/Sheet2?publish=yes
)  
We compared the heat map we created based of of 'covid' or 'coronavirus' mentions in texts to one we created based on data of the number of cases per county in Texas. Some of the cities were fairly close, but others, like Lubbock, El Paso, and Eagle Pass, were over represented. The number of actual cases was also based on the total case count, and not for the cases between 8-30 and 9-5. If case numbers are currently increasing at a  rapid pace in certain cities, we could probably expect more tweets in those areas. However, because some of the larger cities have more overall cases, this wouln't necessarily be reflected in the actual case counts.

The tweets we pulled were random, and may not have had the most representative data for some cities. If we were able to collect more tweets, we may have been able to determine a more representative number of COVID mentions in the tweets. We also were limited by only pulling tweets which had tagged geolocations so that we could determine what area they were from. If we were able to use all tweets, we may have had a better representation.

 ## Recommendations and Future Directions
In the future, we would like to be able to scrape more tweets, and also account for other languages as well. We did not have the fluency or knowledge of other languages to recognize mentions of COVID19 in tweets written in languages other than English. We would like to collect information from other states as well to increase the expanse of the heat map. Lastly, we would like to continue working with this data to create a predictive model that can use Natural Language Processing to predict if the author of a tweet has a confirmed case of COVID19 based on the tweet.

 ## Data Directory
 |__ code_rough_drafts
| |__ getoldtweets.py  
| |__ jenny-dana-work.ipynb  
| |__ twitter3.py  

|__ dana_data
| |__ Abilene_data.csv  
| |__ Amarillo_data.csv  
| |__ El_Paso_data.csv  
| |__ Laredo_data.csv  
| |__ Odessa_data.csv  
| |__ dana-clean-eda.ipynb  
| |__ dana-scrape-data.ipynb  
| |__ sample-heat-map.xlsx  
 
|__ emmanuel
| |__ Data EDA.ipynb  
| |__ Get_Data.ipynb  
| |__ beaumont_data.csv  
| |__ college_station_bryan_data.csv  
| |__ houston_data.csv    
| |__ killeen_data.csv  
| |__ midland_data.csv  
| |__ nacodgoches__data.csv  
| |__ texarkana_data.csv  
 
|__ jenny   
| |__ Odessa_data.csv    
| |__ Austin_noquery_data.csv   
| |__ Brownsville_data.csv  
| |__ Corpus_noquery_data.csv  
| |__ Rockport_data.csv  
| |__ Dalhart_data.csv	  
| |__ San Angelo_data.csv  
| |__ Del Rio_data.csv  
| |__ San Marcos New Braunfels Seguin_data.csv  
| |__ Eagle Pass_data.csv  
| |__ Harlingen_data.csv  
| |__ SanAntonio_data.csv  
| |__ SanAntonio_noquery_data.csv  
| |__ Kerrville Fredericksburg_data.csv   
| |__ Lufkin_data.csv
| |__ jenny_cities_EDA.ipynb 

|__ zak_folder  
| |__ city_tweets  
| |__ zak_data
| |__ 01_tweets_EA_zerhouni.ipynb  
| |__ 02_compile_csv.ipynb 
| |__ 03_modeling.ipynb  
| |__ zak.ipynb  
  
|__ Heat Mapping Covid Cases.pdf  
|__ README.md  

 ## References

[GetOldTweets3](https://github.com/Mottl/GetOldTweets3)  
[Series.str.contains documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains)  
[Tableau](https://public.tableau.com)  
[Texas Metro Areas](https://en.wikipedia.org/wiki/List_of_Texas_metropolitan_areas)  
[GPS Coordinates Generator](https://www.gps-coordinates.net/)  
[Actual Texas COVID19 Case Heatmap](https://public.tableau.com/profile/emmanuel.akindele#!/vizhome/TexasCovid/Sheet2?publish=yes
)  
[NY Times Covid Case Data](https://github.com/nytimes/covid-19-data )
