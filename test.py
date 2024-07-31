import requests
from bs4 import BeautifulSoup

def print_grid_from_url(url):
    # Step 1: Fetch the data from the URL
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    table = bs.find("table")
    rows = table.find_all('tr')

    # Step 2: Parse the data
    characters = []
    max_x = max_y = 0

    for row in rows:
        try:
            parts = row.find_all('span')
            char, x, y = parts[1].text, int(parts[0].text), int(parts[2].text)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            characters.append((char, x, y))            
        except: 
            print('Data input issue')

    # Step 3: Initialize the grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Step 4: Fill the grid with characters
    for char, x, y in characters:
        grid[max_y-y][x] = char
    
    # Step 5: Print the grid
    for row in grid:
        print(''.join(row))

# Example usage:
# print_grid_from_url('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub')
print_grid_from_url('https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub')
