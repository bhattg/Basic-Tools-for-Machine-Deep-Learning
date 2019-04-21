import random
def make_batch(x, y, batch_size=32):
    l = []
    batch_list=[]
    assert x.shape[0]==y.shape[0]
    m = x.shape[0]
    for i in range(m):
        l.append((x[i], y[i]))
    j=0
    random.shuffle(l)
    while j<m:
        if j+batch_size < m:
            batch_list.append(l[j:j+batch_size])
        else:
            batch_list.append(l[j:])
        j+=batch_size
    return batch_list