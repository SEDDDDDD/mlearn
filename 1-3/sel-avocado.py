from bs4 import BeautifulSoup

fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

# css 선택자로 추출
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select_one("#ve-list > li:nth-child(4)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li.black")[1].string)





# find 메서드로 추출
# recursive : True(자식태그), False(자손 태그)
# find(요소명, 속성, recursive=True, string="찾을 문자열")
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)




# find 메서드를 연속적으로 사용
print(soup.find(id="ve-list").find("li", cond).string)