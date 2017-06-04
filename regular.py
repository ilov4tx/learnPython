

#导入re模块
import re
#将正则表达式编译成Pattern对象，注意hello前面的r的意思是‘原生字符串’
pattern = re.compile(r'cy')

#使用re.match匹配文本，获取匹配结果，无法匹配时将返回None
result1 = re.match(pattern,'cydfdsfcyfsdfsdcy')
result2 = re.match(pattern,'helo')

if result1:
    print(result1.group(0))
else:
    print('1匹配失败!')

if result2:
    print(result2.group())
else:
    print('2匹配失败!')