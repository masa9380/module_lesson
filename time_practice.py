from functools import lru_cache # 計算したキャッシュを保持しておくデコレータ
import time

# .time(): 1970/1/1から現在に至るまでの秒数が表示される→Unix時間という
print(time.time())
print(time.time()/(60*60*24*365))

@lru_cache
def fib(n):
    print(f'fibonacci with {n} is running...')
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# .time()を利用することで、処理にかかった時間を表示することができる
before = time.time()
# 処理の内容を記述
# print(fib(30))
after = time.time()
print(f'recursive fibonacci took {after-before:.2f} sec.')


# .ctime(): 今のローカル時間を文字列で返す
print(time.ctime())
# .localtime(): 現在の時刻を構造化データで返す
localtime = time.localtime()
print(localtime)
print(f'今の時刻は{localtime.tm_year}年{localtime.tm_mon}月{localtime.tm_mday}日'
      f'{localtime.tm_hour}時{localtime.tm_min}分{localtime.tm_sec}秒です')


# .sleep(sec): sec秒だけプログラムが待機する
sec = 5
print(f'{sec}秒待ってください')
# time.sleep(sec)
print(f'{sec}秒経ちました')




# 課題：関数の実行時間（sec）を図るtimerデコレータを作る

# decorator用の関数
# 関数の処理にかかった時間を測定するための関数
def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__}の処理に{after-before:.3f}秒かかりました")
    return inner

@timer
def lazy_func(sec):
    print("I'm working so hard...")
    time.sleep(sec)
    print("I'm finally done!")

lazy_func(3)
