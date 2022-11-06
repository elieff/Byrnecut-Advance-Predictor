#!/usr/bin/env python
# coding: utf-8

# In[1]:


def encode(frame, column):
    from sklearn.preprocessing import OneHotEncoder
    import numpy as np
    import pandas as pd
    y = frame[[column]]
    ohe = OneHotEncoder(categories="auto", handle_unknown="error", sparse=False)
    ohe.fit(y)
    encod = ohe.transform(y)
    encod = pd.DataFrame(encod,
    columns=ohe.categories_[0],
    index= frame.index)
    encod.drop(columns = encod.columns[0], axis=1, inplace=True)
    return encod

def evaluate(y_tr, y_te, y_tr_pr, y_te_pr, log=False):
    from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    import numpy as np
    import pandas as pd
    if log == True:
        y_tr = np.exp(y_tr)
        y_te = np.exp(y_te)
        y_tr_pr = np.exp(y_tr_pr)
        y_te_pr = np.exp(y_te_pr)
        
    # residuals
    train_res = y_tr - y_tr_pr
    test_res = y_te - y_te_pr
    
    print(f'Train R2 score: {r2_score(y_tr, y_tr_pr)} ')
    print(f'Test R2 score: {r2_score(y_te, y_te_pr)} ')
    print('')
    print(f'Train RMSE: {mean_squared_error(y_tr, y_tr_pr, squared=False):,.2f} ')
    print(f'Test RMSE: {mean_squared_error(y_te, y_te_pr, squared=False):,.2f} ')
    print('')
    print(f'Train MAE: {mean_absolute_error(y_tr, y_tr_pr):,.2f} ')
    print(f'Test MAE: {mean_absolute_error(y_te, y_te_pr):,.2f} ')
    
    

