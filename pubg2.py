from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from multiprocessing import Pool
import pandas as pd
import time
import re

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

#模式参数&区服参数
mode = '3'
region = '3'
mode1 = 'squad'
region1 = 'as'
index = 'https://pubgtracker.com/leaderboards/pc/Rating?mode='+ mode +  '&region='+ region

#正则表达式pattern参数
pattern_solo = re.compile('{"Region":"as","Season":"2018-01","Match":"solo","Stats":(.*?)}]}',re.S)
pattern_data = re.compile('"value":"(.*?)","rank":(.*?),"percentile":(.*?),"displayValue"',re.S)
pattern_duo = re.compile('{"Region":"as","Season":"2018-01","Match":"duo","Stats":(.*?)}]}',re.S)
pattern_squad = re.compile('{"Region":"as","Season":"2018-01","Match":"squad","Stats":(.*?)}]}',re.S)
pattern100 = re.compile('href="/profile/pc/(.*?)">', re.S)

#循环爬取参数初始化
j = 0
result_list = []

browser = webdriver.Chrome()
browser.set_window_size(1400,900)
#browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)


browser.get(index)
time.sleep(10)
html = browser.page_source

def top100_player(html):
    time.sleep(10)
    items = re.findall(pattern100, html)
    for item in items:
        yield item

#两层正则提取选手游戏数据
def parse_player(player):
    browser.get('https://pubgtracker.com/profile/pc/' + player +'/' + mode1 + '?region=' + region1)
    time.sleep(12)
    html1 = browser.page_source

    html2 = re.search(pattern_duo, html1)
    item1 = html2.group(1)
    if item1:
        item2 = re.findall(pattern_data, item1)
        for item in item2:
            yield item[0], item[1], item[2]

def main(player):
    print('正在采集',player)
    if player.find('<') == -1:
        try:
            for a,b,c in parse_player(player):

                    items = {
                        'player':player,
                        'data':a,
                        'rank':b,
                        'percent':c
                    }
                    result_list.append(items)
        except:
            pass
    else:
        pass

if __name__ == '__main__':
    players = [player for player in top100_player(html)]
    pool = Pool()
    pool.map(main,players)
    df = pd.DataFrame(result_list)
    file_name = '{0}_{1}.{2}'.format(region1,mode1, 'csv')
    df.to_csv(file_name)








