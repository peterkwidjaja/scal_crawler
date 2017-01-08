from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv

#HOME_URL = "http://www.scal.com.sg/directory/scal"
HOME_URL = "http://www.scal.com.sg/directory/slot"
ajaxPageString = "?ajax=yw0&ViewUser_page="

output = []

for i in range(1,41):
  success = False
  while not success:
    try:
      html = urlopen(HOME_URL+ajaxPageString+str(i))
      homeSoup = BeautifulSoup(html.read(), "html.parser")
      companyList = homeSoup.findAll("div",{"class":"lst-alpha"})
      print("page "+str(i))

      for company in companyList:
        name = company.find("div", {"class":"company"}).getText()
        telephone = company.find("p", {"class":"tel"}).getText()
        email = company.find("p", {"class":"email"}).find("a").getText()
        addressPart = company.find("div", {"style":"color: #1A1A1A;padding-bottom: 5px;"})
        address = addressPart.find("span").getText()
        unitNo = addressPart.find("p").getText()
        #print(str(address)+" "+str(unitNo))
        #print(str(name)+" "+str(email))
        #print(str(telephone)[6:])
        combineStr = [str(name),str(email),str(telephone)[6:],str(address),str(unitNo)]
        output.append(combineStr)
        success = True
    except ConnectionResetError as e:
      print("Error! Retrying.."+str(i))


# write out to csv file
with open("slot2.csv", "w") as f:
  writer = csv.writer(f)
  writer.writerow(["Company Name","Email","Telephone","Address","Unit"])
  writer.writerows(output)

# data = []

# for table in tables:
#   curr_table = []
#   for item in table.findAll("tr"):
#     row = []
#     for cell in item.findAll("td"):
#       cell_text = "-".join(cell.findAll(text=True))
#       row.append(cell_text)
#     curr_table.append(row)
#   data.append(curr_table)

# for i in range(len(data)):
#   curr_data = data[i]
#   with open("calories_data_" + str(i) + ".csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(curr_data)href="/directory/scal?ajax=yw0&ViewUser_page=2"
