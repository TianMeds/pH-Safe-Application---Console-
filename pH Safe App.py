from string import capwords
from rich.console import Console
from rich.theme import Theme
from rich.progress import track
import time

 # Path: pH Safe App.py
custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)
class Color:
    
    def __init__(self, color, level, trivia):
        self.color = color
        self.level = level
        self.trivia = trivia

RED = ("means the water is at 1 pH level" + "\n"  "Did you know? Battery acid, and hydrochloric acid has pH levels of below 1, then its not safe to drink")

LIGHT_RED = ("means the water is at  1 - 1.5 pH level" + "\n" 
"Did you know? Lemon Juice, and vinegar has pH levels of 2. So if the tested liquid is a lemon juice, then it is safe to drink")

ORANGE = ("means the water is at 2.5 pH level" + "\n" "Did you know? Soda, and Tomato juice is at 2.5 - 3.5 pH level So if the tested liquid is Soda or Tomato juice, then it is safe to drink")

LIGHT_ORANGE = ("means the water is at  3.3 - 4.2 pH level" + "\n" "Did you know? Black coffee has a pH level of 5. So if the tested liquid is Black Coffee, then it is safe to drink")

YELLOW = ("means the water is at 5 - 5.03 pH level" + "\n"  "Did you know? Milk has a pH level of 6.3 - 6.6. So if the tested liquid is Milk, then it is safe to drink")

LIGHT_GREEN = ("means the water is at 6.5 - 6.8 pH level" + "\n"  "Did you know? Urine is at 6.6 pH level. So if the tested liquid is Urine, then it is not safe to drink")

GREEN = ("means the water is at 7 pH level" + "\n" "Did you know? Saliva is at 6.3 - 6.6 pH level. So if the tested liquid is Saliva, then it is not safe to drink unless it is yours")

BLUE_GREEN = ("means the water is at 7.5 - 8.4 pH level" + "\n"  "Did you know? Blood is at 7.4 pH level. So if the tested liquid is Blood, then it is not safe to drink")

BLUE = ("means the water is at 11.0 - 11.5 pH level" + "\n"  "Did you know? Ammonia solution is at 10.5 - 11.5 pH level. So if the tested liquid is Ammonia solution, then it is not safe to drink")

PURPLE = ("means the water is at 12.5 pH level" "\n" "Did you know? Ammonia solution is at 10.5 - 11.5 pH level. Bleaches has a pH level of 13.5. So if the tested liquid are these, then it is not safe to drink")

VIOLET = ("means the water is  at 13.0 - 14.0 pH level" "\n" "Did you know? Liquid drain cleaner is at 14 pH level. So if the tested liquid is a Liquid drain cleaner, then it is not safe to drink")


START_DIALOG = ("Hi! Welcome to pH Safe App! We Make sure your water is clean")
END_DIALOG = ("""\nThank you for using pH Safe App!
To make sure the water you are about to drink is safe, buy test approved drinking water :>\n 
This app is just a demo, full specifications are upto the future Mc Joseph C. Agbanlog, and Christian Medallada 
(Beginner Developers of pH Safe App v3)\n """)
ADD_DIALOG = ("""Additional Information!
Only water at 6 - 8.5 pH level is safe to drink
Below 7 pH level is acidic and above is alkaline""")

def start():
    
    Name = input("Enter your Name: ")
    
    for p in track(range(4), description="Proccessing..."):
        print(f"Logging In {p}")
        time.sleep(0.7)
        
    console.print("\nSuccessfully Logged In! to pH Safe App", style="success")
    
    console.print("\nMain Menu", style="bold")
    
    console.print("\n" + "Welcome " + Name + " lets purify your water!" + "\n", style="bold italic cyan")

def main():
    
    MainMenu = ["(0) Scan Driking water", "(1) Learn More", "(2) About App", "(3) Buy us a cup of coffee", "(4) Exit App"]
    
    console.print("\nDashboard\n" , style="bold")
    
    for m in MainMenu:
         print(m)
    UserInput = input("\n" + "Please enter the Number you need: ")
    menu(UserInput)
         
