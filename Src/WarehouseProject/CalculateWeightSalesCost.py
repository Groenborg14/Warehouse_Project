import pandas as pd




def get_data():

    # Read the R_l and D_l data from the CSV files and return them as pandas dataframes.
    R_l_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/R_l_data.csv")
    D_l_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/D_l_data.csv")


    # Read the ware data from the CSV file and return it as a pandas dataframe.
    wares = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/test_wares.csv")

    return R_l_data, D_l_data, wares



def calculate_cost_weight(wares):

    w_min = wares['weight_kg'].min()
    w_max = wares['weight_kg'].max()
    w_c= []

    for ware in wares['weight_kg']:
        #w = wares.loc[wares['ware_id'] == ware, 'weight_kg'].values[0]
        norm_w = float((ware - w_min) / (w_max - w_min))
        w_c.append(norm_w)

    data = {"ware_id": wares['ware_id'],"weight_kg": wares['weight_kg'], "w_c": w_c}
    pd.DataFrame(data).to_csv("Warehouse_Project/Tests/TestData/GenData/w_c_data.csv", index=False)

    
    return w_c

def calculate_cost_sales(wares):

    s_min = wares['sales_per_month'].min()
    s_max = wares['sales_per_month'].max()
    s_c= []

    for ware in wares['sales_per_month']:
        #s = wares.loc[wares['ware_id'] == ware, 'sales_per_month'].values[0]
        norm_s = float((ware - s_min) / (s_max - s_min))
        s_c.append(norm_s)

    data = {"ware_id": wares['ware_id'],"sales_per_month": wares['sales_per_month'], "s_c": s_c}
    pd.DataFrame(data).to_csv("Warehouse_Project/Tests/TestData/GenData/s_c_data.csv", index=False)

    print(s_c, len(s_c))
    return s_c
        

R_l_data, D_l_data, wares = get_data()

calculate_cost_weight(wares)
calculate_cost_sales(wares)


    


