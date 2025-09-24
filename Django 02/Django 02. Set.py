st = {25, 98, 7, 95, 25}
st1 = {25, 97, 7, 256}

# print(st)
# print(st1)

print(st.union(st1))
print(st | st1)

print(st.difference(st1))
print(st - st1)

print(st.intersection(st1))
print(st & st1)