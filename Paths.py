paths = [['London','NY'],['NY','Lima'],['Lima','SP']]

def findDestination(paths):
    outs = set()
    ins = set()

    for a,b in paths:
        ins.add(a)
        outs.add(b)

    diff = outs - ins
    return diff

print(findDestination(paths))
