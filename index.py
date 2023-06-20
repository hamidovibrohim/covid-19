#web parsing (saytdan ma'lmotlarni qirqib olish)
#bs4
#0-ish

# DOLLAR_UZS = "https://www.google.com/search?q=usd+uzs+&sxsrf=APwXEdeWyLgzk4g2-Pm65IIoA9H9BbT3zg%3A1686828546166&ei=AvaKZN3gCYOgwPAPluiG0AI&ved=0ahUKEwjd6amClsX_AhUDEBAIHRa0ASoQ4dUDCA8&uact=5&oq=usd+uzs+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCMQigUQJzIECCMQJzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQgAQQywEyBQgAEIAEMgUIABCABDIFCAAQgAQ6DQguEMcBENEDEIoFECc6CAgAEIAEELEDOg4ILhDHARCxAxDRAxCABDoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgcIABCKBRBDOgwIIxCKBRAnEEYQggJKBAhBGABQAFilDmDnGGgAcAF4AoABtAWIAaYXkgELMC4yLjEuMi4xLjKYAQCgAQHAAQE&sclient=gws-wiz-serp"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# full_page = requests.get(DOLLAR_UZS, headers=headers)


# soup = BeautifulSoup(full_page.content, 'html.parser')

# natija = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': "2"})
# print(natija[0].text)


#1-ish
# import requests
# try:
# 	url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
# 	f = str(input(" yyyy-mm-dd shu korinishda \n Sanani kiriting :"))

# 	querystring = {"date":f"{f}"}

# 	headers = {
# 		"X-RapidAPI-Key": "6803a12da6mshab34cc086194f6bp1be22djsn93edeaa16426",
# 		"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
# 	}

# 	response = requests.get(url, headers=headers, params=querystring)
# 	h = response.json()['data']

# 	if not h == []:
# 		a = response.json()['data']['confirmed']
# 		b = response.json()['data']['deaths']
# 		c = response.json()['data']['recovered']
# 		print(f"kasallanganlar soni {a}ta, tuzlaganlar soni {c}ta, vafot etganlar {b} ta")
# 	else:
# 		print("bunday sanada karanavirus bolmagan")
# except KeyError:
#     print("sanani yyyy-mm-dd korinishdayozing masalan 2021-01-01:")

#2-ish

# import requests
# from bs4 import BeautifulSoup

# DOLLAR_UZS = "https://gov.uz/oz/pages/population"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# full_page = requests.get(DOLLAR_UZS, headers=headers)


# soup = BeautifulSoup(full_page.content, 'html.parser')


# natija = soup.findAll('div', {'class': 'text_justify', 'id': "speechArea"})

# print(natija[0].text)

