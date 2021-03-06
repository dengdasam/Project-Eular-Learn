
'''

欧拉计划 题目 002

偶数项斐波那契数列之和

斐波那契数列中的每一项都是前两项的和。由1和2开始生成的斐波那契数列前10项为：

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

计算该斐波那契数列中不超过400万的项，求其中偶数项之和。

分析:

斐波那契数列，可以使用元组元素交换，不断生成；同时设初始值为0的和，不断与偶数项相加，当数列数值大于400万，即停止迭代


'''


def solution():
	ans = 0
	a = 1  # 数列第1项
	b = 2  # 数列第2项
	while a <= 4000000:
		if b % 2 == 0:
			ans += x
		a, b = b, a + b
	return str(ans)


if __name__ == "__main__":
	print(solution())
