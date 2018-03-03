import requests,bs4

x='https://www.flipkart.com/search?q='
y='&otracker=start&as-show=on&as=off'

print("Input the search string")
search=input()

res = requests.get(x+str(search)+y)
res.raise_for_status()

soup1 = bs4.BeautifulSoup(res.text,"html.parser")
soup2 = bs4.BeautifulSoup(res.text,"html.parser")
names = soup1.find_all("a",{"class":"_2cLu-l"})
prices = soup2.find_all("div",{"class":"_1vC4OE"})


print("Flipkart's results")
count = 0
for name,price in zip(names,prices):
    if(count<5):
        print(name.get_text() + "\t" + "Rs" + price.get_text())
        count=count+1
    else:
        break


x = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Delectronics&field-keywords='
res = requests.get(x+str(search))
res.raise_for_status()

soup1 = bs4.BeautifulSoup(res.text,"html.parser")
soup2 = bs4.BeautifulSoup(res.text,"html.parser")
names = soup1.find_all("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
prices = soup1.find_all("span",{"class":"a-size-base a-color-price s-price a-text-bold"})
print("Amazon's results")
count=0
for name,price in zip(names,prices):
    if(count<5):
        print(name.get_text() + "\t" + "Rs" + price.get_text())
        count=count+1
    else:
        break


x = 'https://www.snapdeal.com/search?keyword='
res = requests.get(x+str(search))
res.raise_for_status()

soup1 = bs4.BeautifulSoup(res.text,"html.parser")
soup2 = bs4.BeautifulSoup(res.text,"html.parser")
names = soup1.find_all("p",{"class":"product-title"})
prices = soup2.find_all("span",{"class":"lfloat product-price"})

print("Snapdeal's results")
count=0
for name,price in zip(names,prices):
    if(count<5):
        print(name.get_text() + "\t" + price.get_text())
        count = count+1
    else:
        break


