import requests
from bs4 import BeautifulSoup

# Aamzon product URL


# Function to fetch and print the price

url = "https://www.amazon.in/FUJIFILM-X-H2-Mirrorless-Camera-16-80mm/dp/B0BCM562BH/ref=sr_1_1_sspa?crid=13P5TCOB3YRRC&dib=eyJ2IjoiMSJ9.a4T6d1rg5XsNaBhPXauTVU-87p1j0GUHl7X28T54yDfy14oNp8y11E1TQuJx7iYUoyIr7RQurEPRxAK1vFcPyKl7W5lQD_QtWexgsdzgG2ng0AvS2FXQhQYPYNIA4A7y0OzazJXqv5x9f0bBJybfMo5AZe1TrgVF5Gr2hjI2NviEEOLpbwOJT3-cYnnPwpnL5Y5jAJJlme4fjPYUIgpvgwsDv-TzacHH9yNgVlmX-l8.uBcJCBBEnxptnMPqVRb3EGfXZSVm2ODNHbLAkSP1GYQ&dib_tag=se&keywords=dslr&qid=1733666425&sprefix=dsl%2Caps%2C402&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    # Send the request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
   
    # Look for the price on the page
price_element = soup.find("span", {"class": "a-price-whole"}) 
 
if price_element :
    price = price_element.get_text().strip() 
    print(f"The current price of the product is ₹{price}")
else:
    print("Price not found. The structure of the page might have changed.")
price = price_element.get_text().strip() 
# Call the function
expected=input("Enter desired price:")
def email_send():
    import smtplib
    import getpass

    host = "smtp.gmail.com"
    port = 587
    from_email = "aryansuryawanshi4737@gmail.com"
    to_email = "amazontracker12@gmail.com"
    password = getpass.getpass("Enter password")
    Message = f"Subject:Price has fallen down please check={url}"

    smtp = smtplib.SMTP(host, port)
    status_code, response = smtp.ehlo()
    print(f"{status_code}, {response}")
    status_code, response = smtp.starttls()
    print(f"{status_code}, {response}")
    status_code, response = smtp.login(from_email, password)
    print(f"{status_code}, {response}")
    smtp.sendmail(from_email, to_email, Message)
    smtp.quit()
if expected>price:
    email_send()
    print("Mail has been sent succesfully")
else:
    print("Error")

