# Web scraping using BeautufulSoup

Gently scraped one of the biggest property listing website for condo market in Bangkok, Thailand. End result csv file has 50k+ listings with Lat/Long locations and current asking price.

### The work is divided in 3 steps:

1. In the 'Sale' section, there were 1,484 pages. Retrieve all the href links for each page. Total 53,413 links were retreived.

2. Scraped the data for each property, and store in csv files. Make new csv for each 1000 listings. This step is crucial because the web scraping was done gently and it took quite a bit of time. Since this project was done on my personal laptop, I could not let it run 24/7 and it took several days to complete the run. This small chunks were combined in the next step. 

3. Combine all csv files into one and drop missing values.
