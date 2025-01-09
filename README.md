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

## Features:
- **Automated Driver Onboarding**: Automates the process of verifying driver compliance.
- **Steps**:
  1. Extract data from a .csv file (Driver Licence Number, National Insurance Number, Postcode).
  2. Input data into the DVLA website.
  3. Retrieve points information and save to a .txt file.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install selenium`.
3. Ensure `chromedriver` is available.
4. Run the script: `python dexter_beta.py`.

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

[![How to Use the Script](https://img.youtube.com/vi/jyKTnHhHsAo/0.jpg)](https://www.youtube.com/watch?v=jyKTnHhHsAo)


