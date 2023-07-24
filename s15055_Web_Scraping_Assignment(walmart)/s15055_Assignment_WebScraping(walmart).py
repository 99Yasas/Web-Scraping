from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&affinityOverride=default"
headers = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'ACID=1cbee805-ddf5-4245-9be7-927d354c4f57; hasACID=true; assortmentStoreId=3081; hasLocData=1; vtc=WgMw1HbY5AICK_N47c5AX4; _pxhd=e06f0c9e3ba713dd6a9d1d47df3d235c62af8a18ba936d60634d9574ca8a3ebb:7fe42a5f-b755-11ed-b3b0-4c6c45767259; TBV=7; adblocked=false; _pxvid=7fe42a5f-b755-11ed-b3b0-4c6c45767259; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJzdG9yZVNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY3NzU4MTMzNjQ5MX0sInNoaXBwaW5nQWRkcmVzcyI6eyJ0aW1lc3RhbXAiOjE2Nzc1ODEzMzY0OTEsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMzA4MSIsInR5cGUiOiJERUxJVkVSWSIsInN0b3JlU2VsZWN0aW9uVHlwZSI6bnVsbH1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2Nzc1ODEzMzY0OTEsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2MjoxY2JlZTgwNS1kZGY1LTQyNDUtOWJlNy05MjdkMzU0YzRmNTcifQ%3D%3D; TB_SFOU-100=; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; bstc=SjXruiXovdjvpkBiKqwPwE; auth=MTAyOTYyMDE4xDQ8tVp6jFEuOuL7kLl7B2l5mmi9dqJd2%2BlBbyYEHCDv7pQaRuDx5MPAn5bBYDMsZ%2Bp1DgTu1MM3wsbOujfROOP2Viga%2BNDOY0iK3MBn7xZ%2F7eAOyE%2B%2FhOLoZMsd8VB6767wuZloTfhm7Wk2KcjygmNzsF5Ho8U7SJCh0TVScOlLIXV4X9gPt4WGUt%2B51E3OkrdGhZ%2Fz34NLs95DNX617ehTKFfwpRZdsJs53g5fBJwUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHTExrw2zK6wCEZyH7EGJ%2Ba1yhjxHDsVjFsP561itEfKHOoZKU7yQluv%2FDcjj%2BQUhPU9taDHou0MHzTjAj9qNZWxC3ndJPT0ofPwmTPdvmbP2SfVYSBqwoTNOUfYcSrq6SJE5WBBdZBCyKnCQAR7o6eg%3D; mobileweb=0; xptc=assortmentStoreId%2B3081; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=0Hwwl|14us3|21SVb|2OL6S|68uha|B9GaQ|CUZkH|D8jju|DgxcY|Eq7vl|F9vl4|FAugj|IM26Z|IXdy8|JTFEG|JbH07|MQZaE|O1WSp|PKf1P|SQwC-|VMEdu|XZIx3|X_0sV|aN6OE|aizjH|d7vcJ|pPfKs|pyVOq|qqCxQ|ruskL|tGzti|trekl|uC8cf|uPVFl|unyo-|xMGB0|xig4c|zPHCS; exp-ck=21SVb22OL6S1D8jju1DgxcY1Eq7vl1IM26Z3IXdy83JTFEG1PKf1P1SQwC-1VMEdu1XZIx31X_0sV1aizjH1pPfKs1xig4c1zPHCS1; xpkdw=1; xpm=1%2B1678024554%2BWgMw1HbY5AICK_N47c5AX4~%2B0; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40NzQ2LCJsb25naXR1ZGUiOi0xMjEuMzQzOCwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6W10sImludGVudCI6IlBJQ0tVUCIsInNjaGVkdWxlRW5hYmxlZCI6ZmFsc2V9LCJkZWxpdmVyeSI6eyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIzMDgxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY3ODA0NjE1ODU4NSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjFjYmVlODA1LWRkZjUtNDI0NS05YmU3LTkyN2QzNTRjNGY1NyJ9; _pxff_cfp=1; _astc=fec3f84167073c72b9f83abbb52a7588; pxcts=916c2376-bb5d-11ed-ad72-424a456a4b4a; wmlh=de421ce6fe80a85f7abee09317112ff776c80087c79588223aea1808e3ffa870; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1678024624483; xptwj=rq:516cfe0331b93e77721c:MZMxLjZutXtEWzCTvwY0M5N7Dy09rw+3y6Z/NTcLZa8yi0sLEhbVSd/K1S/QudgzxdIcXeobidNdMpDeLOOkdvzDW9kadwx+C6VRrfGsaIC7egdRhRZl1BQItKdu; akavpau_p2=1678025225~id=52348c5061b5a914e46f2534f3a62d85; bm_mi=249CCD78CF77F631D8F710588377AD83~YAAQFKbWfVA/KnaGAQAAo80PshOqfoOkc757jF20q+26khLC8AbjUvy83owKWPGWDruc0x//HK5pVA9Pixb9wrNiccq4e4Isp5eLBHvErnVXc4RCaCGeu7cDa5tE0Qa7GObw29TVrlhrk089WpjJzYf+Z9q+hzzKBL9GrSR6ZmDZSzcYTmkSYdxMfI+Brph2geJoMxLqlIEnrvA/6o/L6wF6Qe49jNUYv70sBUP5WBWkP/FqNy5QW1AgC1Yl3iwgpgnMnwlmiVbGj6tcBVB2A2o8zlLwLhriOeHO2S5NA4Jv7biaaOCIeiB773O6knYfuteTJhHBvAdZngniVw30gViC0RpAW+UKsup1M/4VeaGbpKdH8eW+BLcvHwPUVuH4gzrtULp3~1; _px3=150286b7ae3f19699549db8d22515c00c34613d9583a9b334dfc587714da059e:7vuL3UZulKj9rZEHpE7mj4HOQQzz29oOpB0Jz+1QI9ILjeOIHBnTqtGYwj8UlNllrau8DfFQwOvu1JXYOa1y9w==:1000:uTBZCUZls12ODYvxTMvFSN1deXle4JQTqcbHPIznS82U/JqL07+Zm85ZPzQJdH1/8hLzBjMGNeC0Jb9msGlVXAO/q8uNmsCejEtHOMO779SAbXqdGsBAmaICpK2y+GAaz1te1TAn7dOP9J1BoLoRLgovEn6bodjGAuvOk0JHC92a1wp/lZ6+0d6C39nSs+N5XxYoQtQhJOnBc72Dy7Ph3g==; bm_sv=0A001CE62BCFF1170446A1D9C8FED038~YAAQF6bWfT1LnrCGAQAAsgoQshNDpaThQg+1I6AZsn5yPTQWRIAopce8Wni0UT3zVObcZds8I8pyfpNkqUBziugLAh8/g+ORZiWf9TdCWipeMb2H7xII4c58RI3u954aGeSrhdBG0KESvRxYjGt2Aspsn+DoJ5oTw61lQomUHPEe5v6TSow0vG9K70VzjMc80+2fpssj73wzHtasfdUfp6Ilp89pwkOjXwE//iAB4pQ3qW9w09Lwbju/p3Avwkw8A40=~1; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1678024641000@firstcreate:1677581336454"; xptwg=1889948344:1B4F587AA1810E0:45E69CD:89B4A4F9:71485177:1EDB9417:; ak_bmsc=A9A635331676DEA0B0FFE1E40C9EA2B0~000000000000000000000000000000~YAAQF6bWfUVLnrCGAQAAWw0QshNGCqNX+3cvvGz3Z92HBJKzUDB3o69g8+Tb84y0aVKeY4/s4mXQoA+ehm2nV9Y6knGo0+KIvF1YNPyXAqu5+V1rzfai7SEJfUqDnlSzhTLWgiUlQhX9pmyCMruJABidwJ+04PIre4/mQ56o1PnArh6ItsbS/BTZRGakK3UEq6tdClbz4K0b+sTLWVbufx99uvQfNuLYc4CF2L6/Oq0tjr8P3VHjZSWkNk5kCuVA6VasCG5FwSF+OwKNc2XuHAsc8QWeHi5SSO9dFtkYjU7+n+xCzHjamnAQFBSVnCCPyK+fIbF9lrcNOFZHKT3xDh4dRSCYGRoE80n9/f0TU7RBlaCd7mwPa54irg6HYNFaQgthdfjrTz8F1pX/vTpVcfNuzww3KOGRw8cLQgQbV8y/IOdPSEBcxQUcBisKRvOze7ZYbv3qV1H1zt40WD6cz/bMzuCl0KFRHppomZOErI/CHEAv97hdVnISll3hJREtxWYUywnMpOEMJICpm++ibUkCcQHF98VjSjK0JCpnvSX5qyXO4V7ior/7Ea1OUAiGavC+rMfEKTpCmoijJg==; _pxde=cccaa3801950792bd5765e0303cc8e478d9f118852ad250262c2c45971146d01:eyJ0aW1lc3RhbXAiOjE2NzgwMjQ2NDM0MzJ9; TS012768cf=014e9abc5bfca330056d2a9ba22bf4be227f02d65c5a665dafcc28f713c8aa3235ca332a0acc6d10d424ca6a1529e7bf1a5affb704; TS01a90220=014e9abc5bfca330056d2a9ba22bf4be227f02d65c5a665dafcc28f713c8aa3235ca332a0acc6d10d424ca6a1529e7bf1a5affb704; TS2a5e0c5c027=08754faef6ab2000b8040aaea03e0067562f1feae69aa946e50370d57001e0b7780bc53bdd25fb7f081aecbd11113000d1757083783317ffb5d716de83b3879191a8960fb63482f70e993e0e939eedea83144c9a43b2aff94faecd76b10547d6; TB_SFOU-100=; TS01a90220=0137b3e9de8bc2710abaca80f02707c1439367f2367161ce4307057e892261eb841c07b924b94240d880a9ac58c7b4958105e045a5; bstc=SjXruiXovdjvpkBiKqwPwE; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1678025485000@firstcreate:1677581336454"; exp-ck=21SVb22OL6S1D8jju1DgxcY1Eq7vl1IM26Z3IXdy83JTFEG1PKf1P1SQwC-1VMEdu1XZIx31X_0sV1aizjH1pPfKs1xig4c1zPHCS1; mobileweb=0; vtc=WgMw1HbY5AICK_N47c5AX4; xpa=0Hwwl|14us3|21SVb|2OL6S|68uha|B9GaQ|CUZkH|D8jju|DgxcY|Eq7vl|F9vl4|FAugj|IM26Z|IXdy8|JTFEG|JbH07|MQZaE|O1WSp|PKf1P|SQwC-|VMEdu|XZIx3|X_0sV|aN6OE|aizjH|d7vcJ|pPfKs|pyVOq|qqCxQ|ruskL|tGzti|trekl|uC8cf|uPVFl|unyo-|xMGB0|xig4c|zPHCS; xpm=1%2B1678024554%2BWgMw1HbY5AICK_N47c5AX4~%2B0; xptc=assortmentStoreId%2B3081; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xptwg=3601004893:D70A16DE2C75C8:22666B5:F97F27C2:96AF409C:D4140AEE:; TS012768cf=0137b3e9de8bc2710abaca80f02707c1439367f2367161ce4307057e892261eb841c07b924b94240d880a9ac58c7b4958105e045a5; TS2a5e0c5c027=08946f9538ab2000fdf9198ff3960d8cf4e32fc6cf19cb71f5e4a38a03a4d6267187ab495d0d21f708ba85ee491130000a90f12bf52cbd6b56c87ec9530db73d5b72eb3c21b1c6b5a925b5a066092828644868de34c3d24712bc74542e61f29a; akavpau_p2=1678026085~id=0147100a6051d11433d88c59e1efba62',
  'device_profile_ref_id': '8vfJh6vlDqFlhyXHFEf8xkT5Dmde3AzWPPLe',
  'referer': 'https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&page=2&affinityOverride=default',
  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-989cda1a1e8b3f596fe68a16aa0fccdf-461c5486e1f96706-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&page=2&affinityOverride=default',
  'wm_qos.correlation_id': 'UCzXenmCjuU2vj37RcjqkCfApUu-wNNbk-ui',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'UCzXenmCjuU2vj37RcjqkCfApUu-wNNbk-ui',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.51.0-1f10f1-0302T0622',
  'x-o-segment': 'oaoh'
}
product_names=[]
price_list=[]

url_list = []

for i in range(1,26):
    url = 'https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&affinityOverride=default&page=' + str(i)

    if i % 2 == 0:
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        driver = webdriver.Edge(options=options)

    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=options)

# Wait for the page to load and extract the prices
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver.get(url)
    wait = WebDriverWait(driver, 100)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.w_iUH7")))
    soup = BeautifulSoup(driver.page_source, "html.parser")

    product_name=soup.findAll('span',{'class':"w_V_DM"})
    product_price=soup.findAll('div',{'data-automation-id':"product-price"})
    for names,price in zip(product_name,product_price):
        product_names.append(names.span.text.strip())
        price_list.append(price.div.text.strip())
    driver.quit()
    
    df=pd.DataFrame({'Product':product_names,'price':price_list})
    filepath=r"E:\Education\3rd Year\2nd Sem\IS 3005 - Statistics in Practice I\Python\s15055_walmart_iphones.xlsx"
    df.to_excel(filepath)
