import pandas as pd
import numpy as np




def create_data(rows, amount_locals):

    # Create made up data of warehouse locals.
    warehouse_list = []

    for i in range(rows):

        list_temp = []
        for j in range(amount_locals):
            list_temp.append(j + 1)

        warehouse_list.append(list_temp)

    return warehouse_list



warehouse_list = create_data(10, 13)
print(warehouse_list)

data = {"rows": warehouse_list}

df = pd.DataFrame(data)

df.to_csv("Warehouse_Project/Tests/TestData/GenData/warehouse_data.csv", index=False)





    