from urllib import parse, request
import random
import json
import time
import datetime
import os
file_name = r'car-' + datetime.datetime.now().strftime('%Y-%m-%d') + '.txt'
# if int(time.strftime("%w")) != 5 or os.path.exists(file_name):
    # exit()
car_list = [
    ['zhengzhou', '豫AXXXXX', 'chejiahao', 'fadongjihao']
]
result_list = []
for x in car_list:
    print(x[1], 'Querying...')
    # if x[0] == 'zhengzhou':
    #     x[3] = ''
    params = parse.urlencode([('city', x[0]), ('hphm', x[1]), ('body', x[2]), ('engine', x[3]), ('hpzl', '02'), ('_', random.random())])
    req = request.urlopen('https://sp0.baidu.com/5LMDcjW6BwF3otqbppnN2DJv/traffic.pae.baidu.com/data/query?%s' % params)
    result = json.loads(req.read().decode())
    # print(x[1], ':', result)
    # if result['data']['count'] > 0:
    #     result_list.append(result)
    if result['status'] != 0:
        result['hphm'] = x[1]
    # print(x[1], ':', result)
    result_list.append(result)
    # time.sleep(10)
    # print(result_list)
    print('Done.')
file = open(file_name, 'w+')
file.write('车牌号\t日期\t扣分\t罚款\t地址\t违章内容')
file.write('\r\n')
for x in result_list:
    if x['status'] == 0:
        # print('------', x)
        if x['data']['count'] > 0:
            for y in x['data']['lists']:
                file.write(x['data']['hphm'] + '\t' + y['time'] + '\t' + str(y['point']) + '\t' + str(y['fine']) + '\t' + y['address'] + '\t' + y['violation_type'])
                file.write('\n')
    else:
        # print('------', x)
        file.write(x['hphm'] + '\t' + str(x['status']) + '\t' + x['msg'])
        file.write('\n')
# file.writelines(str(result_list))
file.close()
os.system('pause')
