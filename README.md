# dentist-sentiment
On this repository, you will find Python code to perform web scraping of the directory provided by the French health insurance, where I retrieved the names of all dentists in the Alsace region. Afterwards, you will find the code to scrape the comments and star ratings left for each dentist on Google Maps. I used Selenium and BeautifulSoup for this task.

The result is a dataset containing all the dentists, their star ratings, and the comments left. We then conducted sentiment analysis using a transformer model obtained from Hugging Face.
