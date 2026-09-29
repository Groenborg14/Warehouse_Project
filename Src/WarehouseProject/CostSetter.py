import ast

import pandas as pd


def check_startpoint(df):

    # Chech if user has set a custom main road through warehouse and return P_l and P_r if so, else return False

    return True

def get_input_data():
    
    # Get input data from csv file and return as a pandas dataframe. Standin for the test data may change in future.

    df = pd.read_csv("Warehouse_Project/Tests/TestData/GenData/warehouse_data_v2.csv")

    return df

def calculate_d(P_l, P_r, input_data, identifiers):

    # P_l and P_r are dummy variables for now and are not used until "main road" functionility is implemented.


    results = []

    # Find the maximum "distance" to the furthest local in the warehouse. This assumes that 1 shelf position is equal to 1 unit of distance.
    # Also currently temporary for testing purposes.

    d_min = min(min(row) for row in input_data)
    d_max = max(max(row) for row in input_data)
    
    # Calculate the min-max normalized D_l value for each local in each row.
    for rows in range(len(input_data)):
        row_distances = []
        temp_identifier = []
        for elem in range(len(input_data[0])):
            
            norm_distance = (input_data[rows][elem] - d_min) / (d_max - d_min) 
            results.append({"D_l": norm_distance, "identifier": identifiers[rows], "Position": elem})
            #print(D_l)
        


    #Create a pandas dataframe from the D_l list and the identifiers list and save it to a csv file.
    
    pd.DataFrame(results).to_csv("Warehouse_Project/Tests/TestData/GenData/D_l_data.csv", index=False)

    

def calculate_r(input_data, identifiers):

    # Calculate R_l for each local in the rows

    results = []
    
    

    total_postions = len(input_data[0]) * len(input_data) -1

    
    r_max = total_postions  # Assuming the maximum value is the total number of locals in the warehouse.
    
    for row in range(len(input_data)):
        
        for elem in range(len(input_data[row])):
            global_position = row * len(input_data[row]) + elem
            norm_r = global_position / r_max

            results.append({"Rl": norm_r, "identifier": identifiers[row], "Position": elem})
        


    #Create a pandas dataframe from the R_l list and the identifiers list and save it to a csv file.
            
    pd.DataFrame(results).to_csv("Warehouse_Project/Tests/TestData/GenData/R_l_data.csv", index=False)
  

data = get_input_data()

# Convert pd dataframe to list of lists
data_list = data['rows'].apply(ast.literal_eval).to_list()
identifiers = data['identifier']
#print(identifiers[3], len(identifiers))
#print(data_list[0][0],len(data_list))
calculate_d(1, 2, data_list, identifiers)
calculate_r(data_list, identifiers)

