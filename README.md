# Page-Scraper
This is a Python based web scraper designed particularly for scraping information about students <br> 
clearing Google Summer of Code in the past years. It collects the name, organisation and project<br>
details of each successful candidate which is available on Google's official webpage: https://summerofcode.withgoogle.com<br> 
and stores it in a ```.csv``` file.<br>
It further compares the obtained data with the student database in ```.json``` format and returns<br>
the name of the relevant matches. 
<br>
## Important Stuff
- This requires Python ```3.x``` installed on your system along with the BeautifulSoup4 and Requests library.
- In case you don't have the above mentioned dependencies, then follow the given installation steps:<br>
```
sudo apt install python
sudo apt install pip
pip install beautifulsoup4 requests
```


## How to Use
- Download the repository in your local machine. Make sure you have all the dependencies installed.
- You might want to create a different .csv file for storing the data. If this is the case, then change<br>
the file name in scraper.py and accordingly in check.py.
- To provide a diiferent JSON database, copy the .json file to the same directory as that of check.py <br> 
and accordingly change the name in check.py( scraper.py remains unchanged).
- Finally, run the python file in your terminal using the following commands.
```python
python scraper.py
```


