# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random
import bs4
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

def enterFilename(text):
    filename = raw_input("Enter "+ text + " filename: ")
    
    filenames = filename.split(".")
    filename = filenames[0] + ".csv"

    return filename

def openFiles(filenameCSV, filenameAddInfo):
    #filename = "deepScrapedBipartite_1.csv"
    f = open(filenameCSV, "w")

    #filenameNodes = "deepScrapedNodesBipartite_1.csv"
    t = open(filenameAddInfo, "w")

    headers = "url; titolo; autore; rating; prezzo\n"

    t.write(headers)

    return f, t


def closeFile(f, t):
    f.close()
    t.close()

def scraping(my_url, old_url, n, f, t):
    n=n+1
    print ("n: " + str(n))
    navigator = []
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    authors = page_soup.find_all("span", class_="visible-contributors")
    author = authors[0].a.string.encode("utf-8")
    containers = page_soup.findAll("div",{"class":"item-container"})
    #container = containers[0]
    #title_container = container.div.findAll("div",{"class":"notranslate_title"})
    #i = 0
    for container in containers:
        title_container = container.find_all("div", class_="book-detail-line")
        title = str(title_container[0].p.string.encode("utf-8"))
        title_url = container.find_all("a", class_="notranslate_title")
        url = title_url[0]["href"]
        autori = container.find_all("span", class_="contributor-name")
        autore =  str(autori[0].string.encode("utf-8"))   
        ratings = container.find_all("div", class_="star-rating")
        if ratings:
            rating =  ratings[0]["aria-label"]
            splited_rating = rating.split(" ")
            rating = str(splited_rating[1])
        else:
            rating = "null"
        prezzi = container.find_all("p", class_="price")
        try:
            prezzo =  str(prezzi[0].span.span.string.encode("utf-8"))
        except:
            prezzo = "gratis"
        header_url="https://www.kobo.com"
        #print(header_url+url)
        navigator.append(header_url+url)
        full_url = header_url + url
        f.write(my_url+ "," + full_url + "\n")
        t.write(full_url + ";" + title + ";" + autore + ";" + rating + ";" + prezzo + "\n")
        #i=i+1
    if not navigator:
        return old_url, my_url
    old_url = my_url
    rnd = random.randint(0,len(navigator)-1)
    my_url = navigator[rnd]
    print(my_url)
    return my_url, old_url

def readCommunities(filename):
    with open(filename) as f:
        link = tuple(f.read().splitlines())
    links = []
    for l in link:
        links.append(l)
    return links


def main(start, iterations, f, t):
    j = 0
    while j<len(start):
        my_url = start[j]
        print ("j: " + str(j))
        i=0
        print(iterations)
        while i<int(iterations):
            old_url = my_url
            my_url, old_url = scraping(my_url, old_url, i, f, t)
            i=i+1
        j=j+1


filenameCSV = enterFilename("scraped info CSV")
filenameAddInfo = enterFilename("adding information CSV")

f, t = openFiles(filenameCSV, filenameAddInfo)

start = readCommunities(sys.argv[1])

main(start, sys.argv[2], f, t)

closeFile(f, t)