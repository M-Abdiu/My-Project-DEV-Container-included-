

    
#Math Stundenrechnung
def Math_Stundenrechnung(datapoints):
    #Get CSV Data
    from FileHandling  import read_csv_input
    csv_file = r"data\Stempelzeiten KW_XX.csv"
    datapoints=read_csv_input(csv_file)
    loopInt = 0
    
    while loopInt < len(datapoints):
        #Vars from CSV 
        EintrittsStempel = datapoints[4]
        AustrittsStempel = datapoints[7]
        EintrittsPause = datapoints[5]
        AustrittsPause = datapoints[6]
        Pensum = datapoints[2]
        
        #Vars used for Calc
        AnzahlArbeitsStunden  = AustrittsStempel - EintrittsStempel
        AnzahlPausenStunden = AustrittsPause - EintrittsPause
    
        EffektivArbeitsStunden = AnzahlArbeitsStunden - AnzahlPausenStunden
        loopInt = loopInt + 1

    return EffektivArbeitsStunden, AnzahlPausenStunden




#Check Vetragsbedingung
def Vertragsbedingungen(EffektivArbeitsStunden, AnzahlPausenStunden,Pensum):
    #MaxVars per Week 
    MaxStunden = 42.0
    MaxPausenAnzahl = 5.0    
        
    #Check Conditions of Vars
    if EffektivArbeitsStunden >MaxStunden * Pensum or AnzahlPausenStunden > MaxPausenAnzahl:
        Vertragsverletzung = True
        return Vertragsverletzung 
    else:
        Vertragsverletzung = False
        return Vertragsverletzung 

#Run
#Math_Stundenrechnung(datapoints) 
print(Math_Stundenrechnung())
    