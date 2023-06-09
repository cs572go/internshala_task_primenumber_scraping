#  internshala_task_primenumber_scraping
This task is a web scraper that extracts data from the Quest CDN website (https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787). 
It uses Selenium WebDriver with Chrome to automate the scraping process.
To get started follow the instructions below.

## Getting Started

Prerequisites are: 

Python 3.9,
pandas 2.0.2,
selenium 4.10.0, and
Chrome web browser.




## Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/cs572go/internshala_task_primenumber_scraping
```
2. Install the required Python packages using pip:
```
pip install -r requirements.txt
```


## Usage
1. Update the 'count' variable in the 'main.py' file to specify the number of rows to scrape from the website.
2. Run the script:
```
python main.py
```
## Output
The output CSV file (scrapper_data.csv) will contain the following columns:

1. SrNo: Serial number of the scraped item
2. Quest no: Quest number of the item
3. Est. Value Notes: Estimated value notes for the item
4. Description: Description of the item
5. Due Date: Closing date of the item
