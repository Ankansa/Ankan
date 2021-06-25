import requests

class myclass:
    data=[]
    def __init__(self,url):
        self.url = url


    def cost(self):
        r = requests.get(self.url)  # For fetch html from the mentioned url
        html = r.text  # for html to txt

        b = str(html)

        t = b.split(">")  # Split html with > for get ₹123<dev/ from >₹123<dev
        for i in t:
            if i.startswith("₹"):  # Scarch on html text which text start with ₹

                m = i.split("<")  # Split with < for getting ₹123
                price = (m[0].split("₹"))  # Split with ₹ for get 123
                final_price = (price[1])  # For convert string to int
                pure_price = final_price.replace(",", "")
                print("Product stating price is : ",pure_price)
                myclass.data.append(pure_price)

                break


    def run(self):
        day="Start"

        while day == "Start":
            r2 = requests.get(self.url)  # For fetch html from the mentioned url
            html2 = r2.text  # for html to txt

            b2 = str(html2)

            t2 = b2.split(">")  # Split html with > for get ₹123<dev/ from >₹123<dev
            for i2 in t2:
                if i2.startswith("₹"):  # Scarch on html text which text start with ₹

                    m2 = i2.split("<")  # Split with < for getting ₹123
                    price2 = (m2[0].split("₹"))  # Split with ₹ for get 123
                    final_price2 = (price2[1])  # For convert string to int
                    pure_price2 = final_price2.replace(",", "")
                    if int(myclass.data[0])>int(pure_price2):
                        print("Price is : ",pure_price2)
                    break


ob=myclass(input("Please enter the flipkart product link hear : "))

ob.cost()

ob.run()

# Massage sending feature is not added in this code. Because this API is chergeba. I dont get any free API for this operation.
