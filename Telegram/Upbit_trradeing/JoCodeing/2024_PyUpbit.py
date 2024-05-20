# UpBit API Key
# Access key : QTB3gwalV5qXF9TRxuznZ6mS51qR9abqmAyUmBVO
# Secret key : lVfLgxm6U4xsT3D8oP74PemP77SorU2s67rtQ76o

import requests
import jwt
import uuid
from urllib.parse import urlencode

# 발급받은 Access Key와 Secret Key를 입력합니다.
access_key = "QTB3gwalV5qXF9TRxuznZ6mS51qR9abqmAyUmBVO"
secret_key = "lVfLgxm6U4xsT3D8oP74PemP77SorU2s67rtQ76o"
server_url = "https://api.upbit.com"

def get_market_list():
    url = f"{server_url}/v1/market/all"
    response = requests.get(url)
    return response.json()

def get_balance(coin):
    query = {'currency': coin}
    query_string = urlencode(query).encode()

    m = jwt.encode({
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query': query_string,
    }, secret_key).decode('utf-8')

    headers = {
        'Authorization': f'Bearer {m}',
    }

    res = requests.get(f"{server_url}/v1/accounts", headers=headers)
    return res.json()

def place_order(market, side, volume, price, ord_type):
    query = {
        'market': market,
        'side': side,
        'volume': volume,
        'price': price,
        'ord_type': ord_type,
    }
    query_string = urlencode(query).encode()

    m = jwt.encode({
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query': query_string,
    }, secret_key).decode('utf-8')

    headers = {
        'Authorization': f'Bearer {m}',
    }

    res = requests.post(f"{server_url}/v1/orders", params=query, headers=headers)
    return res.json()

# 예제 사용
# 시장 정보 조회
markets = get_market_list()
print(markets)

# 잔고 조회
balance = get_balance('BTC')
print(balance)

# 주문하기 (시장가 매수 예제)
#order = place_order('KRW-BTC', 'bid', None, '10000', 'price')  # KRW 10,000 어치 BTC 매수
#print(order)

# 주문하기 (지정가 매도 예제)
#order = place_order('KRW-BTC', 'ask', '0.001', '60000000', 'limit')  # 0.001 BTC를 60,000,000 KRW에 매도
#print(order)
