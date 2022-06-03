"""爬虫相关配置"""

# 关键词
keyword = '手机背面'

# 最大下载数量
max_download_images = 20

# 精简一下网址，去掉网址中无意义的参数
url_init_first = 'https://image.baidu.com/search/flip?tn=baiduimage&word='

# 表头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.192 Safari/537.36'
}
