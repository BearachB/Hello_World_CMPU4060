a_set = {"the", "coat", "had", "many", "colors", "red", "blue", "yellow"}
b_set = {"my", "coat", "had", "two", "main", "colors", "red", "blue"}

#Qa
print("----- Question A -----")
x= a_set.intersection(b_set)
y= b_set.intersection(a_set)
print(x)
print(y)

#Qb
print("----- Question B -----")
w = a_set.union(b_set)
v = a_set.union(a_set)
print(w)
print(v)

#Qc
print("----- Question C -----")
t = a_set.difference(b_set)
u = b_set.difference(a_set)
print(t)
print(u)

#Qd
print("----- Question D -----")
r = a_set.symmetric_difference(b_set)
s = b_set.symmetric_difference(a_set)
print(r)
print(s)
