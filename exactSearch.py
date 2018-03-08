from urllib.request import urlopen
import sys
import bs4
import webbrowser
import requests

def exactS(SearchString):

    '''This method takes the Search String as input and finds the exact match of the String 
        in Flipkart and Amazon and returns the result.'''

    results = ""
    WordArray = SearchString.split(' ')
    NoOfWords = len(WordArray)

    html = requests.get("https://www.flipkart.com/search?q="+SearchString)
    html.raise_for_status()
    bs = bs4.BeautifulSoup(html.text,"html.parser")
    

    try:
        names = bs.find_all("a",{"class":"_2cLu-l"})
        itemName = names[0].get_text().split(' ')
    except IndexError:
        names = bs.find_all("div",{"class":"_3wU53n"})      
        itemName = names[0].get_text().split(' ')

    prices = bs.find_all("div",{"class":"_1vC4OE"})

    cnt=0
    for word in WordArray:
        for itemword in itemName[:NoOfWords+1]:
          if word.upper()==itemword.upper():
            cnt+=1
    

    if cnt/NoOfWords > .6:
        results = results + "Flipkart : \t " + names[0].get_text() + ":\t" + prices[0].get_text() + "\n"

        
        
    res = requests.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + SearchString)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,"html.parser")

    names = soup.find_all("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
    itemName = names[0].get_text().split(' ')
    '''for i in itemName:
        print(i)'''

    prices = soup.find_all("span",{"class":"a-size-base a-color-price s-price a-text-bold"})

    cnt = 0
    for word in WordArray:
        for itemword in itemName[:NoOfWords+1]:
            if word.upper() == itemword.upper():
                cnt+=1


    if cnt/NoOfWords > .6:
            results = results + "Amazon : \t " + names[0].get_text() + "\t" + prices[0].get_text() + "\n"

    return results

if __name__ == "__main__":
    SearchString = ""
    if len(sys.argv) > 1:
        SearchString = (' ').join(sys.argv[1:])

    results = exactS(SearchString)
    print(results)
