def menu(UserInput):
    
    LearnMore = ["(0) What is pH Level", "(1) What is pH Test Strip", "(2) Importance of pH level on drinking water", "(3) Go back to Home"]
                
    if UserInput == "0":
        userChar = input("""\nHave you tested the drinking water using a pH test strip?
        (Y) Yes or (N) No: """)
        userChar = capwords(userChar)
        if userChar == 'Y':
            print("\n" + "Make sure the liquid you tested is water" + "\n")
            print("""What color appeared in the pH strip after you tested the water?
            """)
            
            Colors = ["(1) Red","(2) Light Red", "(3) Orange", "(4) Light Orange", "(5) Yellow", "(6) Light Green", "(7) Green","(8) Blue Green", "(9) Purple","(10) Violet" ]
                
            for c in Colors:
                print(c)
            testcolors = input("\nPlease enter the Corresponding Color: ")
            
            if testcolors == "1":
              print("\n" , (Colors[0]), RED, "\n")
              print(ADD_DIALOG + "\n")
              GoBack()
              
            elif testcolors == "2":
              print("\n" , (Colors[1]), LIGHT_RED, "\n")
              print(ADD_DIALOG + "\n")
              GoBack()
              
            elif testcolors == "3":
                print("\n", (Colors[2]), ORANGE, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
                
            elif testcolors == "4":
                print("\n", (Colors[3]), LIGHT_ORANGE,  "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
                
            elif testcolors == "5":
                print("\n", (Colors[4]), YELLOW, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
                
            elif testcolors == "6":
                print("\n", (Colors[5]), LIGHT_GREEN, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
            
            elif testcolors == "7":
                print("\n", (Colors[6]), GREEN, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
                
            elif testcolors == "8":
                print("\n", (Colors[7]), BLUE_GREEN, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
                
            elif testcolors == "9":
                print("\n", (Colors[8]), PURPLE, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
                
            elif testcolors == "10":
                print("\n", (Colors[9]), VIOLET, "\n")
                print(ADD_DIALOG + "\n")
                GoBack()
            
            else:
                console.print("Please try again!", style="error")
                print("\n")
                menu(UserInput)
            
        elif userChar == 'N':
            main() 
        else: 
            console.print("Please try again!", style="error")
            menu(UserInput)
        
    elif UserInput == "1":
        print("""\nLearn More: 
""")
        for l in LearnMore:
            print(l)
        learn = input("\nEnter a valid option: ")
        
        if learn == "0":
            print("\nThe pH of water is an indicator of how acidic or basic it is.\nThe pH scale runs from 0 to 14, with 7 being the neutral value.\nAcidity is indicated by a pH less than 7, "
			+ "while a pH greater than 7\nindicates a base. In addition, pH is a measurement of the proportion\nof free hydrogen and hydroxyl ions in water." + "\n")
            GoBack()
        elif learn == "1":
            print("\nA pH test strip is a good way to measure the pH of a liquid or substance."
            + "\nThe material in the paper causes the paper to change colour\nat different levels of acidity - for example, from neutral to highly-acid to extremely-acidic.\n")
            GoBack()
            
        elif learn == "2":
            print("\nThe importance of pH level to drinking water is that high-acid diet causes weight gain,\na slowed immune response, and illness vulnerability."
                  + "\nAn alkaline diet causes difficulty metabolizing critical nutrients. Most commercially available uncontaminated\nbottled water will not make you healthy or sick. "
                  "Just because water is slightly more alkaline doesn't mean it's better for your health. \n ")
            GoBack()
            
        elif learn == "3":
            main()
            

    elif UserInput == "2":
        print("""\npH Safe App is an app that will scan for the pH test Strip and determine the pH Level of the tested liquid. 
This app focuses on the SDG focus Number 6 which is Clean Water and Sanitation. 
For the mean time, the app can only be ran through Console. """ + "\n")
        GoBack()
            
    elif UserInput == "3":
        print("""\nMaking this demo app is pretty hard you know If you are a good person, kindly donate to the Programmers via Gcash
    McJoseph Agbanlog: 0936 977 7935, 
    Christian Medallada: 0995 161 7400 """ + "\n")
        GoBack()
    
    elif UserInput == "4":
        print(END_DIALOG)
        
    else:
        console.print("Please try again!", style="error")
        main()
        
def GoBack():
    
    RedirectMenu = ["(0) Go Back to Menu", "(1) Exit App"]
    
    
    for x in RedirectMenu:
        print(x)
    ReturnInMenu = input("\n" + "Enter your choice:")
    if ReturnInMenu == "0":
        main()
    elif ReturnInMenu == "1":
        print("\n" + END_DIALOG)
        exit()
    else:
        console.print("Please try again!", style="error")
        GoBack()
            
if __name__ == "__main__":
    
    console.print("\n" + START_DIALOG + "\n",style="bold italic blue", justify="center")
    start()
    main()


