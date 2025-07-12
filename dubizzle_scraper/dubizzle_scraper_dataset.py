import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from .config import BASE_URL, HEADERS, MAX_PAGES, OUTPUT_LINKS, OUTPUT_EXCEL
from .utils import clean_text

def scrape_property_details(url):
    """Scrape property details from a single URL."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')

        data = {}
        data['URL'] = url
        data['Title'] = clean_text(soup.find('h1').text) if soup.find('h1') else None
        data['Price'] = clean_text(soup.find('span', class_='_24469da7').text) if soup.find('span', class_='_24469da7') else None
        data['Type'] = clean_text(soup.find('span', class_='_8206696c b7af14b4').text) if soup.find('span', class_='_8206696c b7af14b4') else None

        selectors = {
            'Ownership': '#body-wrapper > div._948d9e0a._95d4067f._1e086faf._4122130d > header:nth-child(3) > div > div._948d9e0a._4122130d > div > div.bbda9e25 > div._7a14a9fe > div:nth-child(2) > div > div:nth-child(2) > div > span._8206696c.b7af14b4',
            'Area': '#body-wrapper > div._948d9e0a._95d4067f._1e086faf._4122130d > header:nth-child(3) > div > div._948d9e0a._4122130d > div > div.bbda9e25 > div._7a14a9fe > div:nth-child(2) > div > div:nth-child(3) > div > span._8206696c.b7af14b4',
            'Bedrooms': '#body-wrapper > div._948d9e0a._95d4067f._1e086faf._4122130d > header:nth-child(3) > div > div._948d9e0a._4122130d > div > div.bbda9e25 > div._7a14a9fe > div:nth-child(2) > div > div:nth-child(4) > div > span._8206696c.b7af14b4',
            'Bathrooms': '#body-wrapper > div._948d9e0a._95d4067f._1e086faf._4122130d > header:nth-child(3) > div > div._948d9e0a._4122130d > div > div.bbda9e25 > div._7a14a9fe > div:nth-child(2) > div > div:nth-child(5) > div > span._8206696c.b7af14b4'
        }

        for key, selector in selectors.items():
            element = soup.select_one(selector)
            data[key] = clean_text(element.text) if element else None

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

def main():
    """Scrape property listings and save to Excel."""
    all_links = []

    # Step 1: Scrape all links
    for page in range(1, MAX_PAGES + 1):
        url = BASE_URL + str(page)
        print(f"Scraping page {page}: {url}")
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code != 200:
                print(f"Failed to fetch page {page}, status code: {response.status_code}")
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            listing_divs = soup.find_all('div', class_='_70cdfb32')
            
            for div in listing_divs:
                a_tag = div.find('a', href=True)
                if a_tag:
                    relative_link = a_tag['href']
                    full_link = 'https://www.dubizzle.com.eg' + relative_link
                    all_links.append(full_link)
            
            time.sleep(1)

        except Exception as e:
            print(f"Error on page {page}: {e}")
            continue

    print(f"Extracted {len(all_links)} links from {MAX_PAGES} pages.")

    # Save links to file
    with open(OUTPUT_LINKS, "w", encoding="utf-8") as f:
        for link in all_links:
            f.write(link + "\n")

    # Step 2: Scrape details from each link
    all_data = []
    for i, link in enumerate(all_links, 1):
        print(f"Scraping property {i}/{len(all_links)}: {link}")
        property_data = scrape_property_details(link)
        if property_data:
            all_data.append(property_data)
        time.sleep(1)

    # Step 3: Save to Excel
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_excel(OUTPUT_EXCEL, index=False)
        print(f"Saved {len(all_data)} properties to '{OUTPUT_EXCEL}'")
    else:
        print("No data to save.")

if __name__ == "__main__":
    main()