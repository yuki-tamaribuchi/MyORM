from models.entry import Entry
from models.users import Users



#動作確認済分


#テーブル作成 (作成するテーブルをmodel.__init__内のmodelsリストに追加しておく)
#from framework.operates.create_table import create_all_table
#create_all_table()


#createメソッドで作成
#user = Users().objects.create(username="yuki", lucky_number=1).run()
#entry = Entry().objects.create(title="sample2", writer=4).run()


#インスタンスのgetメソッドでデータを取得
#user = Users().objects.get(username="yuki").run()
#print(user)


#get + カラム指定
#user=Users().objects.get(username="yuki", lucky_number=1).columns("username", "lucky_number").run()
#print(user)


#get + 関連テーブル取得
#entry = Entry().objects.get(title="sample").select_related("writer").run()
#print(entry)


#ANDでフィルター
#entry = Entry().objects.filter(writer="3", title="sample").run()
#print(entry)


#関連テーブルも同時にget
#entry = Entry().objects.get(title="sample").select_related("writer").run()
#entry = Entry().objects.get(title="sample").select_related("writer").columns("title").run()
#print(entry)


#ANDフィルター＋関連テーブル取得
#entry = Entry().objects.filter(writer="3", title="sample").select_related("writer").run()
#print(entry)


#delete + フィルター
#ただし、フィルターを指定シない場合は全削除になる
#Entry().objects.delete().filter(id=1).run()


#update + フィルター
#Users().objects.update(lucky_number=3).filter(username="yuki").run()


#フィルター + オーダー(asc)
#users = Users().objects.filter(lucky_number=3).order_by("id").run()
#print(users)


#フィルター + オーダー(desc)
#users = Users().objects.filter(lucky_number=3).order_by("id").reverse().run()
#print(users)


#フィルター + リミット
#users = Users().objects.filter(lucky_number=3).limit(10).run()
#print(users)


#エラー発生分



#getに関連テーブルのカラムを指定して取得
#entry = Entry().objects.get(lucky_number=1).select_related("writer").run()
#print(entry)





#サンプルファイル

#from framework.operates.create_table import create_all_table
#from samples.insert import insert_users, insert_entry
#create_all_table()
#insert_users(1000)
#insert_entry(1000)

#user = Users().objects.filter(username="sample100").run()
#print(user)


#entry = Entry().objects.filter(title="sample1").select_related("writer").run()
#print(entry)

#entry = Entry().objects.get(title="sample1").select_related("writer").run()
#print(entry)
user=Users().objects.get(username="sample1").run()

entry = Entry().objects.create(title="sample0000", writer=user["Users"]["id"]).run()
print(entry)