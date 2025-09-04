import sys
sys.path.append('/Users/masaki/Desktop/PythonLecture/function')
import docstring
import mymodule as mm

# モジュールをインポートする時はスクリプトのはじめにまとめて行う。
# 順番：標準ライブラリ(sys)→サードパーティのライブラリ(numpy,pandas)→自分たちの作ったライブラリ→ローカルのファイル

# パッケージの中にモジュールがある場合は、
# import package.subpackage.module.funcのような形になる。
# from mymodule import myfunc, myvariable
# from mymodule import * #mymodule内の全ての関数や変数をすべてまとめてインポートできる。
# ただし、何がインポートされているかわからなくなるため、非推奨

# mymodule.myfunc()
mm.myfunc()
mm._anotherfunc()
print(mm.myvariable)
# print(mymodule.myvariable)

print(sys.path)
print(docstring.multiply(3,4))