from bs4 import BeautifulSoup
import urllib2
eq = urllib2.urlopen("http://earthquaketrack.com/p/india/recent")
response = eq.read()
souped = BeautifulSoup(response)
print "\n"
for topbar in souped.findAll("div", { "class" : "city-stats row panel panel-default" }):
	for data in topbar.findAll("div",{"class":"col-lg-4 col-sm-4"}):
		for lists in data.findAll("li"):
			print lists.text
	print "\n"
	for data in topbar.findAll("div",{"class":"col-lg-5 col-sm-4"}):
		for lists in data.findAll("li"):
			print lists.text.strip()
