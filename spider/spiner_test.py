import urllib.request
import urllib
from bs4 import BeautifulSoup
from collections import deque

queue = deque()  # 待爬取的队列
visited = set()  # 已爬取的set

host = 'http://weaponzhi.online'  # 入口页面, 可以换成别的
queue.append(host)

count = 0  # 计数器

while queue:

    url = queue.popleft()  # 队首元素出队
    visited.add(url)  # 标记为已访问

    print('已经抓取: ' + str(count) + '   正在抓取 <---  ' + url)
    count += 1
    try:
        url_response = urllib.request.urlopen(url)
        # 过滤.jpg这种非跳转URL的情况
        if 'html' not in url_response.getheader('Content-Type'):
            continue
        data = url_response.read().decode('utf-8')
    except:
        continue

    soup = BeautifulSoup(data, 'lxml')
    node = soup.find_all('a')  # 查找a标签节点

    for x in node:
        try:
            new_url = x['href']
            if new_url.startswith('/'):
                new_url = host + new_url
            if new_url not in queue and new_url not in visited:
                if 'http' in new_url and 'weaponzhi' in new_url:
                    queue.append(new_url)
                    print('加入队列 ---> ' + new_url)
        except:
            continue
