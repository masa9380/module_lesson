import re
# Regular Expression:正規表現　通称RegEx
# ある文字列が、正しい内容をとなっているかを判定する。
# 正規表現のパターンは色々ある。今回のレクチャーでは磯のうちのいくつかを学ぶ。
# 覚える必要はないが、自分で調べられるように。

# メールアドレスの記述が正しい表現になっているかを確認する
email = "mymail@gmail.com"
print('@' in email) # @があるのか等をいちいち確認していくのは面倒

matched = re.search('@\w+\.', email)
if matched:
    print(matched)
    print('Matched!')
else:
    print('Not found!')

# metacharacter
# 「[]」のパターン []の中にある文字が、文字列の中に含まれているかを判定する
print(re.search('[abc]', 'a')) # a,b,cの文字が、文字列の中に含まれているかを判定する
print(re.search('[abc]', 'd'))
print(re.search('[a-c]', 'apple')) # a-cというようにハイフンで表示することもできる。
print(re.search('[0-9]', '3')) # 数字もいける


# 「^」のパターン　最初の文字がどうかを判定する
print(re.search('^[abc]', 'apple')) # 最初にaがあるためマッチする
print(re.search('^[abc]', 'orange')) # 最初はa,b,cではないためマッチしない


# 「{n}」のパターン　n回リピートを表す
print(re.search('^[0-9]{4}', '2025/9/5')) # 最初の4文字が数字を含んでいるかを判定する
print(re.search('^[0-9]{4}', '309にいく')) # 4文字目に数字を含んでいないからマッチしない

# 「{n,m}」のパターン　最低n回、最高m回リピート
print(re.search('^[0-9]{4}', '2025/9/5')) # n回からm回リピートされていればOKと判定

# 「$」のパターン　最後の1文字を判定する
print(re.search('[0-9]{2}$', '2025/09/05')) # 最後の2文字が数字のためマッチ
print(re.search('[0-9]{2}$', '2025/9/5')) # 最後からh2文字目が数字でないためマッチしない

#「*」のパターン　左のパターンを0回以上繰り返す
print(re.search('a*b', 'ab')) # aは0回以上繰り返されてbとなっっているためマッチ
print(re.search('a*b', 'b')) # aは0回以上繰り返されてbとなっっているためマッチ
print(re.search('a*b', 'a')) # aは0回以上繰り返されているが、bがないためマッチしない

# 「+」のパターン　左のパターンを1回以上繰り返す
print(re.search('a+b', 'ab')) # aは1回以上繰り返されてbとなっっているためマッチ
print(re.search('a+b', 'b')) # aは1回以上繰り返されておらずbとなっっているためマッチ
print(re.search('a+b', 'a')) # aは1回以上繰り返されているが、bがないためマッチしない

# 「?」のパターン　左のパターンを0回か1回繰り返す
print(re.search('ab?c', 'abc')) # bが1回であり、a,cもきちんと存在するためマッチ
print(re.search('ab?c', 'bc')) # bが1回であるが、aが存在しないためマッチしない
print(re.search('ab?c', 'ac')) # bが0回であり、a,cもきちんと存在するためマッチ
print(re.search('ab?c', 'abbbbc')) # bが0回または1回ではないためマッチしない

# 「|」のパターン　or を意味する
print(re.search('abc|012', 'abc')) # abcがあるため、マッチ
print(re.search('abc|012', '012')) # 012があるため、マッチ
print(re.search('abc|012', 'ab12')) # 「abc」・「012」がないため、マッチしない

# 「()」のパターン　グループを表す 「|」を使う場合などに、対象のパターンを限定したい時に使う。
print(re.search('te(s|x)t', 'test')) # sが入っているのでマッチ
print(re.search('te(s|x)t', 'text')) # xが入っているのでマッチ
print(re.search('te(s|x)t', 'tedt')) # sでもxでもないためマッチしない

# 「.」のパターン 任意の1文字
print(re.search('h.t', 'hot')) # マッチ
print(re.search('h.t', 'hit')) # マッチ
print(re.search('h.t', 'hbt')) # マッチ
print(re.search('h.t', 'hbit')) # マッチしない

# 「\」のパターン エスケープ 次の文字をメタキャラクターではなく、単なる文字として判定する
print(re.search('h\.t', 'hot')) # 「.」はメタキャラクターではなく、単なるドットとして判定のため、マッチしない
print(re.search('h\.t', 'h.t')) # こちらがマッチする

# 「\w」のパターン　[a-zA-Z0-9_]の意味：つまり全てのアルファベット、数字およびアンダースコアを意味する
print(re.search('h\wt', 'hit')) # マッチ
print(re.search('h\wt', 'hiit')) # \wは1文字だけを表すのでマッチしない
print(re.search('h\wt', 'h0t')) # マッチ 数字もOK
print(re.search('h\wt', 'h_t')) # マッチ アンダースコアもOK
print(re.search('h\wt', 'h.t')) # マッチしない　ドットは対象外


"""
正規表現を用いた課題
①：input()で入力した生年月日(yyyy/mm/dd)のフォーマットが
正しいフォーマットになっているかをチェックするプログラムを正規表現で作る
(暦の正しさは一旦無視する　例：2025/11/31はOK)

②：input()で入力されたemailアドレスのフォーマットが
正しいフォーマットになっているかをチェックするプログラムを作る
"""

# 課題①
# def input_birthday():
#     birthday = input('生年月日(yyyy/mm/dd)を入力してください。')
#
#     if re.search('[0-9]{4}/[0-9]{2}/[0-9]{2}', birthday):
#         print(f'生年月日の入力を受け付けました({birthday})')
#     else:
#         print('yyyy/mm/ddの形式で入力してください')
#         return input_birthday()
#
# print(input_birthday())

# #↓模範回答
# pattern_dob = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([0-9]|1[0-9]|2[0-9]|3[01])$"
# while True:
#     dob = input('生年月日(yyyy/mm/dd)を入力してください')
#     result = re.search(pattern_dob, dob)
#     if result:
#         print(f'{dob}は正しいフォーマットです')
#         break
#     else:
#         print(f'{dob}は正しくないフォーマットです')

# 課題②
pattern_email= '^(\w|\.|-)+@(\w|\.|-)+\.([A-Z]|[a-z]){2,3}$'
while True:
    email_address = input('メールアドレスを入力してください')
    result = re.search(pattern_email, email_address)
    if result:
        print(f'メールアドレスの入力を受け付けました。({email_address})')
        break
    else:
        print('アドレスのフォーマットが正しくありません。')