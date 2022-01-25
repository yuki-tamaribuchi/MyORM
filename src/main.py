from platformdirs import user_cache_dir
from models.entry import Entry
from models.users import Users



#entry=Entry(writer=1, title="sample")
#entry.save()
#print(entry.__dict__)




#動作確認済分

#テーブル作成 (作成するテーブルをmodel.__init__内のmodelsリストに追加しておく)
#from framework.operates.create_table import create_all_table
#create_all_table()

#createメソッドで作成
#user = Users().objects.create(username="yuki", lucky_number=1)


#インスタンスのgetメソッドでデータを取得
#user = Users().objects.get(username="yuki").run()
#print(user)


#get + カラム指定
#user=Users().objects.get(username="yuki", lucky_number=1).columns("username", "lucky_number").run()
#print(user)


user = Users().objects.filter({"username":"yuki"},{"username":"sample"}).run()
print(user)


#ANDでフィルター
#entry = Entry().objects.filter(writer="3", title="sample").run()
#print(entry)



#関連テーブルも同時にget
#entry = Entry().objects.get(title="sample").select_related("writer").run()
#entry = Entry().objects.get(title="sample").select_related("writer").columns("title").run()
#print(entry)










#以下SQL発行は未実装


#インスタンスのupdateメソッドで値を更新
#user = Users().objects.create(username="yuki", lucky_number=1)
#Users().objects.update(lucky_number = 2).filter(username="yuki", lucky_number=1).run()

#Users().objects.update(lucky_number = 2).filter({"username":"yuki"},{"username":"sample"}).run()


#インスタンスのdeleteメソッドで削除
#user.objects.delete()