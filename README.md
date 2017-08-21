# python_cookbook

## print
print 语句调用str()函数显示对象，而交互式解释器则调用repr()函数来显示对象。    
print 中带逗号的语句输出元素之间会自动添加一个空格。通过指定输出格式，程序员可以最大程度的控制输出布局，也不用担心这些自动添加的空格。它也可以将所有数据放到一处输出——只需要将数据放在格式化运算符右侧的元组或字典中。    
	  who = 'knights'   
	  what = 'Ni!'   
	  print('We are the %s who say %s' %  (who, ( (what + ' ') * 4)))    
	
## _ special meaning
* _在解释器中有特别的含义，表示最后一个表达式的值。   
* _xxx 不用‘from module import *’ 导入。而且一般来京，变量名_xxx被看作是私有的，在模块或类外不可以使用。当变量是私有的时候，用_xxx来表示变量是很好的习惯。因为变量名__xxx__对python来说有特殊含义。对于普通的变量应当避免。
* __xxx__ 系统定义名字
* __xxx 类中的私有变量名

## __init__() 函数
__init__()可以被当成构建函数，不过不像其他语言中的构造函数，它并不创建实例--它仅仅是对象创建后执行的第一个方法。它的目的是执行一些该对象的必要初始化工作。通过创建自己的__init__()方法，可以覆盖默认的__init__()方法（默认的方法什么也不做），从而能够修饰刚刚创建的对象。在这个例子里，我们初始化一个名为name的类实例属性（或者说成员）。这个变量仅在类实例中存在，它并不是实际类本身的一部分。  	
	
## PEP = Pythin Enhancement Proposal  

## 跨行
有两种例外情况一个语句不使用反斜线也可以跨行。在使用闭合操作符时，单一语句可以跨多行，例如：在含有小括号/中括号/花括号时可以多行书写。另外就是三个引号包括下的字符串也可以跨行书写。

## 对象计数器   
每个对象都天生具有一个计数器，记录它自己的引用次数。这个数目表示有多少个变量指向该对象。Python提供了is和is not运算符来测试两个变量是否指向同一个对象。    
a is b 这个表达式等价于下面的表达式 if id(a) == id(b)   

## 垃圾回收
虽然解释器会跟踪对象的引用计数，但是垃圾收集器负责释放内存。垃圾收集器是一块独立代码，它用来寻找引用计数为0的对象，它也负责检查那些虽然引用计数大于0，但也应该被销毁的对象，特定情形会导致循环引用。       
一个循环引用发生在当至少两个对象相互引用时，也就是说所有的引用都消失时，这些引用仍然存在，这说明只靠引用技术是不够的。Python的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。当一个对象的引用计数器变为0，解释器会暂停，释放掉这个对象和仅有这个对象可访问（可到达）的其他对象。作为引用计数的补充，垃圾收集器也会留心被分配的总量很大（及未通过引用计数器销毁的那些）的对象。在这种情况下，解释器会暂停下来，试图清理所有未引用的循环。    

