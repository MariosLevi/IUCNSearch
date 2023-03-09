# IUCNSearch
Scraper to go through the IUCN's list of fungi and see if there are any of commercial value

# Introduction
This script checks whether a list of species from the IUCN Red List of Threatened Species have the keywords 'edible' or 'commercial value' in their species information pages, and also retrieves their IUCN conservation status. The results are saved to a CSV file named 'results.csv'.

# Installation
Clone this repository or download the script.
Install the required libraries: pip install requests beautifulsoup4

# Usage
Go to the IUCN website and apply the filters you want to use to find wanted fungi.
Copy the page source of the resulting page.
Save the page source to a file on your computer (e.g. "vulnerable1.html")
Open the command prompt or terminal and navigate to the directory containing the script.
Run the script: python listmaker.py
Copy and paste the generate list of mycobank ID's into the urls variable on IUCNAnalyzer
Run the script: python IUCNAnalyzer.py
Wait for the script to finish running. The results will be saved to a file named 'results.csv' in the same directory as the script.

# Contributing
Feel free to submit pull requests or open issues if you find any bugs or have any suggestions.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
