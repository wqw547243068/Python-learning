#coding:utf8
#[2018-4-1]python初学者好玩案例:https://blog.csdn.net/qq_18495537/article/details/79278710
from time import sleep  
import requests

if __name__ == "__main__":
    ask = input("请主人输入话题：(随便什么词) ")
    same_max = 10#中止条件，恢复语句中最多多少次相同
    same_count_1 = 0
    same_count_2 = 0
    last_resp_1 = '-'
    last_resp_2 = '-'
    count = 0
    print('{}\t{:<40}\t{:<40}\n{}'.format('轮数', '图灵(问)', '青云客(答)', '-'*80))
    while True:
        count += 1
        #更新问题
        if last_resp_2 != '-':
            ask = last_resp_2
        sleep(1)
        #图灵机器人
        resp = requests.post("http://www.tuling123.com/openapi/api",
            data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": ask, })  
        resp = resp.json()
        #print('第{}轮\t图灵：\t{}'.format(count, resp['text']))
        if same_count_1 > same_max:
            print('图灵把天儿聊死了。。。哈哈哈')
            break
        if resp == last_resp_1:
            same_count_1 += 1
        else:
            last_resp_1 = resp
        #printf('%s\t%s', count, resp['text'])
        print('%s\t图灵： %s'%(count, resp['text']))
        #print('%s\t图灵： %s'%(count, resp['text']), end="")#python3不换行
        sleep(1)
        #青云客机器人
        resp = requests.get("http://api.qingyunke.com/api.php", 
            {'key': 'free', 'appid': 0, 'msg': resp['text']})  
        resp.encoding = 'utf8'  
        resp = resp.json()
        if same_count_2 > same_max:
            print('青云客把天儿聊死了。。。哈哈哈')
            break
        if resp['content'] == last_resp_2:
            same_count_2 += 1
        else:
            last_resp_2 = resp['content']
        #print('第{}轮\t青云客：\t{}'.format(count, resp['content']))
        #print('{}\t{:<40}\t{:<40}'.format(count, s, resp['content']))
        print('\t\t{:>40}'.format('菲菲: '+resp['content']))