# data_collect.py 多源零售数据采集
import pandas as pd
import numpy as np
import random
from datetime import datetime,timedelta

# 设置随机种子
np.random.seed(2026)

# 1. 采集订单数据
order_num = 2000
order_data = {
    "order_id":[f"OD{str(i).zfill(6)}" for i in range(order_num)],
    "user_id":[f"U{str(random.randint(1,500)).zfill(4)}" for _ in range(order_num)],
    "goods_id":[f"G{str(random.randint(1,200)).zfill(4)}" for _ in range(order_num)],
    "order_amount":np.random.uniform(10,500,order_num).round(2),
    "order_num":np.random.randint(1,5,order_num),
    "pay_status":np.random.randint(0,2,order_num),
    "order_time":pd.date_range("2026-01-01","2026-06-01",freq="H",periods=order_num)
}
df_order = pd.DataFrame(order_data)

# 2. 采集用户数据
user_data = {
    "user_id":[f"U{str(i).zfill(4)}" for i in range(1,501)],
    "user_age":[random.randint(15,60) for _ in range(500)],
    "user_gender":[random.choice(["男","女",None]) for _ in range(500)],
    "user_level":[random.choice(["普通","会员","VIP"]) for _ in range(500)]
}
df_user = pd.DataFrame(user_data)

# 3. 采集商品数据
goods_data = {
    "goods_id":[f"G{str(i).zfill(4)}" for i in range(1,201)],
    "goods_name":[f"零售商品{i}" for i in range(1,201)],
    "goods_type":[random.choice(["零食","饮品","日用","美妆"]) for _ in range(200)],
    "goods_price":np.random.uniform(5,300,200).round(2)
}
df_goods = pd.DataFrame(goods_data)

# 人为制造脏数据（适配课程预处理实验）
df_order.loc[df_order.sample(frac=0.05).index,"order_amount"] = np.nan  # 缺失值
df_order.loc[df_order.sample(frac=0.02).index,"order_amount"] = 99999 # 异常极值
df_order = pd.concat([df_order,df_order.sample(frac=0.03)]) # 重复数据

# 保存原始采集数据（对应ODS原始数据）
df_order.to_csv("raw_order.csv",index=False,encoding="utf-8")
df_user.to_csv("raw_user.csv",index=False,encoding="utf-8")
df_goods.to_csv("raw_goods.csv",index=False,encoding="utf-8")

print("=====多源数据采集完成=====")
print("原始订单数据量：",df_order.shape)
print("原始用户数据量：",df_user.shape)
print("原始商品数据量：",df_goods.shape)