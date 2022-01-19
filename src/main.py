from models.users import Users


from models.entry import Entry
from framework.sqls.create_table import generate_create_table_sql

generate_create_table_sql(Entry)


#entry=Entry(writer=1, title="sample")
#entry.save()
#print(entry.__dict__)





#動作確認済分

#テーブル作成 (作成するテーブルをmodel.__init__内のmodelsリストに追加しておく)
#from framework.operates.create_table import create_all_table
#create_all_table()



#以下SQL発行は未実装

#直接渡してデータをセットし、保存する方法
#user=Users(username="yuki")
#user.save()
#print(user)


#createメソッドにデータを渡し保存する方法
#user = Users().objects.create(username="yuki", lucky_number=1)
#print(user)


#インスタンスのupdateメソッドで値を更新
#user = Users().objects.create(username="yuki", lucky_number=1)
#user.objects.update(lucky_number = 2)

#インスタンスのdeleteメソッドで削除
#user = Users().objects.create(username="yuki", lucky_number=1)
#user.objects.delete()


#インスタンスのgetメソッドでデータを取得
#user = Users().objects.create(username="yuki", lucky_number=1)
#user2 = Users().objects.get(username="yuki")
