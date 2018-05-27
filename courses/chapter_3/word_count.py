
# coding:utf8

def main():
	""" 主函数 """
	zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
	"""
	print(zen)
	# 统计词频
	word_dict = {}
	for word in zen.split():
		#print(word)
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
		# 更高效的方式
		word_dict[word] += word_dict.get(word, 0)
	print('word\tcount\n%s'%('='*20))
	for k in word_dict:
		print('%s\t%s'%(k, word_dict[k]))

if __name__ == "__main__":
	print('开始调用主函数')
	main()
