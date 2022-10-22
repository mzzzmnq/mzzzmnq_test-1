print(514)
print(1.14)
print("野兽先辈")

# 字面量：固定的值
# 常见字面量：整数，浮点数，字符串
# ＃号和注释内容一般建议用一个空格隔开

money = 0
print(money)
money = money + 10
print("野兽先辈被撅:", money, "元")
money = money + 10
print("野兽先辈被撅第二次花费:", money, "元")
# 变量

print(type("野兽先辈"))
print(type(514))
# str是string：字符串

name = "野兽先辈"
name_type = type(name)
print(name_type)
# 变量没有类型

num_str = str(11)
print(type(num_str))
print(num_str, )
float_str = str(1.14)
print(type(float_str), float_str)
# 啥都能转字符串str

# 字符串内必须全是数字才能转

float_num = (114)
print(type(float_num), float_num)
# int整数随便转float浮点数

int_num = int(5.14)
print(type(int_num), int_num)
# float浮点数转int整数丢失精度

""" 标识符
    1.数字不能作为开头
    2.大小写区分
    3.关键词
"""

print(11*4)
print("11 * 4 = ", 11 * 4 )
print(11%4)
num = 1
num += 1
print("num += 1 : ", num)
print(num)
# //取整除，**平方，%取余数

