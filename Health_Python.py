import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the uploaded file to examine its content
file_path = 'healthcare_dataset.csv'
healthcare_data = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the dataset
healthcare_data.head()

# Standardizing text columns and handling date formats
def clean_text_columns(df, columns):
    for col in columns:
        df[col] = df[col].str.strip().str.title()  # Remove extra spaces and capitalize first letters
    return df

# List of text columns to clean
text_columns = ['Name', 'Gender', 'Medical Condition', 'Doctor', 'Hospital', 
                'Insurance Provider', 'Admission Type', 'Medication', 'Test Results']

# Clean text columns
healthcare_data = clean_text_columns(healthcare_data, text_columns)

# Convert date columns to datetime format
date_columns = ['Date of Admission', 'Discharge Date']
for col in date_columns:
    healthcare_data[col] = pd.to_datetime(healthcare_data[col], errors='coerce')

# Display a sample of the cleaned dataset
healthcare_data.head()

# Check for missing values in the dataset
missing_values = healthcare_data.isnull().sum()

# Check for duplicate rows
duplicates = healthcare_data.duplicated().sum()

# Calculate 'Length of Stay' as a new feature (difference between Discharge Date and Admission Date)
healthcare_data['Length of Stay'] = (healthcare_data['Discharge Date'] - healthcare_data['Date of Admission']).dt.days

# Validate numeric columns (e.g., Age, Billing Amount)
numeric_summary = healthcare_data[['Age', 'Billing Amount', 'Room Number', 'Length of Stay']].describe()

# Display missing values, duplicates, and numeric summary
missing_values, duplicates, numeric_summary

# Remove duplicate rows
healthcare_data = healthcare_data.drop_duplicates()

# Investigate rows with negative Billing Amount
negative_billing = healthcare_data[healthcare_data['Billing Amount'] < 0]

# Replace negative Billing Amount values with NaN for now (to decide further action later)
healthcare_data.loc[healthcare_data['Billing Amount'] < 0, 'Billing Amount'] = None

# Display the count of rows removed as duplicates and the rows with negative Billing Amount for investigation
rows_removed = 534  # Duplicates removed earlier
negative_billing


# Function to plot bar graphs with value annotations
def plot_bar_with_values(data, column, title, xlabel, ylabel, rotation=45):
    value_counts = data[column].value_counts()
    plt.figure(figsize=(10, 6))
    ax = value_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=rotation, fontsize=10)
    
    # Annotate bar values
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# Plotting for some key categorical variables
categorical_columns = ['Gender', 'Blood Type', 'Medical Condition', 'Admission Type', 'Test Results']
for column in categorical_columns:
    plot_bar_with_values(
        healthcare_data, 
        column, 
        title=f"Distribution of {column}", 
        xlabel=column, 
        ylabel="Count"
    )

# Plotting for numeric variables
numeric_columns = ['Age', 'Billing Amount', 'Length of Stay']

