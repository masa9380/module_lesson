import sys

import numpy as np
# ターミナルにて、pip installコマンドを使うことで、
# モジュールをインストールする。


print(np.__file__)  #numpyがどこに格納されているかを確認
print(sys.path) # numpyへのpathが通っているかを確認

#よくある問題点。
# pip installした時に、sys.pathにモジュールが入っていない
# pip installのコマンドが自分の環境にあっていない場合