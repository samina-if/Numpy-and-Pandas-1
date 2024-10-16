import streamlit as st
import pandas as pd
import numpy as np
import os

def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_kelvin(c):
    return c + 273.15

def user_name(name):
    name = input("Enter user Name: ")
    return name

def main():
    # Create an empty DataFrame to store all user data
    all_data = pd.DataFrame(columns=["user_name", "temperature_Values", "Kelvin_Temperature"])
    st.title("---Temperature Conversion system-----")
    choose=st.selectbox("Enter option:", ("Convert Celsius to Fahrenheit","Convert Celsius to Kelvin","show data","Exit"))
    if choose == "Convert Celsius to Fahrenheit":
            name = ""
            name_record = user_name(name)
            temp = st.number_input("Enter temperature value in Celsius: ")
            if st.button("Convert"):
              c_array = np.array([float(value) for value in temp.split(",")])
              f_array = celsius_fahrenheit(c_array)
              st.success(f"The temperature in Fahrenheit is: {f_array} & {name_record} entered input for conversion")

            # Prepare data for DataFrame
            dic = {"user_name": name_record, "temperature_Values": f_array}
            df = pd.DataFrame(dic)
            # all_data.append(df) = pd.concat(all_data, ignore_index=True)
            # append the new row to the original DataFrame

            all_data= pd.concat([all_data, df], ignore_index=True)     # Save all data to Excel
            all_data.to_excel("temp.xlsx", index=False)

    elif choose == "Convert Celsius to Kelvin":
            name = ""
            name_record = user_name(name)
            temp =st.number_input("Enter temperature value in Celsius: ")
            if st.button("Convert"):
              c_array = np.array([float(value) for value in temp.split(",")])
              k_array = celsius_kelvin(c_array)
              st.success(f"The temperature in Kelvin is: {k_array} & {name_record} entered input for conversion")

            # Prepare data for DataFrame
            dic1 = {"user_name": name_record, "Kelvin_Temperature": k_array}
            df1 = pd.DataFrame(dic1)
            all_data = pd.concat([all_data, df1], ignore_index=True)

            # Save all data to Excel
            all_data.to_excel("temp.xlsx", index=False)

    elif choose == "show data":
            # Read the Excel file and display the data

            with pd.option_context('display.max_rows', None,):
              df2 = pd.read_excel('temp.xlsx')
              print(df2)
    elif choose == "Exit":
         st.success("Exiting the program.")
         #break
    else:
        print("Invalid option. Please try again.")

main()
