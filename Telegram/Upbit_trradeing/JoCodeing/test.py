import pyupbit

access = 'QTB3gwalV5qXF9TRxuznZ6mS51qR9abqmAyUmBVO'          # 본인 값으로 변경
secret = 'lVfLgxm6U4xsT3D8oP74PemP77SorU2s67rtQ76o'          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회