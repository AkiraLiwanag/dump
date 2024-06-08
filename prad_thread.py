import threading
import random
import time
import datetime

def random_function():
    ct = datetime.datetime.now()
    print(ct)
    code = ["Code Red", "Code Blue", "Code Green", "Code Orange", "Code Yellow", "Code Black", "Code White", "Code Purple", "Code Pink"]
    cod = random.sample(code, 1)
    urgency = ["Critical", "High", "Medium", "Low", "Lowest"]
    urge = random.sample(urgency, 1)
    polis = ["3511 A vehicle that has been impounded for a mandatory 30 days", "A.P.S. Arizona Public Service", "A.S.A.P. As soon as possible", "A.T.F. Bureau of Alcohol, Tobacco, and Firearms", "BAILED OUT Subject jumped out of car and ran", "BYFRND Boyfriend", "BEER RUN Shoplifting beer", "BONDOUT Prisoner who is going to post bail and be released", "BEEN MADE/BURNED Undercover officer's ID is known", "BHND Behind", "BIKE Motorcycle", "BIKERS Motorcycle riders", "BOOKING Booking prisoner into jail", "BREAKING UP Radio transmissions are not being received clearly", "BUSTED Arrested", "C.C.W. Carrying concealed weapon", "C.O. Civilian observer", "COMP Complainant", "C.L.D. Citation in lieu of detention", "CRACK, ROCK Smokeable form of cocaine", "D.E.B. Drug Enforcement Bureau", "DIX Detectives", "D.O.A. Dead on arrival", "D.O.B. Date of birth", "D.O.C. Department of Corrections", "D.P.S. Department of Public Safety", "DRIVE BY Shots fired from a moving vehicle", "E.O.C. Emergency Operations Center", "EQUIPMENT Police vehicle", "E.R. Emergency Room", "E.T.A. Estimated time of arrival", "F.A.A. Federal Aviation Administration", "B.I. Federal Bureau of Investigation", "F.I. Field Interrogation (Form 36 card)", "FILE STOP Notation put in police record; File Stops are confirmed by R&I Bureau", "FLIR Device used by aircraft to check for heat sources", "F.O.J. From other jurisdiction", "FRONT DESK Information Desk at main station", "FUGITIVE A wanted person", "GAS WASH/WASHDOWN Fire Department needed to wash gas down", "G.C.I. /B.A. Test used to determine blood alcohol content", "G.I.B. General Investigations Bureau", "GOT THE EYE In view (on a code 5)", "GRN Green", "HOND Honda", "HIT Subject or item wanted", "H.G.N. Horizontal Gaze Nystagmus (a test for detecting drug / alcohol use)", "HOBBLES Nylon rope used for legs and hand restraint", "HOOK Wrecker", "HSE House", "ICE, CRYSTAL Smokeable methamphetamine", "J.C.C. Juvenile Corrections Center", "J.P. Justice of the Peace", "JUMPED ON Assaulted", "JUMPER Person attempting suicide by jumping", "LADDER Fire Department ladder truck", "MARQUIS Test for narcotics", "M.D.C. Mobile Digital Computer (Police car computer)", "MEDICS Paramedics", "MERZ Mercedes Benz", "MHP Mobile Home Park", "MOTOR Solo motor unit", "NUMBER 1 SITUATION Probable cause for arrest", "NUMBER 9's Citations", "OD Overdose", "ONE FROM LIST Contract wrecker (926)", "ONE ON ONE Suspect / witness I.D.", "ONE ROLL Fingerprints", "O.V. On view, officer just witnessed an incident", "PAGE 2 Additional charges filed on a subject already in custody", "P.C. Probable cause", "PLE Purple", "P.O. Probation officer", "RESTRAINTS Leather straps used to restrain prisoners", "RINGER Audible alarm", "ROLLOVER Accident involving overturned vehicle", "R.P. Responsible party", "S/E/C Southeast corner", "SEIZURE Impound a vehicle; subject having convulsions", "SGT Sergeant", "SILENT Silent alarm", "SLIM JIM Device used to open locked vehicle", "SMASH & GRAB Broke out window, grabbed items and ran", "S.O./M.C.S.O. Maricopa County Sheriff's Office", "S.R.P. Salt River Project", "STRIPPED Vehicle stripped", "TECH Radio or computer technician", "THIRTY-SIX Field interrogation (or form 36)", "THREE WHEELER Police 3-wheeled motorcycle", "TILL TAP Grab money from register", "DISPATCH AN ANIMAL To shoot an animal", "TRAFFIC BOX KEY Key used to open traffic signal control box", "XHUSB Ex-husband", "WAGON/WAGON Police paddy wagon"]
    pol = random.sample(polis, random.randint(1, 8))
    locate = ["Local", "Local", "Foreign"]
    loc = random.sample(locate, 1)
    direction = ["South", "North", "West", "East", "Southwest", "Southeast", "Northwest", "Northeast"]
    dire = random.sample(direction, 1)
    suspectcode = (round(random.random()*26))
    sus = "Suspect Code:"
    location = (round(random.random()*99999999,10))
    po = "police:"
    print(po, cod, urge, sus, suspectcode, pol, loc, dire, location)
    print()

def call_random_function():
    while True:
        time.sleep(random.randint(1, 360))
        random_function()

if __name__ == '__main__':
    threading.Thread(target=call_random_function).start()

