
'''
题目：

3的倍数和5的倍数

如果我们列出10以内所有3或5的倍数，我们将得到3、5、6和9，这些数的和是23。
求1000以内所有3或5的倍数的和。

'''


def solution():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


if __name__ == "__main__":
	print(solution())