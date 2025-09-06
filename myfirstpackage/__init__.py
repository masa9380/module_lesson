"""
__init__.py:このファイルを置くことで、Pythonはそのディレクトリをパッケージとして認識する
__init__.pyには初期化用コードを記述する(import時に実行される)
__init__.pyにimport文を書くことで、モジュール名をスキップして、packageの後に関数名やクラス名にアクセスできる

名前空間：そのファイルが属する空間(PAYHみたいなもの)
名前空間パッケージ：__init__.pyがないパッケージのこと
異なるパスに存在する、同名のパッケージを共通のものとしてまとめることが可能になる
例：
/AAA/BBB/myfirstpackage/
            module1.py
            module2.py

/CCC/DDD/myfirstpackage/
            module3.py
            module4.py

↑これらはパッケージのパスはことあるが名前は同じ
import myfirstpackage.module1
import myfirstpackage.module3
というようにインポートできる。便利であるが、インポートに時間がかかるというデメリットがある。
基本的には、パッケージを作成する際は、__init__.pyを作る
"""

# print("This is __init__.py")
from myfirstpackage.subdir.module2 import *
#これをすることによって、module2ないの全ての関数が、myfirstpackageの直下にインポートされる
# →呼び出す際はmyfirstpackage.func()のように
# モジュール名の記述を省略することができる



