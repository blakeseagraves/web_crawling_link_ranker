from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import operator
import statistics

def getLinks(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page, "lxml")
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))

    return links

websites = [
"https://us.cnn.com/",
"https://www.nytimes.com/",
"https://www.foxnews.com/",
"https://www.usatoday.com/",
"https://www.reuters.com/news/us",
"https://www.politico.com/",
"https://www.yahoo.com/news/",
"https://www.npr.org/",
"https://www.latimes.com/california",
"https://www.breitbart.com/",
"https://nypost.com/",
"https://www.nbcnews.com/",
"https://abcnews.go.com/",
"https://www.cbsnews.com/",
"https://washington.cbslocal.com/",
"https://tampa.cbslocal.com/",
"https://sanfrancisco.cbslocal.com/",
"https://boston.cbslocal.com/",
"https://philadelphia.cbslocal.com/",
"https://chicago.cbslocal.com/",
"https://losangeles.cbslocal.com/",
"https://dfw.cbslocal.com/",
"https://detroit.cbslocal.com/",
"https://minnesota.cbslocal.com/",
"https://newyork.cbslocal.com/",
"https://www.nydailynews.com/",
"https://www.chicagotribune.com/",
"https://www.denverpost.com/",
"https://www.boston.com/",
"https://www.seattletimes.com/",
"https://www.mercurynews.com/",
"https://www.theonion.com/",
"https://abc7news.com/tag/music/",
"https://chicago.suntimes.com/",
"https://ktla.com/",
"https://observer.com/",
"https://gothamist.com/",
"https://abc13.com/",
"https://wtop.com/",
"https://wgntv.com/",
"https://www.kxan.com/",
"https://www.seattlepi.com/",
"http://brooklyn.news12.com/",
"https://www.bostonherald.com/",
"https://www.wfla.com/",
"https://www.twincities.com/",
"https://www.kron4.com/",
"https://www.westword.com/",
"https://wsvn.com/news/",
"https://kdvr.com/",
"https://www.phillyvoice.com/",
"https://fox5sandiego.com/",
"https://fox2now.com/",
"https://www.pe.com/",
"https://www.miaminewtimes.com/",
"https://arlington.wickedlocal.com/",
"https://www.phoenixnewtimes.com/",
"https://whdh.com/",
"https://www.minnpost.com/",
"https://www.riverfronttimes.com/",
"https://www.wivb.com/",
"https://www.chicagoreader.com/",
"https://www.metrotimes.com/",
"https://www.houstonpress.com/",
"https://billypenn.com/",
"https://citylimits.org/",
"https://newrightnetwork.com/",
"https://atlantaintownpaper.com/",
"https://boltposts.com/",
"https://www.miamitodaynews.com/",
"http://www.foresthillstimes.com/",
"https://spooknews.com/",
"https://www.pridepublishinggroup.com/pride/",
"https://www.wokepatriots.com/",
"http://marketprimenews.com/",
"https://www.nbcnewyork.com/",
"https://www.nbcchicago.com/",
"https://www.nbclosangeles.com/",
"https://www.nbcsandiego.com/",
"https://www.nbclosangeles.com/",
]


web_crawled_links = []

for website in websites:
    web_crawled_links.extend(getLinks(website))


short_web_crawled_links = []
for link in web_crawled_links:
    short_web_crawled_links.append(link.split('.com', 1)[0] + '.com')

def getDuplicatesCount(short_web_crawled_links):
    links_dict = dict()

    for link in short_web_crawled_links:
        if link in links_dict:
            links_dict[link] += 1
        else:
            links_dict[link] = 1    
 
    return links_dict

sorted_list = dict(sorted((getDuplicatesCount(short_web_crawled_links)).items(), key=operator.itemgetter(1)))

median = statistics.median(sorted_list.values())

top_links = []
bottom_links = []

for key in sorted_list:
    if sorted_list[key] >= median:
        top_links.append(key)
    else:
        bottom_links.append(key)

print("above median links:", top_links)
print('------------------------------------------------------')
print("below median links:", bottom_links)
