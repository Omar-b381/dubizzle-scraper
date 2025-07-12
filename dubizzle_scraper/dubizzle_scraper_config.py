# Configuration variables
BASE_URL = "https://www.dubizzle.com.eg/properties/apartments-duplex-for-sale/?page="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
MAX_PAGES = 200
OUTPUT_LINKS = "data/raw/dubizzle_links.txt"
OUTPUT_EXCEL = "data/processed/dubizzle_properties.xlsx"