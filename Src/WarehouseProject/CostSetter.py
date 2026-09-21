import ast

import pandas as pd


def check_startpoint(df):

    # Chech if user has set a custom main road through warehouse and return P_l and P_r if so, else return False

    return True

def get_input_data():
    
    # Get input data from csv file and return as a pandas dataframe. Standin for the test data may change in future.

    df = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/warehouse_data.csv")

    return df

def calculate_d(P_l, P_r, input_data):

    D_l =[]

    # Find the maximum "distance" to the furthest local in the warehouse. This assumes that 1 shelf position is equal to 1 unit of distance.
    # Also currently temporary for testing purposes.

    d_max = max(max(row) for row in input_data)
    
    # Calculate the normalized D_l value for each local in each row.
    for elem in range(len(input_data[0])):
        
        norm_distance = input_data[0][elem] / d_max
        D_l.append(norm_distance)
        print(D_l)

    return D_l

data = get_input_data()

# Convert pd dataframe to list of lists
data_list = data['rows'].apply(ast.literal_eval).to_list()

print(data_list[0][0],type(data_list[0]))
calculate_d(1, 2, data_list)
