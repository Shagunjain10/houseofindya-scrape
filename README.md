# houseofindya-scrape

This is `Jewelry Product Web Scraper` build using `scrapy` module of `python`.


# Features
It extracts the following:

  * Jewelry Description
  * Jewelry Price
  * Jewelry Image Url
  * Necklace Description
  * Necklace Price
  * Necklace Image Url
# website url
[https://www.houseofindya.com/](https://www.houseofindya.com/)

[https://www.houseofindya.com/zyra/](https://www.houseofindya.com/zyra/)

[https://www.houseofindya.com/zyra/necklace/cat](https://www.houseofindya.com/zyra/necklace/cat)

# Setup  scraper
1. Create Virtual Environment
   - ```virtualenv projectname```
2. Clone this repo
   - ```git clone https://github.com/Shagunjain10/houseofindya_scrape.git```
3. Change directory
    - ```cd houseofindya_scrape```
4. Run requirements.txt file
   - ```pip install -r requirements.txt```

### Run the following command for generate a JSON file
```
scrapy crawl list_of_necklace -o NecklaceList.json
```
It will create `JewelryList.json` json file.

### Run the following command for generate a CSV file
```
scrapy crawl list_of_necklace -o NecklaceList.csv
```
### Run the following command for generate a CSV file for scrape the all jewelry page
```
scrapy crawl list_of_jewelry -o jewelryList.csv
scrapy crawl list_of_jewelry -o JewelryList.json
```

It will create `JewelryList.json` csv file.
