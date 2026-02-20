# AWS Data Engineering ETL Project


**📌 Project Overview**

This project demonstrates a robust end-to-end ETL (Extract, Transform, Load) pipeline built on AWS. The objective is to automate the transformation of raw data from an Amazon S3 source and deliver processed data in Parquet format to a destination bucket using AWS Glue, with automation handled by AWS Lambda.

<img width="1419" height="800" alt="image" src="https://github.com/user-attachments/assets/314a89a7-418a-42d2-bc1d-dbc22a11ce88" />





**🏗 Architecture & Workflow**

The pipeline follows a step-by-step automated flow:

Data Ingestion: Raw CSV data is uploaded from a local system to an Amazon S3 input folder.

Metadata Discovery: An AWS Glue Crawler scans the S3 bucket to infer the schema and populate the AWS Glue Data Catalog.

Data Transformation: An AWS Glue ETL Job (Visual Studio) is used to perform data manipulation, such as dropping unnecessary fields (e.g., "seller" info).

Data Loading: The transformed data is written back to an S3 output folder in Apache Parquet format for optimized querying.

Automation: An AWS Lambda function (Python/Boto3) is configured to trigger the Glue job automatically.

Analysis: Amazon Athena is used to verify and query the data at various stages using standard SQL.


**🛠 Step-by-Step Implementation**

1. Storage Setup (Amazon S3)

Created an S3 bucket with a structured folder hierarchy: input/ for raw data and output/ for processed results.

Uploaded product_data.csv to the input folder to serve as the data source.

2. Data Cataloging (AWS Glue Crawler)

Configured a Crawler to point to the S3 input location.

The Crawler identifies the schema (Marketplace, Customer ID, Product ID, etc.) and creates a metadata table in the Glue Data Catalog.

Verification: Used Amazon Athena to run SQL queries against the raw data to ensure the Crawler captured the schema correctly.

3. ETL Job Development (AWS Glue Studio)

Source: Linked the job to the Glue Data Catalog table.

Transform: Applied a "Drop Fields" transformation to remove specific columns not required for business analysis.

Target: Set the output destination to the S3 output/ folder, converting the format from CSV to Parquet for better performance.

4. Automation (AWS Lambda)

Created a Lambda function using the Python runtime.

Implemented a script using the Boto3 library to programmatically start the Glue ETL job.

Assigned IAM roles with necessary permissions (S3, Glue, CloudWatch) to allow the Lambda function to manage the pipeline.



**⚠️ Challenges & Troubleshooting**

Permissions (IAM): Encountered access issues during the setup. Resolved by creating custom IAM roles with specific policies for Glue, S3, and Lambda to communicate securely.

Job Optimization: Configured "Worker Types" and "Timeouts" within Glue to manage costs and prevent long-running hanging processes.



**🚀 Key Takeaways**

Scalability: The use of Parquet and AWS Glue allows this pipeline to handle large-scale datasets efficiently.

Serverless: The entire architecture is serverless, meaning no infrastructure management is required.

Automation: By integrating Lambda, the pipeline can be triggered by events (like a new file upload), making it a hands-off solution.
