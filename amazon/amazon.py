import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36'
        # Use a user-agent header to mimic a specific browser (Chrome 119.0.6045.160 in this case)
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extracting product name
            product_name = soup.find(id='productTitle').get_text().strip()

            # Extracting product price
            price = soup.find(id='corePriceDisplay_desktop_feature_div').get_text().strip()

            return {'Product Name': product_name, 'Product Price': price}
        else:
            print(f"Failed to fetch data from Amazon. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
amazon_url = 'https://www.amazon.in/iQOO-MediaTek-Dimesity-Processor-Smartphone/dp/B07WGPJPR3/?_encoding=UTF8&pd_rd_w=ghs0w&content-id=amzn1.sym.aff93425-4e25-4d86-babd-0fa9faf7ca5d%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=aff93425-4e25-4d86-babd-0fa9faf7ca5d&pf_rd_r=G81YVXJCN38XKSZXY3XJ&pd_rd_wg=xP27a&pd_rd_r=7887e8b7-b072-44f9-9756-d4e58af5c263&ref_=pd_gw_ci_mcx_mr_hp_atf_m'  # Replace with the desired Amazon product URL
result = scrape_amazon_product(amazon_url)
if result:
    print("Amazon Product Details:")
    print(f"Name: {result['Product Name']}")
    print(f"Price: {result['Product Price']}")
else:
    print("Failed to fetch Amazon product details.")
