"""
常用元字符
.       匹配除换行符以外的任意字符
\w      匹配字母或数字或下划线
\s      匹配任意的空白符
\d      匹配数字
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开始
$       匹配字符串的结尾
\W      匹配非字母或数字或下划线
\D      匹配非数字
\S      匹配非空白符
a|b     匹配字符a或字符b
()      匹配括号内的表达式，也表示一个组
[...]   匹配字符组中的字符
[^...]  匹配除了字符组中的字符的所有字符

量词：控制前面的元字符出现的次数
*       重复零次或更多次
+       重复一个或更多次
?       重复零次或一次
{n}     重复n次，如\d{5}
{n,}    重复n次或更多次
{n,m}   重复n到m次

贪婪匹配和惰性匹配
.*      贪婪匹配
.*?     惰性匹配

------------------------------------
------------------------------------

实例：
str：晚吃饥饿sd游戏csdcsdc游戏
reg：晚.*?游戏
---->返回：'晚吃饥饿sd游戏'，.*?表示尽可能少的匹配
该语句的执行顺序是，先匹配到了 晚吃饥饿sd游戏csdcsdc游戏，然后往回找找了.*最少的那个

str：<div>胡辣汤</div>
reg：<.*?>
---->返回：<div>
        </div>
    匹配到两个结果
"""
