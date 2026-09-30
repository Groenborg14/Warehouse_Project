import pandas as pd
from hungarian_algorithm import algorithm



# Hard coded weights

alpha = 0.6
beta = 0.4



def get_data():

    # Read the R_l and D_l data from the CSV files and return them as pandas dataframes.
    R_l_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/R_l_data.csv")
    D_l_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/D_l_data.csv")


    # Read the cost data from the CSV files and return them as pandas dataframes.
    weight_cost_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/w_c_data.csv")
    sales_cost_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/s_c_data.csv")


    return R_l_data, D_l_data, weight_cost_data, sales_cost_data


def calculate_cost(R_l_data,D_l_data, weight_cost,sales_cost):

    total_cost = []
    
    for wares in range(len(weight_cost)):
        i = 0
        for local in range(len(R_l_data)):
            # Calculate the total cost for each ware based on the formula provided.

            cost = alpha * abs(R_l_data['Rl'][local] - (1-weight_cost['w_c'][wares]))+ beta * (sales_cost['s_c'][wares] * D_l_data['D_l'][local])
            
            
            total_cost.append({"ware_id": weight_cost['ware_id'].iloc[wares], 
                              "location": R_l_data['identifier'].iloc[local] + str(i),
                              "total_cost": cost})
            i+=1
            if i == 18:
                i = 0
                

    
    pd.DataFrame(total_cost).to_csv("Warehouse_Project/Tests/TestData/GenData/total_cost_data.csv", index=False)
    df = pd.DataFrame(total_cost)
    cost_matrix = df.pivot(
        index="ware_id",
        columns="location",
        values="total_cost"
    )

    cost_matrix.to_csv(
        "Warehouse_Project/Tests/TestData/GenData/cost_matrix.csv"
    )



r_l_data, D_l_data, weight_cost, sales_cost = get_data()
calculate_cost(r_l_data,D_l_data, weight_cost,sales_cost)




