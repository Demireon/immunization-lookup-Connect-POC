
# Child Immunization Lookup POC

Amazon Connect Demo: Child Immunization Record Lookup and Appointment Scheduling

## Overview

This repository contains a proof-of-concept (POC) for a simple Amazon Connect-based solution that demonstrates how foundational AWS services can be used to automate common call center use cases. The goal is to show how integrating Amazon Connect with AWS Lambda and DynamoDB can reduce call center workloads by automating responses to frequently asked questions.

## Use Case:
This POC simulates a health department call center handling child immunization record lookups and appointment scheduling for overdue vaccinations. Callers interact with an Amazon Connect contact flow that retrieves immunization records from DynamoDB and schedules appointments for overdue vaccinations.

This project was timeboxed to 10 hours and serves as a demonstration of Amazon Connect fundamentals and the power of serverless AWS integrations.

## Features

	Amazon Connect Contact Flow:
    	•	Captures user input (e.g., Immunization ID) via keypad (DTMF).
    	•	Invokes AWS Lambda to query immunization records from DynamoDB.
    	•	Handles conditional logic for overdue vaccinations and prompts callers to schedule appointments.
	AWS Lambda Functions:
    	•	Immunization Lookup:
    	•	Queries the ImmunizationRecords DynamoDB table for child vaccination records.
    	•	Determines whether the child is up-to-date or overdue for vaccinations.
    	•	Appointment Scheduling:
    	•	Queries the AppointmentSlots DynamoDB table for available appointment slots.
    	•	Reserves the first available slot and associates it with the caller’s Immunization ID.
	DynamoDB Tables:
    	•	ImmunizationRecords:
    	•	Stores child immunization records, including last vaccination date and overdue vaccines.
    	•	AppointmentSlots:
    	•	Stores available appointment slots with their reservation status.
	Business Value:
    	•	Reduces the need for live agents to handle common, repetitive queries.
    	•	Streamlines operations, saving resources and improving customer experience.

## How it works

	Caller Interaction:
    	•	The caller enters their child’s Immunization ID using their phone keypad.
    	•	The system retrieves the child’s vaccination record from DynamoDB.
    	•	If the child is overdue, the caller can schedule an appointment via the same flow.
	Automation:
    	•	Immunization records and appointment slots are dynamically retrieved and updated using AWS Lambda functions.
    	•	Conditional logic in the contact flow directs the caller based on the record status.

## Future Enhancements

	CloudFormation:
	•	Automate the creation of Amazon Connect, DynamoDB tables, and Lambda functions for seamless deployment.
	Advanced Contact Flow Features:
	•	Add voice interaction using Amazon Lex for a conversational experience.
	•	Enable call recording and analytics for tracking call flow effectiveness.
	Improved Appointment Management:
	•	Allow users to cancel or reschedule appointments via self-service options.
	API Integrations:
	•	Integrate with external health department APIs to pull live immunization data.
	Security Enhancements:
	•	Implement stricter input validation and encryption for sensitive data.
