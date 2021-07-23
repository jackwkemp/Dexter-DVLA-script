# DVLA Driver Points Script

An example of a piece of work I completed at my previous employer.

Aim:
To improve driver onboarding efficiency by automating a repetitive process

Context:
For a driver to be onboarded onto my previous employer’s platform, one of the onboarding agents had to manually check to see if the driver had not committed any serious offences e.g drink driving or driving without insurance.

The process required three pieces of key information:
Driver Licence Number
National Insurance Number
Postcode

After obtaining driver permission to check their points for them, we could internally query our system to pull a .csv of the above information.

The Python script is designed to run with Selenium and Chromedriver. 

Script flow:
- Selenium is called and opens the appropriate DVLA website (UK Government website)
- The script pulls the first row from the saved .csv (containing Driver Licence, National Insurance, Postcode)
- The script sends the information to the associated fields on the DVLA Website
- The script confirms the necessary fields and requests to log in
- (If there is a failure due to incorrect information, the script notes this and moves on to the next row)
- Once logged in, the script copies the driver’s points information and saves this information to a .txt file
- Once the script has looped through the list it ends and the onboarding agents can then compare the results against which drivers are booked in for onboarding that day

Another benefit that came out of this project was that agents could proactively call drivers that were not compliant, preventing them from coming in
There was a decrease in overall driver onboarding time, a increase on the total number of onboards per day and an increase in driver satisfaction from their onboarding experience



