import suds
import sys
from lxml import etree 
import time 

def xml_pretty_print(doc):
    return etree.tostring(doc, pretty_print = True)
 
url = "http://www.webservicex.net/stockquote.asmx?wsdl"
a= {}
# get ticker symbol as command line arg or use default
#ticker_symbol = len(sys.argv) > 1 and sys.argv[1] or 'GOOG'
def main():
	

	lines = [line.strip() for line in open('DowJones.txt')]
	print lines
	
	for i in range(len(lines)):
		ticker_symbol = lines[i]
		print ticker_symbol
	
		a.setdefault(ticker_symbol , [])

		print 'opening WSDL: %s...' % url,
		client = suds.client.Client(url)
		print 'Ok'
 
		print 'Sending request...',
		xml_response = client.service.GetQuote(ticker_symbol)
		print 'Ok'
		parser = etree.XMLParser(recover=True)
		root = etree.fromstring(xml_response,parser=parser)
		a[ticker_symbol].append(root[0][1].text)
		print a

	time.sleep(60)
		
while True : 
	main()