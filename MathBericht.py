#Get CSV Data

#Math Stundenrechnung
def Math_Stundenrechnung():
    #Vars
    EintrittsStempel = 8.00
    AustrittsStempel = 18.00
    EintrittsPause = 12.00
    AustrittsPause = 13.00
    AnzahlArbeitsStunden = 0.0
    AnzahlPausenStunden = 0.0
    EffektivArbeitsStunden = 0.0
    
    #VarChanges
    AnzahlArbeitsStunden  = AustrittsStempel - EintrittsStempel
    AnzahlPausenStunden = AustrittsPause - EintrittsPause
    EffektivArbeitsStunden = AnzahlArbeitsStunden - AnzahlPausenStunden

    return EffektivArbeitsStunden, AnzahlPausenStunden
    

#Check Vetragsbedingung
def Vertragsbedingungen(EffektivArbeitsStunden, AnzahlPausenStunden):
    #Vars
    Pensum = 1.0
    MaxStunden = 42.0
    MaxPausenAnzahl = 5.0
    Vertragsverletzung = False
    EffektivArbeitsStunden
    AnzahlPausenStunden
    
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


    