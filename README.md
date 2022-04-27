# Investigator
## Find data for your academic life easily.


Navigating academic search engines to find investigations, magazines and papers can get tedious due to old designs and slow loading times.
Investigator allows you to make a single search in six pages at the same time and returns a xlxs file containing the title and link of each result on the first page.
The search engines chosen are Google Scholar, Research Gate, Base Search, Pubmed, Elsevier and Libgen, but more can be added if need arises.


### How can I use it?
Just check if you have bs4, lxml and openpyxl and run the program with your python interpreter.



## Patch Notes
* Bug-fixes in writing and checkIfHasLink.
* Optimization changes. ERIC was deleted due to excessive load times and led to unoptimal code.

## How can I add another search engine?
 
Just create an object of the class "website" and fill in all the fields: 
*  Name.
*  Search Link: the link of the search query. Place "~ °Ñ° ~" (as is written in the document) in the place where a search term would go.
*  Link: the "base" link of the website.
*  Tag: either the x-path or html tags like div, header, article, etc depending of the scraping type chosen.
*  Chosen Class: the class of the element you are looking for.
*  Scraping Type: two different ways of getting the results were written due to some websites not working with the original one.
  *  Basic gets the html content by the tag and the class.
  *  Selector iterates on the x-path to find all the elements required. To use it, replace the number you need to iterate on with "~°Ñ°~".
    *  Example: 
      *  .catalog > tbody:nth-child(2) > tr:nth-child(1) >.... 
      *  We need to iterate on the last element, so we change it this way: 
      *  .catalog > tbody:nth-child(2) > tr:nth-child(~ °Ñ° ~) >....

## Clarifications

* The project was made without any monetary gain in mind.
* I have no connection to any of the search engines mentioned beforehand and in the code.
* If for any reason any of the webpages involved or their representatives require it, the code will be taken down or modified.
