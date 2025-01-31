# **Healthcare Data Analysis Project**

## **Overview**
This project involves a comprehensive analysis of healthcare data to uncover insights into hospitals, insurance providers, medical conditions, medications, billing amounts, and patient stay durations. Using Python with pandas, matplotlib, and seaborn, we performed data cleaning, exploration, and visualization to derive actionable insights.

## **Objectives**
- Identify top-performing hospitals based on patient volume and specialization.
- Analyze insurance providers' market share and coverage trends.
- Determine the most commonly prescribed medications.
- Study billing trends across hospitals, medical conditions, and insurance providers.
- Assess patient stay duration by medical condition and admission type.
- Provide insights to optimize healthcare operations and patient care.

## **Key Questions Addressed**
### **1. Hospitals**
- **Which hospitals handle the most patients?**
  - Identified the top 10 hospitals based on patient count.
  - **Visualization:** Bar chart showcasing hospital rankings.
  - **Data Export:** CSV file with the top 3 hospitals per condition.

### **2. Medications**
- **Which medications are prescribed most frequently?**
  - Ranked the top 10 most prescribed medications.
  - **Visualization:** Bar chart displaying prescription frequency.

### **3. Insurance Providers**
- **Which insurance providers dominate patient coverage?**
  - Ranked insurance providers by patient coverage volume.
  - **Visualization:** Market share distribution chart.

### **4. Length of Stay**
- **How does length of stay vary based on medical condition and admission type?**
  - Analyzed the average stay duration for different admission types.
  - **Visualization:** Heatmap illustrating stay durations.

### **5. Billing Insights**
- **What are the average billing amounts across hospitals and medical conditions?**
  - Analyzed billing amounts per medical condition and hospital.
  - **Visualization:** Annotated bar charts.

- **Are there billing trends by insurance provider?**
  - Assessed average billing amounts covered by each insurance provider.
  - **Visualization:** Bar chart of top 10 insurance providers by billing trends.

### **6. Patient Demographics**
- **Analyzed various distributions, including:**
  - Gender-based admissions.
  - Most common medical conditions.
  - Admission types and test result distributions.
  - Age-wise medical condition trends.

## **Tools and Technologies Used**
- **Python Libraries:** pandas, matplotlib, seaborn
- **Data Visualization:** Bar charts, heatmaps, and annotations
- **File Exports:** CSV files for insights on hospitals and insurance providers

## **Findings and Insights**
### **Medications**
- **Most frequent medical conditions:**
  ![image](https://github.com/user-attachments/assets/67d9342e-9908-4219-a2dc-b7154d009a40)
- **Seasonal medical trends:**
  ![image](https://github.com/user-attachments/assets/3ab6c406-29f0-42c3-92fc-c321df8b9f47)
- **Medication trends:**
  ![Image](https://github.com/user-attachments/assets/6a7ae3d3-c1fa-404e-b2ef-e343b9f38f97)

### **Insurance Providers**
- **Market share analysis:**
  ![image](https://github.com/user-attachments/assets/93a6152c-3315-4511-a2f7-fdab06458c98)
- **Trends in insurance coverage:**
  ![Image](https://github.com/user-attachments/assets/a432a3ec-19ff-40b4-a2dd-0e9356839841)

### **Hospitals**
- **Hospital rankings and specialization analysis:**
  ![Image](https://github.com/user-attachments/assets/bf126cbc-719b-4653-8851-7af0a0f4129b)

### **Monthly Admission Trends**
  ![image](https://github.com/user-attachments/assets/5a947b38-0112-4d00-bf3c-bbd3b254b48a)

### **Length of Stay**
- **Patterns in hospital stay duration:**
  ![Image](https://github.com/user-attachments/assets/28408549-68a2-4c70-bcca-a79ef8c5ea0c)

### **Patients Demographics**
- **Gender distribution:**
  ![image](https://github.com/user-attachments/assets/1a1215cd-ec0d-4b21-b761-0a6c4a3e4db3)
- **Most common medical conditions by age and gender:**
  ![Image](https://github.com/user-attachments/assets/4fc76366-b4cd-4e28-99a5-5a98a1f54786)

## **Conclusions**
The analysis provided insights to optimize healthcare operations. Findings can be used to:
- Improve patient care and resource allocation.
- Streamline procurement for frequently prescribed medications.
- Optimize billing structures with insurance providers.
- Enhance hospital efficiency through better length-of-stay management.

## **Recommendations**
- **Resource Allocation:** Allocate resources based on hospital specialization.
- **Medication Optimization:** Optimize supply chain for high-demand medications.
- **Insurance Negotiations:** Leverage billing data for better provider contracts.
- **Operational Efficiency:** Improve patient turnover through length-of-stay insights.

## **Future Scope**
- **Predictive Analytics:** Machine learning models for patient outcomes and readmission risks.
- **Seasonal Trends:** Further analysis on medical trends over different years.
- **Patient Satisfaction:** Integrating feedback data for quality improvement.

---

### **Setup & Execution**
1. **Clone Repository:**
   ```bash
   git clone https://github.com/your-repo/healthcare-data-analysis.git
   cd healthcare-data-analysis
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Analysis Scripts:**
   ```bash
   python analysis_script.py
   ```

This document serves as a detailed overview of the healthcare data analysis project, providing structured insights for improving healthcare analytics.
