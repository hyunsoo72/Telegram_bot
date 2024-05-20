import telepot
from pprint import pprint
import time
from telepot.loop import MessageLoop
import pandas as pd



def get_bot(api_key):
   bot = telepot.Bot(api_key)
   info = bot.getMe()
   pprint(info)

   return bot


def get_update(bot, offset=None):
   '''
   offset : last update_id +1 -> 최근 받아온 업데이트 아이디 이후 것으로 설정
   '''
   resp = bot.getUpdates(offset)

   return resp


def get_offset(updates):
   last_update_id = updates[-1]['update_id']
   offset = last_update_id + 1

   return offset


def get_datetime(timestamp):
   from datetime import datetime
   from pytz import timezone

   KST = timezone('Asia/Seoul')
   date = datetime.fromtimestamp(timestamp).astimezone(KST).strftime('%Y-%m-%d')
   date_time = datetime.fromtimestamp(timestamp).astimezone(KST).strftime('%Y-%m-%d %H:%M:%S')

   return date, date_time


def get_username(upt):
    temp = ''
    lst = ['username','first_name','last_name']
    name_lst = [i for i in lst if i in upt['message']['from']]
    if name_lst[0] == lst[0]:
        return upt['message']['from'][name_lst[0]]
    else:
        for i in name_lst:
            temp += upt['message']['from'][i]
        return temp


def get_df(updates):
    title, author, author_name, datetime, message, basis_dt = [], [], [], [], [], []
    for upt in updates:
        if 'text' in upt['message']:
            date, date_time = get_datetime(upt['message']['date'])
            user_name = get_username(upt)
            title.append(upt['message']['chat']['title'])
            author.append(upt['message']['chat']['id'])
            author_name.append(user_name)
            datetime.append(date_time)
            message.append(upt['message']['text'])
            basis_dt.append(date)

    return pd.DataFrame(
        {'title': title, 'author': author, 'author_name': author_name, 'datetime': datetime, 'message': message,
         'basis_dt': basis_dt})


def main(api_key, offset, destination_table, project_id, cycle_sec, limit_cnt):
    bot = get_bot(api_key)
    cnt = 0
    while True:
        updates = get_update(bot, offset)
        if len(updates) > 0:
            offset = get_offset(updates)
            df = get_df(updates)
            table_schema = [{'name': 'title', 'type': 'STRING'},
                            {'name': 'author', 'type': 'STRING'},
                            {'name': 'author_name', 'type': 'STRING'},
                            {'name': 'datetime', 'type': 'DATETIME'},
                            {'name': 'message', 'type': 'STRING'},
                            {'name': 'basis_dt', 'type': 'DATE'},
                            ]
            if len(df) > 0:
                df.to_gbq(destination_table=destination_table, project_id=project_id, if_exists='append',
                          table_schema=table_schema)
                print(f'SUCCESS : telegram data load, rows:{len(df)}')

        cnt += 1
        if cnt > limit_cnt:
            break

        time.sleep(cycle_sec)

    return 'SUCCESS'


if __name__ == '__main__':
    API_KEY = <telegrambot API_KEY 6857912701:AAFC9uuDSmKPJ_IedwYCXkPYGVChu1gTMQw>
    offset = None
    destination_table = <data 적재 테이블>
    project_id= <data 적재 프로젝트>
    sleep_sec = <적재 주기>
    limit_cnt = <제한 적재 횟수>
    main(API_KEY, offset, destination_table, project_id, cycle_sec, limit_cnt)