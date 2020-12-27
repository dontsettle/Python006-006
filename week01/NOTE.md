学习笔记
git init  #初始化
git config --global user.name "dontsettle"   #创建名字
git config --global user.email "email地址"    #创建email地址
git config --global --list #查看创建内容
pwd                 #查看文件路径
git status         #查看工作区内容
git add            #提交文件到暂存区
git commit -m  "....."     #提交文件到本地仓库并写注释
git log             #查看日志
clear               #清空屏幕
#时间笔记
import time
from datetime import datetime,timedelta

a = time.time()
print('时间戳')
print(a)
print(time.localtime())
print('时间的格式化')
aa = time.strftime('%Y-%m-%d %X',time.localtime())
print(aa)
print('字符转换为时间对象')
print(time.strptime('2020-12-22 16:43:01','%Y-%m-%d %X'))

print('*'*11,'datatime 时间偏移的处理','*'*11)
print('now()')
print(datetime.now())
print('today()')
print(datetime.today())
print('时间偏移')
print("day+1")
print(datetime.today() - timedelta(days=1))
print(datetime.today() + timedelta(days=-1))

#路径笔记
os.path.abspath('test.log') #获得路径名
os.path.basename(path)      #获得文件名
os.path.exists('xxx.xxx')   #判断文件存在
os.path.isfile('XXX.XXX')   
os.path.isdir('xxx.xxx')
os.path.join('a','b')      #路径组合
#虚拟环境
touch a.py                # 建文件
rm a.py                   #删除 a.py 文件
python -m venv venv1      #建虚拟环境
source venv1/scripts/activate  #激活虚拟环境
which python                    #看路径
python -V                   #看版本
deactivate                  #退出虚拟环境
pip freeze                  #查看在虚拟环境下的第三方库
pip freeze>requirements.txt  #把第三方库打包到文件里
cat requirements.txt          #试运行第三方库包
