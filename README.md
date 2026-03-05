# Cloud Sales Analytics Dashboard (Nigeria E-Commerce)

## 🎯 Project Objective
The objective of this project was to build an end-to-end data pipeline to analyze the annual sales performance of a Nigerian E-Commerce store for 2023 and 2024. By integrating Python, AWS cloud storage, and Power BI, the dashboard provides actionable insights into customer behavior, regional sales distribution, and revenue trends to drive growth in 2025.

## 📊 Dashboard Preview
![Dashboard Screenshot](das# Cloud Sales Analytics Dashboard (Nigeria E-Commerce)

## 🎯 Project Objective
The objective of this project was to build an end-to-end data pipeline to analyze the annual sales performance of a Nigerian E-Commerce store for 2023 and 2024. By integrating Python, AWS cloud storage, and Power BI, the dashboard provides actionable insights into customer behavior, regional sales distribution, and revenue trends to drive growth in 2025.

## 📊 Dashboard Preview
![Dashboard Screenshot](https://github.com/mohimpact/cloud-sales-dashboard/blob/main/dashboards/screenshots/executive_summary.png?raw=true)

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.11 (Pandas for cleaning, Boto3 for AWS integration)
* **Cloud:** AWS S3 (Data Lake storage)
* **Visualization:** Power BI (DAX, Power Query)
* **Version Control:** GitHub

## ❓ Questions (KPIs) Addressed
* **Sales vs. Time:** Compare revenue and order trends across 2023 and 2024.
* **Top Performing Region:** Which Nigerian cities/states contribute the most to total sales?
* **Category Analysis:** Which product category (Electronics, Fashion, Beauty, Home) is the highest seller?
* **Customer Value:** What is the Average Order Value (AOV) across the platform?
* **Growth Metrics:** What is the Year-over-Year (YoY) revenue growth compared to targets?

## 🏗️ The Process
1.  **Environment Setup:** Configured Python 3.11 and installed essential libraries including `pandas`, `boto3`, and `python-dotenv`.
2.  **Data Generation & Cleaning:** * Generated a unique dataset of 20,000 Nigerian e-commerce transactions using Python.
    * Cleaned data using Pandas to handle null values, format dates, and engineer time-based features (Month, Quarter, Year).
3.  **Cloud Integration:** Created an **AWS S3 Bucket** and used an IAM user with programmatic access to automate the upload of processed data from the local environment to the cloud.
4.  **Data Modeling:** * Connected Power BI to the S3 data source.
    * Developed a custom **DAX DateTable** for time-intelligence.
    * Created measures for `Total Revenue`, `Total Orders`, `AOV`, and `YoY Growth %`.
5.  **Dashboard Design:** Built an interactive UI with dynamic slicers for Year, Month, and City to allow for deep-dive analysis.

## 💡 Project Insights
* **Revenue Milestone:** Total revenue reached **₦15.07bn** across 20,000 orders.
* **Regional Hubs:** **Imo State** and the South-Eastern region emerged as the primary revenue drivers.
* **High-Ticket Items:** The **Average Order Value (AOV)** is approximately **₦753K**, suggesting a customer base focused on premium electronics and high-end goods.
* **Category Balance:** Sales are evenly distributed across Home, Fashion, Beauty, and Electronics, with each category contributing nearly **₦3.7bn**.
* **Growth Performance:** Despite a downward monthly trend in 2024, the YoY growth showed a **+94.73%** increase over the set goal in the primary reporting view.

## 🏁 Final Conclusion & Recommendations
To improve performance in 2025, the business should:
1.  **Target the South-East:** Implement regional marketing campaigns in Imo and surrounding states where purchase density is highest.
2.  **High-Value Retention:** Since the AOV is high (₦750k+), introduce installment payment options (Buy Now, Pay Later) to sustain sales during low-revenue months.
3.  **Trend Intervention:** Investigate the consistent monthly revenue decline observed in 2024 to determine if it is due to market competition or supply chain issues.

---
*Created as part of the Cloud Sales Dashboard Portfolio Project.*hboards/screenshots/executive_summary.png) 
*Note: Replace with your actual screenshot path*

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.11 (Pandas for cleaning, Boto3 for AWS integration)
* **Cloud:** AWS S3 (Data Lake storage)
* **Visualization:** Power BI (DAX, Power Query)
* **Version Control:** GitHub

## ❓ Questions (KPIs) Addressed
* **Sales vs. Time:** Compare revenue and order trends across 2023 and 2024.
* **Top Performing Region:** Which Nigerian cities/states contribute the most to total sales?
* **Category Analysis:** Which product category (Electronics, Fashion, Beauty, Home) is the highest seller?
* **Customer Value:** What is the Average Order Value (AOV) across the platform?
* **Growth Metrics:** What is the Year-over-Year (YoY) revenue growth compared to targets?

## 🏗️ The Process
1.  **Environment Setup:** Configured Python 3.11 and installed essential libraries including `pandas`, `boto3`, and `python-dotenv`.
2.  **Data Generation & Cleaning:** * Generated a unique dataset of 20,000 Nigerian e-commerce transactions using Python.
    * Cleaned data using Pandas to handle null values, format dates, and engineer time-based features (Month, Quarter, Year).
3.  **Cloud Integration:** Created an **AWS S3 Bucket** and used an IAM user with programmatic access to automate the upload of processed data from the local environment to the cloud.
4.  **Data Modeling:** * Connected Power BI to the S3 data source.
    * Developed a custom **DAX DateTable** for time-intelligence.
    * Created measures for `Total Revenue`, `Total Orders`, `AOV`, and `YoY Growth %`.
5.  **Dashboard Design:** Built an interactive UI with dynamic slicers for Year, Month, and City to allow for deep-dive analysis.

## 💡 Project Insights
* **Revenue Milestone:** Total revenue reached **₦15.07bn** across 20,000 orders.
* **Regional Hubs:** **Enugu State** and the South-Eastern region emerged as the primary revenue drivers.
* **High-Ticket Items:** The **Average Order Value (AOV)** is approximately **₦753K**, suggesting a customer base focused on premium electronics and high-end goods.
* **Category Balance:** Sales are evenly distributed across Home, Fashion, Beauty, and Electronics, with each category contributing nearly **₦3.7bn**.
* **Growth Performance:** Despite a downward monthly trend in 2024, the YoY growth showed a **+94.73%** increase over the set goal in the primary reporting view.

## 🏁 Final Conclusion & Recommendations
To improve performance in 2025, the business should:
1.  **Target the South-East:** Implement regional marketing campaigns in Enugu and surrounding states where purchase density is highest.
2.  **High-Value Retention:** Since the AOV is high (₦750k+), introduce installment payment options (Buy Now, Pay Later) to sustain sales during low-revenue months.
3.  **Trend Intervention:** Investigate the consistent monthly revenue decline observed in 2024 to determine if it is due to market competition or supply chain issues.

