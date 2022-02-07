from bs4 import BeautifulSoup
from bs4.element import AttributeValueWithCharsetSubstitution
import requests
import lxml
import openpyxl

def scrapingWebsite(webpage, tag, htmlClass):
  r = requests.get(webpage)
  soup = BeautifulSoup(r.content, "lxml")
  Headlines = []
  Links = []

  for x in soup.find_all(f"{tag}", class_= f"{htmlClass}"):
     Headlines.append((x.get_text()).strip())

  #for y in soup.find_all(f"{tag}", class_= f"{htmlClass}", href=True):
   #  Links.append(x[href])
  
  return(Headlines)
      
def scrapingLibgen(link):
   r = requests.get(link)
   soup = BeautifulSoup(r.content, "lxml")
   Headlines = []
   Links = []

   #This page was not friendly to scraping, due to not having classes and divs, so I had to iterate on the CCSselector
   for x in range(11):
      for element in soup.select(f"#tablelibgen > tbody:nth-child(2) > tr:nth-child({x}) > td:nth-child(1) > a"):
         if not ((element.get_text()).startswith("DOI")): Headlines.append(element.get_text())

   #for y in soup.find_all(f"{tag}", class_= f"{htmlClass}", href=True): Links.append(x[href])


def start(argument):
  # Page = [link, tag, class, name, scraping function]
   pubmed = [f"https://pubmed.ncbi.nlm.nih.gov/?term={argument}", "a", "docsum-title", "PubMed", "basic"]
   scholar = [f"https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q={argument}&btnG=", "h3", "gs_rt", "Scholar", "basic"]
   #sciencedir = [f"https://www.sciencedirect.com/search?qs={argument}", "a", "result-list-title-link u-font-serif text-s", "Sciencedirect", "basic"]
   researchgate = [f"https://www.researchgate.net/search/publication?q={argument}", "div",
   "nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-publication-item__title", "ResearchGate", "basic"]
   elsevier = [f"https://www.elsevier.com/search-results?query={argument}", "h2", "search-result-title", "Elsevier", "basic"]
   libgen = [f"https://libgen.li/index.php?req=[{argument}columns%5B%5D=t&columns%5B%5D=a&columns%5B%5D=s&columns%5B%5D=y&columns%5B%5D=p&columns%5B%5D=i&objects%5B%5D=f&objects%5B%5D=e&objects%5B%5D=s&objects%5B%5D=a&objects%5B%5D=p&objects%5B%5D=w&topics%5B%5D=l&topics%5B%5D=a&topics%5B%5D=m&topics%5B%5D=s&res=25",
  "", "", "LibGen", "scrapingLibgen"]
   listOfWebpages = [pubmed, scholar, researchgate, elsevier, libgen]
  
   #creating the xlsx file
   my_wb = openpyxl.Workbook()
   my_sheet = my_wb.active

   #putting the number of the search results
   for n in range(1, 21):
      if (n % 2 == 0):
         my_sheet.cell(row=n, column=1).value = (n/2)   

   #Defining the column, the first one is used by names
   columnNumber = 2

   for webpage in listOfWebpages:
      #Naming the column
      my_sheet.cell(row=1, column=columnNumber).value = webpage[3]

      #getting the headlines as returns
      #this next thing is to know what kind of scraping we're using, the most basic one or a specific one.
      rowNumber = 2
      if (webpage[4] == "basic"):
         headlines = scrapingWebsite(webpage[0], webpage[1], webpage[2])
      elif (webpage[4] == "libgen"):
         headlines = scrapingLibgen(libgen[0])

      #writing every headline
      for headline in headlines:
         my_sheet.cell(row=rowNumber, column=columnNumber).value = headline
         rowNumber += 2

      columnNumber += 1

   my_wb.save("INVESTIGATOR.xlsx")

start("engineer")