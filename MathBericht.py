#Get CSV Data

#Math Stundenrechnung
def Math_Stundenrechnung():
    #Vars from CSV //Placeholders
    EintrittsStempel = 8.00
    AustrittsStempel = 18.00
    EintrittsPause = 12.00
    AustrittsPause = 13.00
    
    #Vars used for Calc
    AnzahlArbeitsStunden  = AustrittsStempel - EintrittsStempel
    AnzahlPausenStunden = AustrittsPause - EintrittsPause
    
    EffektivArbeitsStunden = AnzahlArbeitsStunden - AnzahlPausenStunden

    return EffektivArbeitsStunden, AnzahlPausenStunden
    

#Check Vetragsbedingung
def Vertragsbedingungen(EffektivArbeitsStunden, AnzahlPausenStunden):
    #MaxVars per Week // change to daily
    MaxStunden = 42.0
    MaxPausenAnzahl = 5.0    
    
    # Var from CSV
    Pensum = 1.0
    
    #Check Conditions of Vars
    if EffektivArbeitsStunden >MaxStunden * Pensum or AnzahlPausenStunden > MaxPausenAnzahl:
        Vertragsverletzung = True
        return Vertragsverletzung 
    else:
        Vertragsverletzung = False
        return Vertragsverletzung 

#Run
EffektivArbeitsStunden, AnzahlPausenStunden = Math_Stundenrechnung()
print(AnzahlPausenStunden)
print(EffektivArbeitsStunden)
Vertragsverletzung = Vertragsbedingungen(EffektivArbeitsStunden, AnzahlPausenStunden )
print(Vertragsverletzung)


    