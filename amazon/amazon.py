import requests
from bs4 import BeautifulSoup


def get_amazon_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.200 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            product_name = soup.find('span', id='productTitle').get_text().strip()
            product_price = soup.find('span', class_='a-offscreen').get_text().strip()
            return {'Product Name': product_name, 'Product Price': product_price}
        else:
            print(f"Failed to fetch data from Amazon. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return None

def get_snapdeal_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.200 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            product_name = soup.find_all('h1', class_='pdp-e-i-head')
            titles = []
            for h1_tag in product_name:
                title = h1_tag.get('title')
                if title:
                    titles.append(title)
            product_price = soup.find('span', class_='payBlkBig', itemprop='price')
            price = product_price.get_text(strip=True)
            return {'Product Name': title, 'Product Price': price}
        else:
            print(f"Failed to fetch data from snapdeal. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {str(e)}")
        return None
    
# Amazon URL
amazon_url = 'https://www.amazon.in/iQOO-MediaTek-Dimesity-Processor-Smartphone/dp/B07WGPJPR3/?_encoding=UTF8&pd_rd_w=ghs0w&content-id=amzn1.sym.aff93425-4e25-4d86-babd-0fa9faf7ca5d%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=aff93425-4e25-4d86-babd-0fa9faf7ca5d&pf_rd_r=G81YVXJCN38XKSZXY3XJ&pd_rd_wg=xP27a&pd_rd_r=7887e8b7-b072-44f9-9756-d4e58af5c263&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

# Snapdeal URL
snapdeal_url = 'https://www.snapdeal.com/product/asian-tan-running-shoes/7493990459833733520'


# Get Amazon product details
amazon_product_info = get_amazon_product_info(amazon_url)
if amazon_product_info:
    print("\nAmazon Product Details:")
    print(f"Name: {amazon_product_info['Product Name']}")
    print(f"Price: {amazon_product_info['Product Price']}")
else:
    print("Failed to fetch Amazon product details.")

# Get Snapdeal product details
snapdeal_product_info = get_snapdeal_product_info(snapdeal_url)
if snapdeal_product_info:
    print("\nsnapdeal Product Details:")
    print(f"Name: {snapdeal_product_info['Product Name']}")
    print(f"Price: ₹{snapdeal_product_info['Product Price']}")
else:
    print("Failed to fetch snapdeal product details.")


