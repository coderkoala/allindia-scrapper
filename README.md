# allindiaexams.in Scraper


 A tiny python script I made in behalf of Gurkha Technology Inhouse for minimizing digitizing efforts for questions. It simply scrapes the in the following format:
 
 | Question  |Answer | Option A |Option B |Option C |Option D | Option E|
| ------------- | ------------- |------------- |------------- |------------- |------------- |------------- |
| Who is Ram's father?  | B |Nirajan  | Dasharath | Sita  | Surya  | Maisasur |
 
 
 Installation of Python
 ---
 
 - Make sure to install `python 3` and `pip`

##### Windows:
[Install Python here](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe)

##### Linux:
[Follow the instructions here](https://itsfoss.com/python-setup-linux/)


 Installation of Git
 ---
 
 - Make sure to install `python 3` and `pip`

##### Windows:
[Install Git here](https://git-scm.com/downloads)

##### Linux:
Simply use command line git that is already included. If not, use:

`sudo apt-get install git`

---

 ##### Initial installation
 
 Setting up your script installtion folder
 ```
 git clone https://github.com/coderkoala/python-scraper.git scraper
 cd scraper
 python3 -m venv venv
 . ./venv/bin/activate
 ```
 
 After that, it's just a matter of installing dependencies
 ```
 pip install -r requirements.txt 
 ```
 ---
 ##### Running the script to scrape
 
 Make sure to have an `allindiaexams.in` web url you wish to ready.
 
 **Simply run: `python3 scrapper.py`** 
 
 
 
