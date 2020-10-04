import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv

fields = ["Timestamp" , "Question"]

# Fetch the service account key JSON file contents
cred = credentials.Certificate('e-week-firebase-adminsdk-uvnma-2d671aae5c.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://e-week.firebaseio.com/'
})

ref = db.reference('Questions')

filename = "questions.csv"
    
    # writing to csv file  
with open(filename, 'w') as csvfile:
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    # writing the fields  
    csvwriter.writerow(fields)  


for i,j in ref.get().items():
    try:
        rows = [i, j]
        with open(filename, "a") as csvfile:
            csvwriter = csv.writer(csvfile)  
            csvwriter.writerows(rows) 
    except:
        pass
    
    print(i, j)
