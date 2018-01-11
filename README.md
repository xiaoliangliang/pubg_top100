# 用selenium爬取绝地求生各区服top100玩家数据

## 环境准备
1. python3
2. selenium库
3. pandas库
4. 下载最新版的Chrome浏览器
5. re正则表达式库

# 参数修改

以下是欧服&solo模式&2018第一赛季的参数： 
#模式参数&区服参数

  mode = '1'
  region = '2'
  mode1 = 'solo'
  region1 = 'eu'
  
  #正则表达式pattern参数
  
  pattern_solo = re.compile('{"Region":"eu","Season":"2018-01","Match":"solo","Stats":(.*?)}]}',re.S)>


### 这里可以选择不同的模式&区服，如果要改成亚服&双排模式的top100数据：

#模式参数&区服参数

mode = '2'
region = '3'
mode1 = 'duo'
region1 = 'as'

#正则表达式pattern参数

pattern_solo = re.compile('{"Region":"as","Season":"2018-01","Match":"duo","Stats":(.*?)}]}',re.S)


## 运行爬虫程序
1. cmd进入命令行
2. cd到该文件夹目录下
3. python pubg1.py(该版本为最稳定版本，但是速度一般。。)

## 代码优化思路（pubg2.py是测试版本，不稳定）
1. 用PhantomJS代替Chrome浏览器
2. 加入多线程爬取

## 爬取之后用pandas进行数据预处理的结果：
![alt text](123.png "title")
