Lista = [ 5, 9, 13]

Lista.append(15)
Lista.append(99)
Lista.append(55)
Lista.append(88)
Lista.append(8)
for x, e in enumerate(Lista):
    print(f"[{x}]  = {e}")

Lista.sort()
print(Lista)
Lista.sort(reverse=True)
print('{Lista} '.format(Lista.sort()))