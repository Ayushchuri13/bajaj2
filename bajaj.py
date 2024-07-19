#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json


# In[17]:


import pandas as pd

# Provide the path to your JSON file
file_path = "C:\\Users\\ayush\\Downloads\\DataEngineeringQ2.json"


df = pd.read_json(file_path)


print(df)


# In[20]:


print("Columns in the DataFrame:", df.columns)

# Define the columns to check for missing values (adjust as per actual column names)
columns_to_check = ['firstName', 'lastName', 'DOB']


# In[25]:


patient_details_df = pd.DataFrame(df['consultationData'].tolist())

# Print the columns of the patient_details DataFrame to confirm
print("Columns in 'patientDetails' DataFrame:", patient_details_df.columns)

# Define the columns to check for missing values
columns_to_check = ['firstName', 'lastName', 'DOB']


# In[28]:


patient_details_df = pd.DataFrame(df['consultationData'].tolist())

# Print the columns of the patient_details DataFrame to confirm
print("Columns in 'patientDetails' DataFrame:", patient_details_df.columns)


# In[26]:


percentages = []
for column in columns_to_check:
    if column in patient_details_df.columns:
        missing_count = patient_details_df[column].apply(lambda x: x == '' or pd.isna(x)).sum()
        total_count = len(patient_details_df[column])
        percentage_missing = (missing_count / total_count) * 100
        percentages.append(round(percentage_missing, 2))
    else:
        percentages.append(100.00)  
print(f"{percentages[0]}, {percentages[1]}, {percentages[2]}")


# In[27]:


patient_details_df = pd.DataFrame(df['patientDetails'].tolist())


if 'gender' in patient_details_df.columns:
   
    mode_gender = patient_details_df['gender'].mode()[0]
    patient_details_df['gender'].fillna(mode_gender, inplace=True)
    patient_details_df['gender'].replace('', mode_gender, inplace=True)

    
    total_count = len(patient_details_df)
    female_count = (patient_details_df['gender'] == 'female').sum()
    female_percentage = (female_count / total_count) * 100

   
    print(round(female_percentage, 2))
else:
    print("The 'gender' column does not exist in the DataFrame.")


# In[29]:


patient_details_df = pd.DataFrame(df['patientDetails'].tolist())

# Check if the 'medicines' column exists
if 'medicines' in patient_details_df.columns:
    # Expand the 'medicines' column into a DataFrame
    medicines_df = patient_details_df['medicines'].explode().dropna().reset_index(drop=True)
    medicines_expanded_df = pd.json_normalize(medicines_df)

    # Count the frequency of each 'medicineName'
    medicine_counts = medicines_expanded_df['medicineName'].value_counts()

    # Get the 3rd most frequently prescribed 'medicineName'
    third_most_frequent_medicine = medicine_counts.index[2]

    # Print the 3rd most frequently prescribed medicine name
    print(third_most_frequent_medicine)
else:
    print("The 'medicines' column does not exist in the DataFrame.")


# In[30]:


patient_details_df = pd.DataFrame(df['patientDetails'].tolist())

# Check if the 'medicines' column exists
if 'medicines' in patient_details_df.columns:
    # Calculate the number of medicines prescribed for each patient
    num_medicines = patient_details_df['medicines'].apply(lambda x: len(x) if pd.notna(x) else 0)

    # Calculate the average number of medicines prescribed
    average_medicines = num_medicines.mean()

    # Print the average number of medicines rounded to 2 decimal places
    print(round(average_medicines, 2))
else:
    print("The 'medicines' column does not exist in the DataFrame.")


# In[31]:


def calculate_age(dob):
    if pd.isna(dob) or dob == '':
        return None
    return datetime.now().year - pd.to_datetime(dob).year

# Calculate age for each patient
patient_details_df['age'] = patient_details_df['DOB'].apply(calculate_age)


# In[32]:


phone_pattern = re.compile(r'^\d{10}$')

# Check if the 'phoneNumber' column exists
if 'phoneNumber' in df.columns:
    # Validate phone numbers using the regex pattern
    valid_phone_numbers = df['phoneNumber'].apply(lambda x: bool(phone_pattern.match(str(x))))

    # Count the number of valid phone numbers
    valid_phone_number_count = valid_phone_numbers.sum()

    # Print the number of valid phone numbers
    print(valid_phone_number_count)
else:
    print("The 'phoneNumber' column does not exist in the DataFrame.")


# In[ ]:




