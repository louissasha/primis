#! python3
# intake.py - Program to Open Intakes in Browser based on user input.

#TODO: Import tools

#TODO: Uses Sys.ARGV to determine what to do with user input

#TODO: Open browser to the correct intake

import webbrowser
import sys

mine = "http://sp.sunlifecorp.com/sites/BAnalytics/Lists/Intakes/My%20Intakes%20%20In%20Progress.aspx"
address = "http://sp.sunlifecorp.com/sites/BAnalytics/Lists/Intakes/DispForm.aspx?ID="
#search = http://sp.sunlifecorp.com/sites/BAnalytics/Lists/Intakes/Intakes%20%20All.aspx?View={72D25D70-BEF8-438B-8D6E-9725CE2C5865}&FilterField1=Assigned%5Fx0020%5FTo&FilterValue1=Haikel%20Nour
#search2 = http://sp.sunlifecorp.com/sites/BAnalytics/Lists/Intakes/Intakes%20%20All.aspx?View={72D25D70-BEF8-438B-8D6E-9725CE2C5865}&FilterField1=Assigned%5Fx0020%5FTo&FilterValue1=Haikel%20Nour&FilterField2=Status&FilterValue2=Closed

intake_number = sys.argv[1]

if len(sys.argv) < 1:
    print("""         How to use this file example:          
            intake <number>    = opens the page of that specific intake number
            intake mine <name> = opens the page related to that name, if no name selected it will open the users page
    """)
    sys.exit(0)

if len(sys.argv) == 2:
    if sys.argv[1] == "mine":
        print("Opening your intake page")
        webbrowser.open(mine)
        sys.exit(0)
    if sys.argv[1].isdecimal():
        print("Opening the page for intake: "+ str(sys.argv[1])) 
        webbrowser.open(address+str(sys.argv[1]))
        sys.exit(0)
    else:
        print("""Second argument has to be 'mine' if you want to open ur page
                 Second argument has to be 'mine'+ <firstname> if you want to open <firstname>'s page
                 Second argument has to be a number if you want to open that specific intake page
        """)
        sys.exit(0)

if len(sys.argv) > 3:
    print("""         How to use this file example:          
            intake <number>    = opens the page of that specific intake number
            intake mine <name> = opens the page related to that name, if no name selected it will open the users page
    """)
    sys.exit(0)



    #  Get intake number from the address line
    #  address = ''.join(sys.argv[1])



