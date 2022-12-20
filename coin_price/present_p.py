import os
import sys
from typing import List, Final
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))


import time
from kafka import KafkaProducer
from kafka_distribute.producer import producer_optional

from api_injection.coin_apis import BithumAPIBitcoin, UpbitAPIBitcoin
from api_injection.schema import CoinPresentSchema, concatnate_dictionary


COIN_PRECENT_PRICE: Final[str] = "coin_price"
start_time = time.time()

bootstrap_server: List[str] = ["kafka1:19091", "kafka2:29092", "kafka3:39093"]
producer = KafkaProducer(bootstrap_servers=bootstrap_server, security_protocol="PLAINTEXT")


# 현재가 객체 생성 
upbit = UpbitAPIBitcoin()
bit = BithumAPIBitcoin()


# 로그 생성
present_upbit: dict[str, int] = CoinPresentSchema(name=upbit[0]["market"], 
                                                  api=upbit[0],
                                                  args=("timestamp", "opening_price", "trade_price", "high_price", "low_price",
                                                    "prev_closing_price", "acc_trade_volume_24h", "acc_trade_price_24h")).kwargs

present_bithum: dict[str, int] = CoinPresentSchema(name=bit.__namesplit__(5), 
                                                   api=bit["data"], 
                                                    args=("date", "opening_price", "closing_price", "max_price", "min_price",
                                                     "prev_closing_price", "units_traded_24H", "acc_trade_value_24H")).kwargs


# # 스키마 생성
schema = concatnate_dictionary(upbit=present_upbit, bithum=present_bithum)
producer_optional(producer=producer, data=schema, topic=COIN_PRECENT_PRICE)

   

