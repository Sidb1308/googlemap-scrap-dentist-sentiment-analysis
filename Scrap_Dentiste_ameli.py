from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 

#Create an instance of the Chrome browser.

path="/Users/mac/Desktop/chromedriver"
service= Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Open Google Maps
driver.get("https://annuairesante.ameli.fr/trouver-un-professionnel-de-sante/chirurgiens-dentistes/68-haut-rhin-mulhouse")

# Wait for the page to load
time.sleep(2)
noms_dentistes = []
adresses_dentistes = []
while True:
    # Searching for all elements containing the names of dentists on the current page
    nom_dentists = driver.find_elements(By.CLASS_NAME, 'nom_pictos')
    adress = driver.find_elements(By.CLASS_NAME, 'item.left.adresse')
    
    
    # Printing the names of dentists on the current page"
    for dentist,adress in zip( nom_dentists,adress):
        
        noms_dentistes.append(dentist.text)
        adresses_dentistes.append(adress.text)
    
    # Finding the element corresponding to the next page
    try:
        page_suivante = driver.find_element(By.XPATH, '//a[./img[contains(@alt, "Page suivante")]]')
        
        #If the element for the next page is found, click on it to navigate to the next page."
        page_suivante.click()
        
        # Waiting for a few seconds for the new page to fully load
        time.sleep(2)
    except NoSuchElementException:
        # If the element for the next page is not found, it means we have reached the last page
        break
    
df = pd.DataFrame({
    "Nom du dentiste": noms_dentistes,
    "Adresse du dentiste": adresses_dentistes
})

# Saving the DataFrame to a CSV file
df.to_csv("dentistes_mulhouse.csv", index=False)

    


    
