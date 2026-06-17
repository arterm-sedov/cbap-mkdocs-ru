import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# URL of the webpage to check
URL = 'https://disk.comindware.ru/CBAP/4.7/Astra/'

def fetch_page(url):
    """Fetches the webpage content."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve data, status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching the page: {e}")
        return None

def get_new_files(html_content):
    """Extracts new files with a date later than yesterday."""
    soup = BeautifulSoup(html_content, 'html.parser')
     # Find the table with id="list"
    table = soup.find('table', id='list')
    if not table:
        print("Table with id='list' not found.")
        return []

    rows = table.find_all('tr')


    # Get yesterday's date for comparison
    yesterday = datetime.now() - timedelta(days=1)
    new_files = []

    # Loop through each row in the table to find file details
    for row in rows:
        columns = row.find_all('td')
        if len(columns) < 3:
            continue
       
        file_name = columns[0].text.strip()
        file_date_str = columns[2].text.strip()
        if file_name == 'Parent directory/':
            continue
        # Convert the date string to a datetime object
        try:
            file_date = datetime.strptime(file_date_str, '%Y-%b-%d %H:%M')
        except ValueError:
            continue  # Skip rows where the date is not in the expected format
        
        # Check if the file's date is later than yesterday
        if file_date < yesterday:
            new_files.append(file_name)
    
    return new_files

def main():
    """Main function to fetch and check for new files."""
    html_content = fetch_page(URL)
    if not html_content:
        return

    new_files = get_new_files(html_content)
    
    if new_files:
        # Print file names, this will be captured by the shell script
        print("New files found:")
        for file in new_files:
            print(file)
    else:
        print("No new files found.")

if __name__ == "__main__":
    main()
