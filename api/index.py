from http.server import BaseHTTPRequestHandler

# import requests
# import traceback
# from bs4 import BeautifulSoup

PRODUCT_ID = 'B0B6NRZFVD';

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # soup = fetch_html_from_amz_url(PRODUCT_ID)
    
        # price_element = soup.find(class_='twister-plus-buying-options-price-data')
        # buybox_json = json.loads(price_element.get_text())
        # buybox_price_json = buybox_json['desktop_buybox_group_1'][0]

        # print(buybox_price_json['priceAmount'])
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('buybox_price_json'.encode('utf-8'))
        return


# # Function to fetch HTML content from a URL
# def fetch_html_from_amz_url(product_id):
#     url = 'https://www.amazon.in/gp/product/' + product_id
#     # Define user-agent header to simulate a browser request
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Connection': 'keep-alive'
#     }
#     print(f'Fetching URL :: {url}')

#     # Send an HTTP GET request with headers
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')
#         return soup
#     else:
#         print('Failed to fetch the web page. Status code:', response.status_code)
#         return None
