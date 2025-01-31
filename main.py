import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import csv

count = 0


# website_to_scrape = input("What is the full link to the website? ")


poke_db = "https://pokemondb.net/pokedex/national"

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(poke_db)

pokemon_names = driver.find_elements(By.CSS_SELECTOR, value=".infocard span a")

# print(pokemon_names)

text = []

for name in pokemon_names:
    text.append(name.text)

only_text = []


with open("pokemon.csv", mode='w', encoding='utf-8') as file:
    file.write("Index,Name,Type1,Type2")
    for n in text:
        if n == '':
            file.write(f"\n{count + 1},")
            count += 1
        else:
            file.write(f"{n},")

driver.quit()