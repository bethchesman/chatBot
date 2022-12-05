from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import webbrowser

def run():
    
    url = "https://maps.googleapis.com/maps/api/staticmap?center=49.941140,-119.396210&zoom=16&size=400x400&markers=size:mid%7Ccolor:red%7C49.941140,-119.396210&key=AIzaSyBTJXT29wkFppv-tZpncXfnESgXj28xpWE"
    
    
    user_input = ""
    print("Hi! Welcome to the Appointment Booking Feature. To return to the home at any time type ""exit"".")
    print("To book an academic advising appointment please follow the link provided below and a map will be provided to the academic advising offices.")
    print("https://students.ok.ubc.ca/academic-success/advising-options/academic-advising/contact/")
    
    webbrowser.open(url, new=2)
    
    while user_input != "exit":
        user_input = str(input())
        if user_input == "exit":
            print("Exiting Appointment Booking")
            return
        else: 
            print("Your input is not recognised. To exit this feature please type exit")
            
            
run()