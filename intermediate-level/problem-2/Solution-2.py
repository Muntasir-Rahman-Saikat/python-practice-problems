x=["bat", "tab", "cat", "act"]
group={}

for i in x:
    key="".join(sorted(i))
    if key not in group:
        group[key]=[i]
    else:
        group[key].append(i)
print(group)
