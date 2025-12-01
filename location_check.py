class LocationCheck:

    def __init__(self, location):
        if location[0:3] == "AUS":
            self.oss = "OSS-APAC-ANZ"
        elif location[0:3] == "CHN":
            self.oss = "China HW/SW Fulfillers"
        elif location[0:3] == "IND":
            self.oss = "OSS-APAC-India"
        elif location[0:3] == "JPN":
            self.oss = "OSS-APAC-Japan"
        elif location[0:3] == "KOR":
            self.oss = "OSS-APAC-Korea"
        elif location[0:3] == "MYS":
            self.oss = "OSS-APAC-Malaysia"
        elif location[0:3] == "SGP":
            self.oss = "OSS-APAC-Singapore"
        elif location[0:3] == "THA":
            self.oss = "OSS-APAC-Thailand"
        elif location[0:3] == "AUT":
            self.oss = "OSS-EU-DACH"
        elif location[0:3] == "BEL":
            self.oss = "OSS-EU-FraBeNe"
        elif location[0:3] == "DNK":
            self.oss = "OSS-EU-Nordics"
        elif location[0:3] == "FIN":
            self.oss = "OSS-EU-Nordics"
        elif location[0:3] == "FRA":
            self.oss = "OSS-EU-FraBeNe"
        elif location[0:3] == "GRC":
            self.oss = "OSS-EU-Iberia-Italy"
        elif location == "DEU - Hamburg":
            self.oss = "OSS-EU-DACH"
        elif location == "DEU - Field":
            self.oss = "OSS-EU-DACH"
        elif location == "DEU - Marl":
            self.oss = "OSS-EU-DACH"
        elif location == "DEU - Munich":
            self.oss = "OSS-EU-DACH"
        elif location == "DEU - Tuttlingen / Ortho":
            self.oss = "OSS-EU-Manufacturing"
        elif location == "DEU - Tuttlingen / Service Center":
            self.oss = "OSS-EU-Manufacturing"
        elif location[0:3] == "ITA":
            self.oss = "OSS-EU-Iberia-Italy"
        elif location[0:3] == "NZL":
            self.oss = "OSS-EU-FraBeNe"
        elif location[0:3] == "NOR":
            self.oss = "OSS-EU-Nordics"
        elif location[0:3] == "POL":
            self.oss = "OSS-EU-Poland"
        elif location[0:3] == "ESP":
            self.oss = "OSS-EU-Iberia-Italy"
        elif location[0:3] == "PRT":
            self.oss = "OSS-EU-Iberia-Italy"
        elif location[0:3] == "SWE":
            self.oss = "OSS-EU-Nordics"
        elif location[0:3] == "CHE":
            self.oss = "OSS-EU-DACH"
        elif location == "CHE - Aarau/Site1":
            self.oss = "OSS-EU-Manufacturing"
        elif location == "CHE - Aarau/Site2":
            self.oss = "OSS-EU-Manufacturing"
        elif location[0:3] == "RUS":
            self.oss = "OSS-MEA-Russia"
        elif location[0:3] == "SAU":
            self.oss = "OSS-MEA-UAE"
        elif location[0:3] == "UAE":
            self.oss = "OSS-MEA-UAE"
        elif location[0:3] == "ZAF":
            self.oss = "OSS-MEA-South Africa"
        elif location[0:3] == "TUR":
            self.oss = "OSS-MEA-Turkey"
        elif location[0:3] == "BRA":
            self.oss = "OSS-LA-Brazil"
        elif location[0:3] == "MEX":
            self.oss = "OSS-LA-Mexico"
        elif location[0:2] == "PR":
            self.oss = "OSS-LA-Puerto Rico"
        elif location[0:3] == "COL":
            self.oss = "OSS-LA-Colombia"
        elif location[0:3] == "CRI":
            self.oss = "OSS-LA-Costa Rica"
        elif location[0:9] == "UK - Hull":
            self.oss = "OSS-UK-Hull"
        elif location == "UK - Godmanchester":
            self.oss = "OSS-UK-Godmanchester"
        elif location[0:12] == "UK - Warwick":
            self.oss = "OSS-UK-Godmanchester"
        elif location == "UK - Aurora LSpa":
            self.oss = "OSS-UK-Godmanchester"
        elif location == "UK - Croxley":
            self.oss = "OSS-UK-Croxley Green"
        elif location == "UK - Watford":
            self.oss = "OSS-UK-Croxley Green"
        elif location == "UK - Field":
            self.oss = "OSS-UK-Croxley Green"
        elif location[0:3] == "IRL":
            self.oss = "OSS-UK-Croxley Green"
        elif location[0:2] == "US":
            self.oss = "US/UK HW/SW Sourcing"
        elif location[0:3] == "CAN":
            self.oss = "OSS-NA-Mississauga"
        else:
            self.oss = "OSS not found!"
