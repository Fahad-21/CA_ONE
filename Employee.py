#Create a class Employee
class Employee:
    #Craeating constructor with attributes staffId,lastName,firstName,reghours,hourlyRate,otMultiple,taxCredit,standardBand
    def __init__(self, staffId, lastName, firstName, regHours, hourlyRate, otMultiple, taxCredit, standardBand) -> None:
        self.staffId = staffId
        self.lastName = lastName
        self.firstName = firstName
        self.regHours = regHours
        self.hourlyRate = hourlyRate
        self.otMultiple = otMultiple
        self.taxCredit = taxCredit
        self.standardBand = standardBand

        self.standard_rate = 0.2
        self.higher_rate = 0.4
