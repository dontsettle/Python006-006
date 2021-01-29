# 翻页的处理
import requests
from lxml import etree
# pip install lxml
from time import sleep
from pathlib import *
import sys
# 控制请求的频率，引入了time模块

# 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    
    ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

    header = {'user-agent':ua}
    response = requests.get(myurl,headers=header)

    selector = etree.HTML(response.text)
    # 电影影评列表
    film_coment = selector.xpath('//div[@class="comment"]/p/span[1]/text()')

    #  影评星级列表
    film_rating = selector.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class')

    # 遍历对应关系字典
    film_info = dict(zip(film_coment, film_rating))
    # for i in film_info:     
    #     dou_book=(f'电影影评: {i} \t\t 影评星级: {film_info[i]}')
        # print(dou_book)
    # 获得python脚本的绝对路径
    p = Path(__file__)
    pyfile_path = p.resolve().parent
    # 建立新的目录html
    html_path= pyfile_path.joinpath('html')

    if not html_path.is_dir():
        Path.mkdir(html_path)
    page = html_path.joinpath('douban.html')

    # 上下文管理器
    try:
        with open(page,'w',encoding='utf-8') as f:
            for dou_key,dou_value in film_info.items():
                f.write(dou_key+'\n'+dou_value)
                f.write('\n')
    except FileNotFoundError as e:
        print(f'文件无法打开,{e}')
    except IOError as e:
        print(f'读写文件出错,{e}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 生成包含所有页面的元组
    urls = tuple(f'https://movie.douban.com/subject/30444960/comments?start={ page * 20 }&limit=20&status=P&sort=new_score'for page in range(4))
    for page in urls:
        get_url_name(page)
        sleep(5)