# カレントディレクトリから相対インポート
from .module3 import myfunc3
# ペアレントディレクトリから相対インポート
# from ..subdir import module3
from .. import module1

def myfunc():
    print('This is mufunc from module2!')


def myfunc2():
    print('This is myfunc2 from module2!')
    myfunc3() # カレントディレクトリからインポートした場合
    # module3.myfunc3() # ペアレントディレクトリからインポートした場合