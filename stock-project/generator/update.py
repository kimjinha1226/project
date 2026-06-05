import requests
import json
import os
from datetime import datetime

url = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

service_key = "b716345525eb5dfd73ffcfd4781de2ece4093d96a8f868f2ef3752b6fddbe0da"

all_stocks = []
latest_stocks = {}

for page in range(1, 51):
    params = {
        "serviceKey": service_key,
        "numOfRows": "100",
        "pageNo": str(page),
        "resultType": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    body = data["response"]["body"]
    items = body["items"]["item"]

    if isinstance(items, dict):
        items = [items]

    for stock in items:
        stock_data = {
            "date": stock.get("basDt"),
            "name": stock.get("itmsNm"),
            "code": stock.get("srtnCd"),
            "price": stock.get("clpr"),
            "change": stock.get("vs"),
            "rate": stock.get("fltRt"),
            "market": stock.get("mrktCtg")
        }

        all_stocks.append(stock_data)

        name = stock_data["name"]
        code = stock_data["code"]
        date = stock_data["date"]

        key = f"{name}_{code}"

        if key not in latest_stocks:
            latest_stocks[key] = stock_data
        else:
            old_date = latest_stocks[key]["date"]
            if date and old_date and date > old_date:
                latest_stocks[key] = stock_data

    print(f"{page}페이지 수집 완료 / 누적 {len(all_stocks)}개")

    if len(items) < 100:
        break

# 최신 날짜 기준 데이터만 저장
stock_list = list(latest_stocks.values())

with open("/app/html/stock.json", "w", encoding="utf-8") as f:
    json.dump(stock_list, f, ensure_ascii=False, indent=4)

history_path = "/app/html/history.json"

if os.path.exists(history_path):
    with open(history_path, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = {}

now = datetime.now().strftime("%H:%M:%S")

for stock in stock_list:
    name = stock["name"]
    price = stock["price"]

    if name and price:
        if name not in history:
            history[name] = []

        history[name].append({
            "time": now,
            "price": price
        })

        history[name] = history[name][-20:]

with open(history_path, "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=4)

print("stock.json 생성 완료")
print("history.json 생성 완료")