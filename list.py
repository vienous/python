#append
list_1 = [1,2,3];
list_1.append(4);
print(list_1);

#count
list_2 = [1,2,3,4,3,5,4,5];
print(list_2.count(4));

#extend 改变a
a = [1,2,3];
b = [4,5];
a.extend(b);
print(a);
 
#index

list_3 = ['a','s','d','g'];
print(list_3.index('d'));
#print(list_3.index('v')); 报错

#insert
list_4 = [1,2,3,4,5];
list_4.insert(2,1);
print(list_4);

#pop  返回数组
list_5 = [1,2,3]
print(list_5.pop());

print(list_5.pop(0));

#remove 移除第一个匹配的元素
list_6 = ['1','a','a'];
list_6.remove('a');
print(list_6);

#reverse()

#sort  不返回值
a = [3,2,1];
#不可以 y=a.sort;

y = a[:];
y.sort();
print(y)



#sort(key,reverse)    //key=len,reverse=ture

