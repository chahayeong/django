# *********************
# --- Data Type ---
# *********************

'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
Vector : List, Tuple, Dictionary, Set

hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])

Python List

'''

# List CRUD Example

ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
# Read: ls 의 목록을 출력
# Update: ls와 tinyls 의 결합
# Delete: ls 에서 786을 제거

ls.append(100)
print(ls)
ls2 = ls + tinyls
print(ls2)
ls.remove(786)
print(ls)



# Tuple CRUD Example

tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
# Read: tp 의 목록을 출력
# Update: tp와 tinytp 의 결합
# Delete: tp 에서 786을 제거

tplist = list(tp)
tplist.append(100)
tp = tuple(tplist)
print(tp)
tp2 = tp + tinytp
print(tp2)
tplist = list(tp)
tplist.remove(786)
tp = tuple(tplist)
print(tp)




# dictionary CRUD Example

dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍': 30}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
# Read: dt 의 목록을 출력
# Update: dt와 tinydt 의 결합
# Delete: dt 에서 'abcd' 제거

dt['tom'] = 100
print(dt)
dt.update(tinydt)
print(dt)
del(dt['abcd'])
print(dt)

