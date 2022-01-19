from models.users import Users


#直接渡してデータをセットし、保存する方法
#user=Users(username="yuki")
#user.save()
#print(user)


#createメソッドにデータを渡し保存する方法
user = Users().objects.create(username="yuki", lucky_number=1)
print(user)


#インスタンスのupdateメソッドで値を更新
#user = Users().objects.create(username="yuki", lucky_number=1)
#user.objects.update(lucky_number = 2)

#インスタンスのdeleteメソッドで削除
#user = Users().objects.create(username="yuki", lucky_number=1)
#user.objects.delete()


#インスタンスのgetメソッドでデータを取得
#user = Users().objects.create(username="yuki", lucky_number=1)
#user2 = Users().objects.get(username="yuki")