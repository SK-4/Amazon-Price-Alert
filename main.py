import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = "https://www.amazon.in/LASER-WINGS-Cotton-Bedsheet-Stripes/dp/B09F3HN49N/ref=sr_1_1_sspa?pd_rd_r=70ad5544-df16-427b-9eb6-0438aa84e181&pd_rd_w=Ysk8X&pd_rd_wg=CLG0a&pf_rd_p=1f2380ba-33d6-4bbb-8271-6f3b3e3e2d6f&pf_rd_r=BX52SGQWADMWP9EHNC1D&qid=1650427975&refinements=p_n_material_browse%3A3249381031&s=kitchen&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRlBLTlRTUEg5SzA1JmVuY3J5cHRlZElkPUEwNjcxNDYwM1FROFROUzVROTRZRiZlbmNyeXB0ZWRBZElkPUEwMzIzNTc3MzVDVkJOMVExVVdYJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url=f"{PRODUCT_URL}",headers=headers)
website  = response.text

soup =  BeautifulSoup(website,"lxml")

price_with_comma = soup.find(name="span",class_="a-offscreen").getText().split("₹")[1]
product_price = float(price_with_comma.replace(",",""))
print(product_price)

title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 800
my_email = "sk2587359@gmail.com"
password =  "rockybhai7"

if product_price < BUY_PRICE:
    message = f"{title} is now cheaper {product_price}, go buy it here :{PRODUCT_URL}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kshirsagarsoham1@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )

print("You Did It!!!")