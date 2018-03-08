import requests,bs4


def generalS(search):

    '''This method takes the Search String as input and returns the first 5 results of 
       the string in Flipkart, Amazon and Snapdeal.''' 

    x='https://www.flipkart.com/search?q='
    y='&otracker=start&as-show=on&as=off'

    res = requests.get(x+str(search)+y)
    res.raise_for_status()

    soup1 = bs4.BeautifulSoup(res.text,"html.parser")
    soup2 = bs4.BeautifulSoup(res.text,"html.parser")
    names = soup1.find_all("a",{"class":"_2cLu-l"})
    prices = soup2.find_all("div",{"class":"_1vC4OE"})

    results = ""
    results = results + "Flipkart's results : \n"
    count = 0
    for name,price in zip(names,prices):
        if(count<5):
            results = results + name.get_text() + "\t" + "Rs" + price.get_text() + "\n"
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
    results = results + "Amazon's results : " + "\n"
    count=0
    for name,price in zip(names,prices):
        if(count<5):
            results = results + name.get_text() + "\t" + "Rs" + price.get_text() + "\n"
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

    results = results + "Snapdeal's results : " + "\n"
    count=0
    for name,price in zip(names,prices):
        if(count<5):
            results = results + name.get_text() + "\t" + price.get_text() + "\n"
            count = count+1
        else:
            break
    return results

if __name__ == '__main__':
    print("Input the search string")
    SearchString = input()
    results = ""
    results = generalS(SearchString)
    print(results)