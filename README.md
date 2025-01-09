# DVLA Driver Points Script

An example of a project I completed at my previous employer, designed to improve driver onboarding efficiency by automating a repetitive process.

## Aim

To streamline the driver onboarding process by automating the verification of driver compliance with legal requirements.

## Context

In my previous role, onboarding agents were tasked with manually verifying that drivers had not committed serious offences (e.g., drink driving or driving without insurance) before they could be onboarded onto the platform. This manual process was time-consuming and inefficient.

The verification process required three key pieces of information:

- Driver Licence Number

- National Insurance Number

- Postcode

With driver consent, we could query our internal system to generate a .csv file containing the required information. The goal of the project was to automate the process using a Python script integrated with Selenium and Chromedriver.

## Script Overview

The Python script automates the following workflow:

1. Access the DVLA Website:

    - Selenium is invoked to open the appropriate UK Government (DVLA) website.

2. Extract Data from .csv:

    - The script retrieves the first row of data from a saved .csv file containing the Driver Licence Number, National Insurance Number, and Postcode.

3. Input Data:

    - The script enters the extracted information into the corresponding fields on the DVLA website.

4. Submission and Validation:

    - The script verifies the necessary fields and submits the information to log in.

    - If the login attempt fails due to incorrect information, the script records the failure and proceeds to the next row in the .csv file.

5. Extract Driver Points Information:

    - Once logged in successfully, the script extracts the driver’s points information and saves it to a .txt file.

6. Completion:

    - The script loops through all rows in the .csv file, completing the process for each driver. After completion, onboarding agents can review the results to identify drivers scheduled for onboarding that day.

## Outcomes and Benefits

This automation yielded several key benefits:

- Increased Efficiency:

    - Significantly reduced the time required for driver onboarding by eliminating repetitive manual tasks.

- Proactive Issue Resolution:

    - Enabled agents to identify and contact non-compliant drivers in advance, preventing wasted time and resources.

- Improved Onboarding Metrics:

    - Achieved a measurable decrease in onboarding time per driver and an increase in the total number of onboardings per day.

- Enhanced Driver Satisfaction:

    - Streamlined the onboarding process improved the overall driver experience.

This project exemplifies the impact of leveraging automation to solve operational inefficiencies and deliver tangible improvements to business processes and customer satisfaction.



