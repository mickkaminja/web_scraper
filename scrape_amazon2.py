from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

	# opening connection

my_url = 'https://www.amazon.com/b/ref=br_asw_smr?_encoding=UTF8&node=18637575011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=DV3HJDAQGN2A6NME99GN&pf_rd_t=36701&pf_rd_p=74c2af8b-5acb-4bf8-b252-8b1584c94b14&pf_rd_i=desktop'
	# grabbing the page

uClient = uReq(my_url) 

	# dumping in page_html as a variable

page_html = uClient.read()

	# closing uClient
	
		# uClient.close()  *****not sure this works well so will focus on this later
		
			# its not required though

	# parsing of html and putting int variable page_soup
	
page_soup = soup(page_html, "html.parser")

	# get info under div tags
	
containers = page_soup.findAll("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
	
	# find number of divs by same class name found...using len method
	
len(containers)

		# set variable containers' first array(container[]) as container
		
container = containers[0]

	# find vlue of alt attribute in img tag in div tag in selected class
	
container.h2["data-attribute"]	

	# starting script loop
test = open("testfile.txt" ,"w")
	
for tech in containers:
	brand = tech.h2["data-attribute"]
	
	test.write(brand)
	#test.close()
