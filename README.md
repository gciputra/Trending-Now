# Trending-Now
Adopting NLP text processing methods to analyze tweet sentiments on Premier League teams | Made with Pyscript and Javascript

### View the application demo [here]({link})

### How to Run:
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
Flow of code:


### For Future Use
Note: This web app model is highly susceptible to syntax changes. 
- Pyscript => As previously mentioned, pyscript is still fairly new and is under constant heavy development and changes. For instance, I had to change the code from using pyscript.write functions to manually print strings to html into an Element('id').element.innerHTML function for future-proof issues. Other examples include the asyncio and await function.
- Twitter and Football API => Both API is also under development and the json structure to pull data might change in the future. The code assumes the Twitter v1.1 API and the v1 Rapid API.