for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    plt.hist(healthcare_data[column].dropna(), bins=15, color='lightgreen', edgecolor='black', alpha=0.7)
    plt.title(f"Distribution of {column}", fontsize=14)
    plt.xlabel(column, fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(fontsize=10)
    plt.tight_layout()
    plt.show()


# Function to plot bar graphs for bivariate analysis between numeric and categorical variables
def plot_bivariate_bar(data, numeric_col, categorical_col, title, xlabel, ylabel):
    avg_values = data.groupby(categorical_col)[numeric_col].mean().sort_values()
    plt.figure(figsize=(12, 6))
    ax = avg_values.plot(kind='bar', color='coral', edgecolor='black')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    
    # Annotate bar values
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# Bivariate analysis: Bar plots for numeric vs categorical variables
bivariate_pairs = [
    ('Billing Amount', 'Medical Condition', 'Average Billing Amount by Medical Condition'),
    ('Length of Stay', 'Admission Type', 'Average Length of Stay by Admission Type'),
    ('Billing Amount', 'Test Results', 'Average Billing Amount by Test Results'),
    ('Length of Stay', 'Medical Condition', 'Average Length of Stay by Medical Condition')
]

for numeric_col, categorical_col, title in bivariate_pairs:
    plot_bivariate_bar(
        healthcare_data, 
        numeric_col, 
        categorical_col, 
        title=title, 
        xlabel=categorical_col, 
        ylabel=f"Average {numeric_col}"
    )

# Load dataset (assuming healthcare_data is already loaded)
# Create age groups in 10-year intervals starting from 13 years of age
bins_10_years = sorted(list(range(13, 101, 10)) + [healthcare_data['Age'].max() + 1])
labels_10_years = [f"{bins_10_years[i]}-{bins_10_years[i+1]-1}" for i in range(len(bins_10_years)-1)]
healthcare_data['Age Group (10 Years)'] = pd.cut(healthcare_data['Age'], bins=bins_10_years, labels=labels_10_years, right=False)

# Count the most common medical condition for each gender and new age group
common_conditions_10_years = healthcare_data.groupby(['Gender', 'Age Group (10 Years)', 'Medical Condition']).size().reset_index(name='Count')
most_common_conditions_10_years = common_conditions_10_years.loc[common_conditions_10_years.groupby(['Gender', 'Age Group (10 Years)'])['Count'].idxmax()]

# Pivot the data for plotting
plot_data = most_common_conditions_10_years.pivot(index='Age Group (10 Years)', columns='Gender', values='Count').fillna(0)
conditions_data = most_common_conditions_10_years.pivot(index='Age Group (10 Years)', columns='Gender', values='Medical Condition')

# Plot the result
def plot_most_common_conditions(plot_data, conditions_data):
    plt.figure(figsize=(14, 8))
    bar_width = 0.4
    age_groups = plot_data.index
    x = range(len(age_groups))

    # Plot bars for each gender
    plt.bar(x, plot_data['Male'], width=bar_width, label='Male', color='blue', alpha=0.7)
    plt.bar([i + bar_width for i in x], plot_data['Female'], width=bar_width, label='Female', color='orange', alpha=0.7)

    # Annotate bars with the most common medical condition
    for i, age_group in enumerate(age_groups):
        plt.text(i, plot_data['Male'].iloc[i] + 2, conditions_data['Male'].iloc[i], ha='center', fontsize=10, color='blue')
        plt.text(i + bar_width, plot_data['Female'].iloc[i] + 2, conditions_data['Female'].iloc[i], ha='center', fontsize=10, color='orange')

    # Customize the plot
    plt.title('Most Common Medical Conditions by Gender and Age Group (10 Years)', fontsize=16)
    plt.xlabel('Age Group (10 Years)', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks([i + bar_width / 2 for i in x], age_groups, rotation=45, fontsize=12)
    plt.legend(title='Gender', fontsize=12)
    plt.tight_layout()
    plt.show()

# Call the plotting function
plot_most_common_conditions(plot_data, conditions_data)


########################################################

# Load dataset (assuming healthcare_data is already loaded)
# Ensure 'Date of Admission' is in datetime format
healthcare_data['Date of Admission'] = pd.to_datetime(healthcare_data['Date of Admission'], errors='coerce')

# Extract year and month from 'Date of Admission'
healthcare_data['Year'] = healthcare_data['Date of Admission'].dt.year
healthcare_data['Month'] = healthcare_data['Date of Admission'].dt.month

# Group by year and month to count admissions
def plot_admissions_by_month(data):
    years = data['Year'].dropna().unique()
    years = sorted(years)

    for year in years:
        yearly_data = data[data['Year'] == year]
        monthly_counts = yearly_data.groupby('Month').size()

        # Plot the bar graph for the year
        plt.figure(figsize=(10, 6))
        bars = plt.bar(monthly_counts.index, monthly_counts.values, color='skyblue', edgecolor='black')

        # Annotate bars with admission counts
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
                     ha='center', va='bottom', fontsize=10)

        # Customize the plot
        plt.title(f'Admissions by Month for Year {int(year)}', fontsize=16)
        plt.xlabel('Month', fontsize=14)
        plt.ylabel('Number of Admissions', fontsize=14)
        plt.xticks(range(1, 13), 
                   ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
                   fontsize=12)
        plt.tight_layout()
        plt.show()

# Call the function to plot admissions by month for each year
plot_admissions_by_month(healthcare_data)


################################

# Count the number of patients attended by each doctor
doctor_patient_counts = healthcare_data['Doctor'].value_counts().head(10)

# Plot the top 10 doctors with the most patients attended
plt.figure(figsize=(12, 6))
bars = plt.bar(doctor_patient_counts.index, doctor_patient_counts.values, color='purple', edgecolor='black')

# Annotate bars with patient counts
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
             ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Top 10 Doctors with Most Patients Attended', fontsize=16)
plt.xlabel('Doctor', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

##################################



# Group by 'Doctor' to check overall dominance
doctor_total_counts = healthcare_data['Doctor'].value_counts()
print("Total patient count per doctor:")
print(doctor_total_counts)

# Group by 'Medical Condition' and 'Doctor' to find the doctor with the most patients for each condition
doctor_condition_counts = healthcare_data.groupby(['Medical Condition', 'Doctor']).size().reset_index(name='Count')
most_common_doctor_per_condition = doctor_condition_counts.loc[doctor_condition_counts.groupby('Medical Condition')['Count'].idxmax()]

# Check if one doctor dominates across all conditions
print("Checking doctor dominance across conditions:")
doctor_dominance = most_common_doctor_per_condition['Doctor'].value_counts()
print(doctor_dominance)

# Display the result of most common doctor per condition
print("Most common doctor per medical condition:")
print(most_common_doctor_per_condition)

# Plot the result
plt.figure(figsize=(14, 8))
bars = plt.bar(most_common_doctor_per_condition['Medical Condition'], most_common_doctor_per_condition['Count'], 
               color='green', edgecolor='black')

# Annotate bars with doctor names
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             most_common_doctor_per_condition.iloc[i]['Doctor'],
             ha='center', va='bottom', fontsize=10, rotation=90)

# Customize the plot
plt.title('Doctor with Most Patients for Each Medical Condition', fontsize=16)
plt.xlabel('Medical Condition', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

###################################################

# Count the number of patients handled by each hospital
hospital_patient_counts = healthcare_data['Hospital'].value_counts().head(10)

# Plot the top 10 hospitals with the most patients handled
plt.figure(figsize=(12, 6))
bars = plt.bar(hospital_patient_counts.index, hospital_patient_counts.values, color='teal', edgecolor='black')

# Annotate bars with patient counts
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
             ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Top 10 Hospitals with Most Patients Handled', fontsize=16)
plt.xlabel('Hospital', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

#####################################################

# Load dataset (assuming healthcare_data is already loaded)

# Count the number of patients associated with each insurance provider
insurance_provider_counts = healthcare_data['Insurance Provider'].value_counts()

# Plot a pie chart for insurance providers
plt.figure(figsize=(10, 8))
plt.pie(insurance_provider_counts, labels=insurance_provider_counts.index, 
        autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 12})

# Customize the plot
plt.title('Market Share of Insurance Providers', fontsize=16)
plt.tight_layout()
plt.show()

######################################################


# Count the usage of each medication
medication_usage_counts = healthcare_data['Medication'].value_counts().head(10)

# Plot a bar graph for the top 10 most used medications
plt.figure(figsize=(12, 6))
bars = plt.bar(medication_usage_counts.index, medication_usage_counts.values, color='purple', edgecolor='black')

# Annotate bars with usage counts
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
             ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Top 10 Most Used Medications', fontsize=16)
plt.xlabel('Medication', fontsize=14)
plt.ylabel('Usage Count', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()


###########################################################

# Create age groups in 10-year intervals
bins = sorted(set(list(range(0, 101, 10)) + [healthcare_data['Age'].max() + 1]))
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]
healthcare_data['Age Group'] = pd.cut(healthcare_data['Age'], bins=bins, labels=labels, right=False, duplicates='drop')

# Count the number of patients in each age group
age_group_counts = healthcare_data['Age Group'].value_counts().sort_index()

# Plot a bar graph for the age group distribution
plt.figure(figsize=(12, 6))
bars = plt.bar(age_group_counts.index.astype(str), age_group_counts.values, color='teal', edgecolor='black')

# Annotate bars with patient counts
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
             ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Patient Distribution by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()


##########################################################

# Count the number of occurrences for each medical condition
condition_counts = healthcare_data['Medical Condition'].value_counts()

# Plot the most common medical conditions
plt.figure(figsize=(12, 6))
bars = plt.bar(condition_counts.index, condition_counts.values, color='purple', edgecolor='black')

# Annotate bars with counts
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
             ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title('Most Common Medical Conditions', fontsize=16)
plt.xlabel('Medical Condition', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

##############################################################

# Analyze which doctor deals with what medical condition
doctor_condition_counts = healthcare_data.groupby(['Doctor', 'Medical Condition']).size().reset_index(name='Count')
doctor_conditions_summary = doctor_condition_counts.groupby('Doctor')['Medical Condition'].nunique().reset_index()
doctor_conditions_summary.columns = ['Doctor', 'Number of Conditions']

# Display doctors and the conditions they deal with
print("Doctors and the number of conditions they handle:")
print(doctor_conditions_summary)

# Merge condition counts with unique conditions
doctor_condition_details = pd.merge(doctor_condition_counts, doctor_conditions_summary, on='Doctor')

# Display detailed summary
print("Detailed doctor-condition association:")
print(doctor_condition_details)
















