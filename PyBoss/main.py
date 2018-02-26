"""
Created on Thu Feb 22 09:34:38 2018

@author: Debbie Chan

A new HR system requires employee records be stored completely differently.

Task: 
    bridge the gap by creating a Python script able to convert employee records to the required format.
    Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records.
    
    Old format: 
    Emp ID,Name,DOB,SSN,State
    214,Sarah Simpson,1985-12-04,282-01-8166,Florida
    
    New format:
    Emp ID,First Name,Last Name,DOB,SSN,State
    214,Sarah,Simpson,12/04/1985,***-**-8166,FL
    
    Summary of required conversions: 
    The Name column should be split into separate First Name and Last Name columns.
    The DOB data should be re-written into DD/MM/YYYY format.
    The SSN data should be re-written such that the first five numbers are hidden from view.
    The State data should be re-written as simple two-letter abbreviations.
"""

# Import modules
import os 
import csv

# Open csv files for reading current employee records and open another csv file to write employee data in the required format.
csvpath = os.path.join('raw_data', 'employee_data2.csv')
newempcsv = os.path.join('raw_data', 'new_employee_data.csv')

# Python dictionay for state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Set empty list variables
empid = []
firstName = []
lastName = []
dob = []
ssn = []
state = []

# Open employee data csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip header
    next(csvreader, None)
        
    # Read through current employee record from csv file and format as required.
    for row in csvreader:
        empid.append(row[0])
        name = row[1]
        fname, lname = name.split(" ")
        firstName.append(fname)
        lastName.append(lname)
        dobYear, dobMonth, dobDD = row[2].split("-")
        dob.append(dobDD + "/" + dobMonth+ "/" + dobYear)
        ssn.append( "***-**-" + row[3][7:11])
        state.append(us_state_abbrev.get(row[4]))
        
# zip lists together
cleanCSV = zip(empid, firstName, lastName, dob, ssn, state)

# Open new csv file to write newly formatted employee record
with open(newempcsv, 'w', newline="") as csvfile:
    
    csvWriter = csv.writer(csvfile, delimiter=',')
    
    # Write Headers into file
    csvWriter.writerow(["empid", "firstName", "lastName", "dob", "ssn", "state"])
     
    # Write the zipped lists to a csv
    csvWriter.writerows(cleanCSV)