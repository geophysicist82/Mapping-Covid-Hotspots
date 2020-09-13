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
[Actual Texas COVID19 Case Heatmap](https://www.google.com/search?q=covid+cases+in+texas+by+city&rlz=1C1CHBF_enUS906US906&oq=covid+cases+in+texas+by+&aqs=chrome.2.0j69i57j0l6.8686j0j9&sourceid=chrome&ie=UTF-8)  
We compared the heat map we created to one found on Google which shows the number of confirmed COVID19 cases per city in Texas from the last 14 days. Some of the cities were fairly close, but others, Like Dallas and Fort Worth were not as well represented. The tweets we pulled were random, and may not have had the most representative data for those cities. This often occured for the larger cities, which had more tweets from their area than we were able to scrape. If we were able to collect more tweets, we may have been able to determine a more representative number of COVID mentions in the tweets. We also were limited by only pulling tweets which had tagged geolocations so that we could determine what area they were from. If we were able to use all tweets, we may have had a better representation.

 ## Recommendations and Future Directions
In the future, we would like to be able to scrape more tweets, and also account for other languages as well. We did not have the fluency or knowledge of other languages to recognize mentions of COVID19 in tweets written in languages other than English. We would like to collect information from other states as well to increase the expanse of the heat map. Lastly, we would like to continue working with this data to create a predictive model that can use Natural Language Processing to predict if the author of a tweet has a confirmed case of COVID19 based on the tweet.

 ## Data Directory
*add when everything is done and cleaned up*
 ## References

[GetOldTweets3](https://github.com/Mottl/GetOldTweets3)  
[Series.str.contains documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains)  
[Tableau](https://public.tableau.com)  
[Texas Metro Areas](https://en.wikipedia.org/wiki/List_of_Texas_metropolitan_areas)  
[GPS Coordinates Generator](https://www.gps-coordinates.net/)  
[Actual Texas COVID19 Case Heatmap](https://www.google.com/search?q=covid+cases+in+texas+by+city&rlz=1C1CHBF_enUS906US906&oq=covid+cases+in+texas+by+&aqs=chrome.2.0j69i57j0l6.8686j0j9&sourceid=chrome&ie=UTF-8)
