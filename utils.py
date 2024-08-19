from bs4 import BeautifulSoup

def Get_stock_text(html :str)-> str:
    soup = BeautifulSoup(html, 'html.parser')
    a=soup.getText()
    result = a.replace("\t","")
    result=result.replace(" ","")
    result=result.replace("\n","")
    return result[1:]