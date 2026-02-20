import json
import boto3

# Initialize the Glue client
client = boto3.client('glue')

def lambda_handler(event, context):
    # Specify the name of your AWS Glue Job
    # Replace 'glue-job-test' with your actual job name from the console
    glue_job_name = "glue-job-test"
    
    try:
        # Trigger the Glue job
        response = client.start_job_run(JobName=glue_job_name)
        
        # Return the Job Run ID for tracking
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully triggered Glue job: {glue_job_name}"),
            'jobRunId': response['JobRunId']
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error triggering Glue job: {str(e)}")
        }
