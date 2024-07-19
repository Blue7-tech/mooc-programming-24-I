# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    birthday = int(pic[:6])    
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    if year == 0 and pic[6] == "+":
        year = 1900
    elif year == 0 and pic[6] == "-":
        year = 1800
    elif year == 0 and pic[6] == "A":
        year = 2000
        
    try:
        datetime(year,month,day)
    except ValueError:
        return False

    if pic[6] != "-" and pic[6] != "+" and pic[6] !="A":
        return False
    
    for_ctrl_char = birthday*1000+int(pic[7:10])
    
    if pic[-1] == string[for_ctrl_char % 31]:
        return True
        
if __name__ == "__main__":
    print(is_it_valid("080842-720N"))