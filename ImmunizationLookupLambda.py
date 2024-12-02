import boto3
import json
from datetime import datetime

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Extract ImmunizationID from the event payload
    # Use for testing: immunization_id = event.get('ImmunizationID')
    immunization_id = event.get('Details', {}).get('Parameters', {}).get('ImmunizationID')
    
    if not immunization_id:
        return {
            "StatusCode": 400,
            "Message": "ImmunizationID is required."
        }
    
    # Query DynamoDB table
    try:
        response = dynamodb.get_item(
            TableName='ImmunizationRecords',
            Key={'ImmunizationID': {'S': immunization_id}}
        )
    except Exception as e:
        return {
            "StatusCode": 500,
            "Message": f"Error querying DynamoDB: {str(e)}"
        }

    # Check if record exists
    record = response.get('Item')
    if not record:
        return {
            "StatusCode": 404,
            "Message": "Immunization record not found."
        }

    # Extract relevant fields
    last_vaccination_date = record['LastVaccinationDate']['S']
    overdue_vaccinations = record.get('OverdueVaccinations', {}).get('SS', [])
    
    # Determine status
    status = "UpToDate" if not overdue_vaccinations else "Overdue"
    
    return {
        "StatusCode": 200,
        "Status": status,
        "LastVaccinationDate": last_vaccination_date,
        "OverdueVaccinations": overdue_vaccinations
    }