# python_cookbook
print 语句调用str()函数显示对象，而交互式解释器则调用repr()函数来显示对象。
print 中带逗号的语句输出元素之间会自动添加一个空格。通过指定输出格式，程序员可以最大程度的控制输出布局，也不用担心这些自动添加的空格。它也可以将所有数据放到一处输出——只需要将数据放在格式化运算符右侧的元组或字典中。
  who = 'knights'
  what = 'Ni!'
  print('We are the %s who say %s' %  (who, ( (what + ' ') * 4)))


_在解释器中有特别的含义，表示最后一个表达式的值。
