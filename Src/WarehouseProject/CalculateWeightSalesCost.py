import pandas as pd




def get_data():

   

    # Read the ware data from the CSV file and return it as a pandas dataframe.
    wares = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/test_wares.csv")

    return wares



def calculate_cost_weight(wares):

    w_min = wares['weight_kg'].min()
    w_max = wares['weight_kg'].max()
    w_c= []

    for weight in wares['weight_kg']:
        #w = wares.loc[wares['ware_id'] == ware, 'weight_kg'].values[0]
        norm_w = float((weight - w_min) / (w_max - w_min))
        w_c.append(norm_w)

    data = {"ware_id": wares['ware_id'],"weight_kg": wares['weight_kg'], "w_c": w_c}
    pd.DataFrame(data).to_csv("Warehouse_Project/Tests/TestData/GenData/w_c_data.csv", index=False)

    


def calculate_cost_sales(wares):

    s_min = wares['sales_per_month'].min()
    s_max = wares['sales_per_month'].max()
    s_c= []

    for sale in wares['sales_per_month']:
        #s = wares.loc[wares['ware_id'] == ware, 'sales_per_month'].values[0]
        norm_s = float((sale - s_min) / (s_max - s_min))
        s_c.append(norm_s)

    data = {"ware_id": wares['ware_id'],"sales_per_month": wares['sales_per_month'], "s_c": s_c}
    pd.DataFrame(data).to_csv("Warehouse_Project/Tests/TestData/GenData/s_c_data.csv", index=False)

   
    
        

wares = get_data()

calculate_cost_weight(wares)
calculate_cost_sales(wares)


    


