import random
import numpy as np
def make_batch(x, y, batch_size=32):
    l = []
    batch_list=[]
    assert x.shape[0]==y.shape[0]
    m = x.shape[0]
    for i in range(m):
        l.append((x[i], y[i]))
    j=0
    random.shuffle(l)
    x_list = []; y_list=[]
    for i in range(len(l)):
    	x, y = l[i]
    	x_list.append(x)
    	y_list.append(y)
    x = np.asarray(x_list)
    y = np.asarray(y_list)
    while j<m:
        if j+batch_size < m:
            batch_list.append((x[j:j+batch_size], y[j:j+batch_size]))
        else:
            batch_list.append((x[j:], y[j:]))
        j+=batch_size
    return batch_list