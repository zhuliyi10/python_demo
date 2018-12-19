import pickle

# 我们将要存储对象的文件名
shoplistfile = 'shoplist.data'

# 购物清单
shoplist = ['苹果', '芒果', '胡萝卜']

# 定到文件
f = open(shoplistfile, 'wb')

pickle.dump(shoplist, f)
f.close()

del shoplist  # 释放shoplist变量

# 从仓库读回
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
f.close()
print(storedlist)
