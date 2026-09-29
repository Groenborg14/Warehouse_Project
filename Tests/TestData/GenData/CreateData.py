import pandas as pd
import re



def create_data(rows, amount_locals):

    # Create made up data of warehouse locals.
    warehouse_list = []

    for i in range(rows):

        list_temp = []
        for j in range(amount_locals):
            list_temp.append(j + 1)

        warehouse_list.append(list_temp)



    return warehouse_list

def get_input():
    #print("Please enter the number of rows in the warehouse:")
    rows = int(input("Please enter the number of rows in the warehouse:"))
    #print("Please enter the number of locals in each row:")
    amount_locals = int(input("Please enter the number of locals in each row:"))
    #print("Please enter the unique identifier for the rows (e.g. 'A', 'B', 'C', etc.):")
    row_identifier = input("Please enter the unique identifier for the rows (e.g. 'A', 'B', 'C', etc.):")
    print("You have entered the following information:")
    print(f"Number of rows: {rows}")
    print(f"Number of locals in each row: {amount_locals}")
    print(f"Row identifier: {row_identifier}")
    print("Creating warehouse data...")


    warehouse_list = create_data(rows, amount_locals)

    row_identifier = re.split(r'\s*,\s*', row_identifier)  # Split the input string into a list of identifiers

    data = {"rows": warehouse_list, "locals": amount_locals, "identifier": row_identifier}


    df = pd.DataFrame(data)

    df.to_csv("Warehouse_Project/Tests/TestData/GenData/warehouse_data_v2.csv", index=False)


get_input()


#warehouse_list = create_data(10, 13)
#print(warehouse_list)








    