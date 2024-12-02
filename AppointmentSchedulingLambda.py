import boto3
import json

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AppointmentSlots')

def lambda_handler(event, context):
    # Extract ImmunizationID (required for associating with appointment)
    # Use for testing: immunization_id = event.get('ImmunizationID')
    immunization_id = event.get('Details', {}).get('Parameters', {}).get('ImmunizationID')
    
    if not immunization_id:
        return {
            "StatusCode": 400,
            "Message": "ImmunizationID is required."
        }
    
    # Query for available slots
    try:
        response = table.scan(
            FilterExpression="Available = :available",
            ExpressionAttributeValues={":available": True}
        )
    except Exception as e:
        return {
            "StatusCode": 500,
            "Message": f"Error querying DynamoDB: {str(e)}"
        }
    
    available_slots = response.get('Items', [])
    if not available_slots:
        return {
            "StatusCode": 404,
            "Message": "No available appointment slots."
        }

    # Reserve the first available slot
    slot = available_slots[0]
    slot_id = slot['SlotID']
    
    try:
        table.update_item(
            Key={'SlotID': slot_id},
            UpdateExpression="SET Available = :available, ImmunizationID = :immunization_id",
            ExpressionAttributeValues={
                ":available": False,
                ":immunization_id": immunization_id
            }
        )
    except Exception as e:
        return {
            "StatusCode": 500,
            "Message": f"Error updating DynamoDB: {str(e)}"
        }

    # Return the reserved slot details
    return {
        "StatusCode": 200,
        "ScheduledSlot": {
            "SlotID": slot_id,
            "Date": slot["Date"],
            "Time": slot["Time"],
            "ImmunizationID": immunization_id
        }
    }