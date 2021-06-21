import requests

def track_price():
    url = input("Please enter the flipkart product link hear : ")
    r = requests.get(url)  # For fetch html from the mentioned url
    html = r.text  # for html to txt

    b = str(html)

    t = b.split(">")  # Split html with > for get ₹123<dev/ from >₹123<dev

    for i in t:
        if i.startswith("₹"):  # Scarch on html text which text start with ₹

            m = i.split("<")  # Split with < for getting ₹123
            price = (m[0].split("₹"))  # Split with ₹ for get 123
            final_price = (price[1])  # For convert string to int
            print("The product price is : " + final_price)
            break


track_price()