# Trending-Now
Adopting NLP text processing methods to analyze tweet sentiments on Premier League teams | Made with Pyscript and Javascript

### View the application demo [here](https://drive.google.com/file/d/1OBxnusYtSITpMGdLVJyX5FmUN2liKcvC/view?usp=sharing)

### How to Run:
Test it out here: [chrome]https://gciputra.github.io/Trending-Now/ OR
Clone this repository and on the terminal, set up a local host server:
```python -m http.server -b 127.0.0.1 8080```
That's all!

### The idea
Agueroooooo!!! The world of football is full of passion, drama and ice-cold criticism. As one of the most prominent social media platforms for virtually anyone to voice their opinions, the world of football and sports media in general has never been the same since the launch of Twitter. Trending Now serves as a simple-to-operate browser app available to use in Chrome, Internet Explorer, Bing, and many others to analyze tweet sentiments on premier league teams. As the project utilizes web-parsing under Rapid API, it is able to analyze the percentage of tweets that are positive and negative and displays samples of tweets for both. The machine learning module "TextBlob" boasts up to 68% accuracy in determining the sentiment polarity of each tweet. Ideas are always welcome to improve this model! 

### File and directory guide
- main.py => handles the logic such as array handling functions for manipulating user data from index.html
- index.html => front-end main display which loads the premier league standings 
- getTweets.py => constructs twitter client to parse and provide sentiment analysis logic to be displayed in tweets.html
- tweets.html => redirected web page that displays the tweet sentiment data based on input from index.html
- requirements.txt => lists the libraries and frameworks employed along with their version. All installed with pip. 

### How the code works:
Intro to Pyscript: Pyscript is a very Alpha python framework which eases integrating python scripts and logic into html files while also providing the capabilities of exchanging objects between python and javascript such as objects, functions, or variables. As the project's backend logic is predominantly written under python, I utilized this python framework to take advantage of exchanging data quickly and easily between the front-end and back-end. 
Flow of code:\

**Index.html and main.py**\
1. The file contains a mixture of Javascript in <scripts> and Pyscript in <py-script>, Py-script is mainly used for handling logic and recieving imported variables and functions from pure back-end python files while Javascript handles displaying information in HTML format. When the browser initially renders the page, pyscript is compiled first, then Javascript.
2. The py-script code first defines an object "pyodide globals" to allow exchange of objects and functions between python and javascript. It then tries to avoid SSL error with the browser by importing the SSL library.
3. Then, the web_search function is called which works by using the GET method from the Requests library to encode the url, required headers and parameters correctly to request a response from the Rapid Football API. The response variable mainly serves as a file handle and is not readible at the moment. Thus, the json.loads function is called to parse the text received from the API into convenient json structure.
4. The create_array function is imported from the main.py file to navigate through the JSON structure and identify the team name, form, points, and rank data and returns a list. The tabulate library then involves converting the list of data into tables with HTML format and syntax. The html_table variable then stores this HTML format and is passed towards the Javascript section.
5. Upon pressing the button "load it up", two JS functions are called: "stringToHtml" and "add_buttons". stringToHtml recieves the html_table variable from pyscript and converts the data type from string to html. Then the table is written on the "table" div. add_buttons sets the id of the newly displayed table as "standing" and therefore Javascript is able to iterate through each table row and display a button.
6. Each button in each row of the table is looped through once again and given a unique id from 0 to 49 (as there are 50 rows). As a button is clicked, the program navigates through the row of that specific button and stores the team name in the local storage of the browser.\\
**tweets.html and getTweets.py**\
1. getTweets.py constructs a twitter_client python object and defines several object functions such as filter_tweets, sentiment_analyzer, and get_tweets.
2. As the twitter_client object is imported to Javascript, the "main" function on tweets.html creates an instance of twitter_client named "Client" which is asked to communicate with the twitter api to utilize its query function to search for relevant tweets. The query string is the team name which is taken from the local storage stored by index.html.
3. After the query, the twitter api sends several responses containing text data of the tweet and some metadata but we are only interested in the text. Afterwards the filter_tweets function ensures that links and special characters are removed from the text.
4.    

### For Future Use
Note: This web app model is highly susceptible to syntax changes. 
- Pyscript => As previously mentioned, pyscript is still fairly new and is under constant heavy development and changes. For instance, I had to change the code from using pyscript.write functions to manually print strings to html into an Element('id').element.innerHTML function for future-proof issues. Other examples include the asyncio and await function.
- Twitter and Football API => Both API is also under development and the json structure to pull data might change in the future. The code assumes the Twitter v1.1 API and the v1 Rapid API.
