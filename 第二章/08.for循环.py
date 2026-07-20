# #for循环:遍历输入的字符串
#
# msg = input("请输入需要遍历的字符串:")
#
# for s in msg: #s 表示遍历出来的元素;msg表示需要遍历的数据
#     print(f"元素:{s}")
# else:
#     print("遍历结束")

#案例1: 计算1-100之间的奇数和
total = 0
#原始版本
for i in range(1,101):
    if i % 2 == 1:
        total += i

#简化版本
for i in range(1,101,2):
    total += i

print(total)







