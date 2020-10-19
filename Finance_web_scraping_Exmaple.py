
import requests
from sys import exit


class Finance:
    indicat = [ 'Bid', 'Open', 'Ask', 'Volume','All','Exit' ]
    url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

    def __init__(self):
        self.ShowScreen(1)
        param = input("\nSelect value from the list above: ")
        if(param.capitalize() == 'All' or int (param) == 4):
            self.getAllParams()
        else:
            self.getParamValue(param)
        print("\nBye..")
        exit(0)
        

    def getParamValue(self,param):
        inputType = True if param.isalpha() else False
        if inputType:
            param = param.capitalize()
            if param in self.indicat:
                pass
            else:
                print("you enter Wrong value, Please try again")
                exit(1)
        else:
            param = int(param)
            if param < len(self.indicat):
                if(param == len(self.indicat)-1):
                    print("\nBye...")
                    exit(0)
                else:
                    param = self.indicat[param]
            else:
                print("you enter Wrong value, Please try again")
                exit(2)
        try:
            response = requests.get(self.url)
            htmltext = response.text
            splitlist = htmltext.split(param)
            result = splitlist[1].split("\">")[2].split("<")[0]
        except:
            result = "Error...We will fix it soon"
            exit(3)
        print(f"\n{Colors.OKGREEN}Result: {result}{Colors.OKGREEN}")
        
    
    def getAllParams(self):
        for i in range((len(self.indicat)-2)):
            self.getParamValue(self.indicat[i])
        
    def ShowScreen(self, showMeThis):
        if showMeThis == 1: # welcome Screen
            print(f"\n{Colors.HEADER}Welcom to Apple Inc.(AAPL) Finance\n{Colors.HEADER}")
            for i in self.indicat:
                print(f" [*]\t{i}")


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


##############
Finance()

