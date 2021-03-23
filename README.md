# houseofindya-scrape

This is `Jewelry Product Web Scraper` build using `scrapy` module of `python`.


# Features
It extracts the following:

  * Jewelry Description
  * Jewelry Price
  * Jewelry Image Url
# website url
[https://www.houseofindya.com/](https://www.houseofindya.com/)

[https://www.houseofindya.com/zyra/](https://www.houseofindya.com/zyra/)
# Setup  scraper
1. Create Virtual Environment
   - ```virtualenv projectname```
2. Clone this repo
   - `` git clone https://github.com/Shagunjain10/houseofindya_scrape.git```
3. Change directory
    - ```cd houseofindya_scrape```
4. Run requirements.txt file
   - ```pip install -r requirements.txt```

### Run the following command for generate a JSON file
```
scrapy crawl list_of_necklace -o JewelryList.json
```
It will create `JewelryList.json` [json file](https://github.com/Shagunjain10/houseofindya_scrape/blob/main/JewelryList.json).

### Run the following command for generate a CSV file
```
scrapy crawl list_of_necklace -o jewelryList.csv
```

It will create `JewelryList.json` [csv file](https://github.com/Shagunjain10/houseofindya_scrape/blob/main/jewelryList.csv).
