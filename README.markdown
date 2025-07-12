# Dubizzle Scraper

This project scrapes property listings from Dubizzle Egypt (apartments and duplexes for sale) and saves the data to an Excel file. The scraped information includes title, price, type, ownership, area, bedrooms, and bathrooms for each property.

## Project Structure
- `data/processed/`: Contains the output Excel file (`dubizzle_properties.xlsx`).
- `data/raw/`: Contains the scraped links (`dubizzle_links.txt`).
- `dubizzle_scraper/`: Source code for the scraping logic.
  - `config.py`: Configuration variables (e.g., base URL, headers).
  - `dataset.py`: Main scraping script.
  - `utils.py`: Utility functions for text cleaning.
- `requirements.txt`: Python dependencies.
- `setup.cfg`: Linting configuration for flake8.
- `LICENSE`: MIT License.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/dubizzle-scraper.git
   cd dubizzle-scraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scraper:
   ```bash
   python -m dubizzle_scraper.dataset
   ```

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies.

## Output
- Links are saved to `data/raw/dubizzle_links.txt`.
- Property details are saved to `data/processed/dubizzle_properties.xlsx`.

## Notes
- The script includes a 1-second delay between requests to avoid overwhelming the server.
- Ensure compliance with Dubizzle's terms of service before scraping.
- Update selectors in `dataset.py` if the website structure changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.