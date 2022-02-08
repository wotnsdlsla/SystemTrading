from api.Kiwoom import *
from strategy.RSIStrategy import *
import sys

app = QApplication(sys.argv)
kiwoom = Kiwoom()

rsi_strategy = RSIStrategy()
rsi_strategy.start()

#API 호출 부분
#Kiwoom.get_account_number(self)
# kospi_code_list = kiwoom.get_code_list_by_market("0")
# print(kospi_code_list)
# for code in kospi_code_list:
#     code_name = kiwoom.get_master_code_name(code)
#     print(code, code_name)
#
# kosdaq_code_list = kiwoom.get_code_list_by_market("10")
# print(kosdaq_code_list)
# for code in kosdaq_code_list:
#     code_name = kiwoom.get_master_code_name(code)
#     print(code, code_name)

# 종목 얻어오기
# df = kiwoom.get_price_data("005930")
# print(df)

# 내 계좌 금액 얻어오기
# deposit = kiwoom.get_deposit()

# 주문 하기
# order_result = kiwoom.send_order('send_buy_order', '1001', 1, '007700', 1, 28000, '00')
# print(order_result)

#주문정보 얻어오기
# orders = kiwoom.get_order()
# print(orders)

#잔고 얻어오기
# position = kiwoom.get_balance()
# print(position)

#실시간 종목 얻어오기
# fids = get_fid("체결시간")
# codes = '005930;007700;000660'
# kiwoom.set_real_reg("1000", codes, fids, "0")

#유니버스 저장 조회
# rsi_strategy = RSIStrategy()
# rsi_strategy.start()

#나가기
app.exec_()