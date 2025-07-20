import json
from config import host, user, password, db_name, res
from Eval import dictdates
i=1
alllogs={}
logslist=[]
columns=["ip", "time", "another"]
row=[]

# with open("access_logs.log", "r") as file: 
#             logs = file.readlines()

# for log in logs:
#     dellog=log.split(' ')
#     # print(dellog)
#     ip = dellog[0]
#     time = dellog[3]+dellog[4]
#     detail=''
#     for h in dellog[5:22]:
#         detail+=h
#     row.append(ip)
#     row.append(time)
#     row.append(detail)
#     json_log=dict(zip(columns, row))
#     # print(json_log)
#     alllogs[i]=json_log
#     i+=1
# with open('logs1.json', 'w') as fp:
#     json.dump(alllogs, fp)

# print(alllogs)
# with open('logs1.json', 'w') as outfile:
#     json.dump(alllogs, outfile)
# print('конвертация закончена')
# detail_date.append(a[0])
# detail_date.append(a[3]+a[4])
# detail_date.append(a[5:22])
# for h in logs:
#     date.append(detail_date)
# print(date)



#287050
# a=res.json()
# dates=a[0]
# dictdates=eval(dates)
i=1
while i<287050:
    print(dictdates[f'{i}'])