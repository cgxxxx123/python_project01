# # 常见数据类型 --- >type()获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello")) #str
#
# print(type(10)) #int
# print(type(3.14))  #flaot
# print(type(True))   #bool
# print(type(False))  #bool
# print(type(None))   #NoneType
#
# num = 100
# print(type(num))  #int
#
# # 常见数据类型 --- >isinstance(数据、类型) -- >bool值→>判定数据是否是指定的类型,如果是:True,否则:False
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))

# #字符串
# #定义字符串的三种方式
#
# s1 = "Hello"
# s2 = 'World'
# s3 = """
# 哈喽
# 这里是三引号字符串呦
# 可以换行呦
# """#注释应该放到外面哦,上面的三引号是不行的呦
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# #单引号定义字符串特殊情况(\'转义字符)
# msg = 'It\'s very easy!'
# print(msg)
#
# msg2 = "It's very easy!"
# print(msg2)
#
# msg3 ="Hello 的意思就是\"您好\""
# print(msg3)
#
# msg4 = 'Hello 的意思就是 \"您好\"'
# print(msg4)
#
# print("欢迎大家进入到Python课程的学习!\n大家记得一键三连哦~")

#字符串拼接
s1 = "人生苦短" "我用python"  ",ok"
print(s1)

msg1 = "人生苦短"
msg2 = "我用python"
print("龟叔说:"+msg1+","+msg2)

# 案例 :--- >str(int数字) --- >将int类型的数字转为字符串
#案例:大家好,我是涛哥,今年18岁,学习的专业是软件工程,爱好Python、Java"

# 字符串格式化 -- > 方式一:%s 占位符
name = "涛哥"
age = 18
pro="软件工程"
hobby = "Python. Java"
print("大家好,我是%s今年%s岁,I学习的专业是%s,爱好%s"   %(name,age,pro,hobby))

# 字符串格式化 -- >方式二:f" .. {变量名/表达式} .. ”----->推荐方式
name = "涛哥"
age = 18
pro="软件工程"
hobby = "Python. Java"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")