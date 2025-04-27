# GDP Scraper

This project scrapes GDP data from the Wikipedia page on the list of countries by GDP (nominal) and saves it in a CSV file. It also provides data analysis and visualization.

## Features
- Scrape GDP data by country from Wikipedia
- Save the data to a CSV file
- Data cleaning and analysis using Python
- Visualization of the top countries by GDP

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`
- `matplotlib`
- `seaborn`

## How to Run

1. Clone the repository:
git clone https://github.com/kavitsheth/GDP_Scraping_Project.git

markdown
Copy
Edit

2. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

3. Run the scraper:
python gdp_scraper.py

markdown
Copy
Edit

4. Analyze the data:
Open the Jupyter notebook `notebooks/gdp_analysis.ipynb` and run the analysis.

## Output
- The GDP data is saved to `gdp.csv` in the `data/` directory.
- The analysis results will be shown in the Jupyter notebook.

## License
This project is licensed under the MIT License.