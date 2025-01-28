# **Healthcare Data Analysis Project**

## **Overview**

This project involves a detailed analysis of healthcare data to uncover patterns, trends, and insights across various domains, including hospitals, insurance providers, medical conditions, medications, billing amounts, and length of patient stays. The analysis was performed using Python, leveraging libraries like pandas, matplotlib, and seaborn for data manipulation and visualization.

**Objectives**

*The primary objectives of the project were:*

To identify the top-performing hospitals based on the number of patients and specialization in medical conditions.

To evaluate insurance providers based on their coverage and association with specific medical conditions.

To analyze the most commonly prescribed medications and their frequency.

To study trends in billing amounts across hospitals, medical conditions, and insurance providers.

To assess the length of patient stays in relation to medical conditions and admission types.

To provide actionable insights for improving patient care and operational efficiency in healthcare institutions.

**Key Questions Addressed**

*1. Hospitals*

Which hospitals handle the most patients?

Identified the top 10 hospitals based on patient count.

Visualization: A bar chart was created to highlight the top hospitals and the number of patients handled.

Exported top 3 hospitals for each condition to a CSV file.

*2. Medications*

Which medications are prescribed most frequently?

Generated a list of the top 10 most prescribed medications and their counts.

Visualization: A bar chart displaying medication counts with annotations.

*3. Insurance Providers*

Which insurance providers dominate in terms of patient coverage?

Ranked insurance providers by the number of patients covered.

Visualization: A bar chart showing the top 10 insurance providers and patient counts.

*4. Length of Stay*

How does the length of stay vary based on medical conditions or admission types (urgent, elective, etc.)?
Calculated the average length of stay for each combination of medical condition and admission type.

*5. Billing Insights*

What are the average billing amounts across different medical conditions or hospitals?

Computed average billing amounts by medical condition and hospital.

Visualization: Separate bar charts for medical conditions and hospitals, annotated with billing values.

Are there trends in billing amounts based on insurance providers?

Analyzed average billing amounts by insurance provider.

Visualization: A bar chart for the top 10 insurance providers, annotated with billing values.

*6. Patients Demographics*

Distribution between male and female admissions?

Distribution of medical conditions?

Distribution of Admission type?

Distribution of Test Results?

Distribution of Age?

Most common medical condition by age and Gender?


## **Tools and Technologies Used**

Python Libraries: pandas, matplotlib, seaborn

Data Visualization: Bar charts, heatmaps, and annotations for data representation.

File Exports: CSV files for hospital and insurance provider insights.

**Findings and Insights**

*Medications*

Most frequent medical condition

![image](https://github.com/user-attachments/assets/67d9342e-9908-4219-a2dc-b7154d009a40)

Seasonal medical trends

![image](https://github.com/user-attachments/assets/3ab6c406-29f0-42c3-92fc-c321df8b9f47)


A small subset of medications dominated prescriptions, indicating potential areas for cost optimization or focused inventory management.

![Image](https://github.com/user-attachments/assets/6a7ae3d3-c1fa-404e-b2ef-e343b9f38f97)

Top 10 Doctors with most patients attended

![image](https://github.com/user-attachments/assets/272753df-5a1e-412d-97a9-9ee2ec268ab5)

Speciality doctor for respective medical conditions

![image](https://github.com/user-attachments/assets/3d437d72-8e7b-4aa9-8adc-2ed3c863ce46)

*Insurance Providers*

Share of all the insurance providors

![image](https://github.com/user-attachments/assets/93a6152c-3315-4511-a2f7-fdab06458c98)



A few insurance providers covered a majority of patients, highlighting market dominance.

Specific providers showed preferences for covering certain medical conditions, offering opportunities for partnerships or negotiations.

![Image](https://github.com/user-attachments/assets/a432a3ec-19ff-40b4-a2dd-0e9356839841)

*Hospitals*

The top-performing hospitals handled significantly more patients compared to others.
Specialization analysis revealed specific hospitals excel in treating particular medical conditions, aiding targeted referrals and resource allocation.

![Image](https://github.com/user-attachments/assets/bf126cbc-719b-4653-8851-7af0a0f4129b)

*Monthly admission trends*

![image](https://github.com/user-attachments/assets/5a947b38-0112-4d00-bf3c-bbd3b254b48a)

*Yearly admissions in respective months

![image](https://github.com/user-attachments/assets/05b2f9f6-21f6-442c-a5fe-cc8acf5c2c97) - 2019
![image](https://github.com/user-attachments/assets/7b6a2ef4-492c-4c52-b483-37cee75b1fc7) - 2020
![image](https://github.com/user-attachments/assets/b902f833-28c7-4d14-bf3d-878bd6f7e81e) - 2021
![image](https://github.com/user-attachments/assets/c5c3e7a3-0f6e-44a9-96cb-cdb401451e21) - 2022
![image](https://github.com/user-attachments/assets/73c03882-beff-49a0-989f-2fdba4c92561) - 2023
![image](https://github.com/user-attachments/assets/af43e395-c72e-416f-bd0c-deb6a0988bbf) - 2024


*Length of Stay*

The length of stay analysis revealed patterns based on admission type and medical condition, providing insights for capacity planning and operational efficiency.

![Image](https://github.com/user-attachments/assets/28408549-68a2-4c70-bcca-a79ef8c5ea0c)

*Patients Demographics*

Distribution between male and female admissions?

![image](https://github.com/user-attachments/assets/1a1215cd-ec0d-4b21-b761-0a6c4a3e4db3)

Distribution of medical conditions?

![Image](https://github.com/user-attachments/assets/d425fae8-446b-47d1-9174-e64e787f5ce9)

Distribution of Admission type?

![Image](https://github.com/user-attachments/assets/f9ecf717-588f-4756-8f8a-49c966ec36da)

Distribution of Test Results?

![Image](https://github.com/user-attachments/assets/977eb872-b10a-45e3-b00f-8551dbaec196)

Distribution of Age?

![image](https://github.com/user-attachments/assets/470c4355-0e5a-4da1-967e-b4e4f8d9f18d)

Most common medical condition by age and Gender?

![Image](https://github.com/user-attachments/assets/4fc76366-b4cd-4e28-99a5-5a98a1f54786)

**Conclusions**

The analysis provided actionable insights into multiple aspects of healthcare operations. By leveraging these findings, healthcare providers can optimize patient care, manage costs effectively, and streamline operations. Furthermore, these insights can guide decision-making for partnerships, resource allocation, and strategic planning.

**Recommendations*

Resource Allocation: Allocate resources to hospitals specializing in high-demand medical conditions.
Medication Optimization: Streamline the supply chain for the most prescribed medications to reduce costs.
Insurance Negotiations: Use billing and coverage data to negotiate better rates with dominant insurance providers.
Operational Efficiency: Utilize length of stay insights for better hospital capacity planning and improved patient turnover.
Further Analysis: Conduct a deeper dive into seasonal trends or regional variations to enhance strategic planning.

**Future Scope**

Predictive Analytics: Develop machine learning models to predict patient outcomes, readmission risks, or billing amounts.
Seasonal Analysis: Analyze seasonal patterns in patient admissions, medical conditions, and billing amounts.
Patient Satisfaction: Integrate patient feedback data to correlate operational metrics with satisfaction scores.
This document encapsulates the comprehensive efforts undertaken in this project and provides a foundation for continuous improvement in healthcare analytics.

