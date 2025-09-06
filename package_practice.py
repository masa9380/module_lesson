# # 様々なパターンでパッケージをインポートし、モジュールを使ってみる
#
# # パターン1：moduleをそれぞれインポートする
# import myfirstpackage.module1
# import myfirstpackage.subdir.module2
#
# myfirstpackage.module1.myfunc()
# myfirstpackage.subdir.module2.myfunc()
#
# # パターン2：from を使ってモジュールをまとめてインポートする
# from myfirstpackage import module1
# from myfirstpackage.subdir import module2
#
# module1.myfunc()
# module2.myfunc()
#
# # パターン3：fromを使って、モジュールないの関数をインポートする
# # 注意：同じ関数名のものは、最後に呼ばれたものしか適用されない。
# # 今回の場合はmodule2のもののみ適用される
# from myfirstpackage.subdir.module2 import myfunc
# import myfirstpackage



# # __all__を用いてインポート対象の関数を限定してインポート
# from myfirstpackage.subdir import *
# myfunc() # これは実行できる。(__all__で指定指定しているから)
# myfunc2() # これは実行できない。(__all__で指定指定していないから)
#


# relative importの練習
import myfirstpackage.subdir.module2
myfirstpackage.subdir.module2.myfunc2()
