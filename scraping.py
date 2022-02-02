from bs4 import BeautifulSoup
from bs4.element import AttributeValueWithCharsetSubstitution
import requests
import lxml
import openpyxl

def scrapingWebsite(argument, tag, class):
  r = requests.get(argument)
  soup = BeautifulSoup(r.content, "lxml")

  #First of all: we get all the headlines
  for x in soup.find_all(f"tag", class_= f"{class}"):
     Headlines = f"{Headlines} ~ {x.get_text()}"
     
  print(headlines, )


def start(argument):
  # Page = [link, tag, class]
  
  pubmed = [f"https://pubmed.ncbi.nlm.nih.gov/?term={argument}", "a", "docsum-title"]
  scholar = [f"https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q={argument}&btnG=", "h3", "gs_rt"]
  libgen = [f"https://libgen.li/index.php?req={argument}&columns%5B%5D=t&columns%5B%5D=a&columns%5B%5D=s&columns%5B%5D=y&columns%5B%5D=p&columns%5B%5D=i&objects%5B%5D=f&objects%5B%5D=e&objects%5B%5D=s&objects%5B%5D=a&objects%5B%5D=p&objects%5B%5D=w&topics%5B%5D=l&topics%5B%5D=c&topics%5B%5D=f&topics%5B%5D=a&topics%5B%5D=m&topics%5B%5D=r&topics%5B%5D=s&res=25",
  "", ""]
  sciencedir = [f"https://www.sciencedirect.com/search?qs={argument}", "a", "result-list-title-link"]
  researchgate = [f"https://www.researchgate.net/search/publication?q={argument}", "div"
  "nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-publication-item__title"]
  elsevier = [f"https://www.elsevier.com/search-results?query={argument}", "header", "search-result-header"]
  
  listOfWebpages = [pubmed, scholar, sciencedir, researchgate, elsevier]
  
  for webpage in listOfWebpages:
    scrapingWebsite(webpage[0], webpage[1], webpage[2])

  
start()
