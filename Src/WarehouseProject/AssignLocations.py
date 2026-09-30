
import pandas as pd
from scipy.optimize import linear_sum_assignment



def get_cost_data():
    
    # Read the total cost data from the CSV file and return it as a pandas dataframe.
    total_cost_data = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/cost_matrix.csv",
                                  index_col="ware_id")

    return total_cost_data


def assign_locations(total_cost_data):

   

    cost_matrix = total_cost_data.values

    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    for row, col in zip(row_ind, col_ind):

        ware = total_cost_data.index[row]
        location = total_cost_data.columns[col]
        cost = total_cost_data.iloc[row, col]

        print(ware, "→", location, "Cost:", cost)

    assignments = []

    for row, col in zip(row_ind, col_ind):

        assignments.append({
            "ware_id": total_cost_data.index[row],
            "location": total_cost_data.columns[col],
            "cost": total_cost_data.iloc[row, col]
        })

    assignment_df = pd.DataFrame(assignments)

    assignment_df.to_csv(
        "Warehouse_Project/Tests/TestData/GenData/assignments.csv",
        index=False
)


total_cost_data = get_cost_data()
assign_locations(total_cost_data)
