import pickle
import json
import numpy as np

locations=None
model=None
columns=None

def load_location():

    with open("column.json",'r') as f:
        global locations
        global columns
        columns=json.load(f)['data_columns']
        locations=columns[3:]

        return locations


def load_model():

    with open('bangalorea_house_prices.pickle','rb') as f:
        global model
        model=pickle.load(f)



        
def predict_price(loc,bhk,area,bath):
    
 

    try:
        ind=columns.index(loc.lower())
    except:
        ind=-1
    
    load_location()
    load_model()
    x=np.zeros(len(columns))

    x[0]=bhk
    x[1]=area
    x[2]=bath

    if ind>=0:
        x[ind]=1
    
    return model.predict([x])[0].round(3)


if __name__=='__main__':
    load_location()
    load_model()
    print(predict_price('1st Phase JP Nagar',2,1000,2))
    