class LocationCheck:

    def __init__(self, location):
        if location[0:3] == "AUS":
            self.oss = "SNI-OSS-APAC-ANZ"
        elif location[0:3] == "CHN":
            self.oss = "China HW/SW Fulfillers"
        elif location[0:3] == "IND":
            self.oss = "SNI-OSS-APAC-India"
        elif location[0:3] == "JPN":
            self.oss = "SNI-OSS-APAC-Japan"
        elif location[0:3] == "KOR":
            self.oss = "SNI-OSS-APAC-Korea"
        elif location[0:3] == "MYS":
            self.oss = "SNI-OSS-APAC-Malaysia"
        elif location[0:3] == "SGP":
            self.oss = "SNI-OSS-APAC-Singapore"
        elif location[0:3] == "THA":
            self.oss = "SNI-OSS-APAC-Thailand"
        elif location[0:3] == "AUT":
            self.oss = "SNI-OSS-EU-DACH"
        elif location[0:3] == "BEL":
            self.oss = "SNI-OSS-EU-FraBeNe"
        elif location[0:3] == "DNK":
            self.oss = "SNI-OSS-EU-Nordics"
        elif location[0:3] == "FIN":
            self.oss = "SNI-OSS-EU-Nordics"
        elif location[0:3] == "FRA":
            self.oss = "SNI-OSS-EU-FraBeNe"
        elif location[0:3] == "GRC":
            self.oss = "SNI-OSS-EU-Iberia-Italy"
        elif location == "DEU - Hamburg":
            self.oss = "SNI-OSS-EU-DACH"
        elif location == "DEU - Field":
            self.oss = "SNI-OSS-EU-DACH"
        elif location == "DEU - Marl":
            self.oss = "SNI-OSS-EU-DACH"
        elif location == "DEU - Munich":
            self.oss = "SNI-OSS-EU-DACH"
        elif location == "DEU - Tuttlingen / Ortho":
            self.oss = "SNI-OSS-EU-Manufacturing"
        elif location == "DEU - Tuttlingen / Service Center":
            self.oss = "SNI-OSS-EU-Manufacturing"
        elif location[0:3] == "ITA":
            self.oss = "SNI-OSS-EU-Iberia-Italy"
        elif location[0:3] == "NZL":
            self.oss = "SNI-OSS-EU-FraBeNe"
        elif location[0:3] == "NOR":
            self.oss = "SNI-OSS-EU-Nordics"
        elif location[0:3] == "POL":
            self.oss = "SNI-OSS-EU-Poland"
        elif location[0:3] == "ESP":
            self.oss = "SNI-OSS-EU-Iberia-Italy"
        elif location[0:3] == "PRT":
            self.oss = "SNI-OSS-EU-Iberia-Italy"
        elif location[0:3] == "SWE":
            self.oss = "SNI-OSS-EU-Nordics"
        elif location[0:3] == "CHE":
            self.oss = "SNI-OSS-EU-DACH"
        elif location == "CHE - Aarau/Site1":
            self.oss = "SNI-OSS-EU-Manufacturing"
        elif location == "CHE - Aarau/Site2":
            self.oss = "SNI-OSS-EU-Manufacturing"
        elif location[0:3] == "RUS":
            self.oss = "SNI-OSS-MEA-Russia"
        elif location[0:3] == "SAU":
            self.oss = "SNI-OSS-MEA-UAE"
        elif location[0:3] == "UAE":
            self.oss = "SNI-OSS-MEA-UAE"
        elif location[0:3] == "ZAF":
            self.oss = "SNI-OSS-MEA-South Africa"
        elif location[0:3] == "TUR":
            self.oss = "SNI-OSS-MEA-Turkey"
        elif location[0:3] == "BRA":
            self.oss = "SNI-OSS-LA-Brazil"
        elif location[0:3] == "MEX":
            self.oss = "SNI-OSS-LA-Mexico"
        elif location[0:2] == "PR":
            self.oss = "SNI-OSS-LA-Puerto Rico"
        elif location[0:3] == "COL":
            self.oss = "SNI-OSS-LA-Colombia"
        elif location[0:3] == "CRI":
            self.oss = "SNI-OSS-LA-Costa Rica"
        elif location[0:9] == "UK - Hull":
            self.oss = "SNI-OSS-UK-Hull"
        elif location == "UK - Godmanchester":
            self.oss = "SNI-OSS-UK-Godmanchester"
        elif location[0:12] == "UK - Warwick":
            self.oss = "SNI-OSS-UK-Godmanchester"
        elif location == "UK - Aurora LSpa":
            self.oss = "SNI-OSS-UK-Godmanchester"
        elif location == "UK - Croxley":
            self.oss = "SNI-OSS-UK-Croxley Green"
        elif location == "UK - Watford":
            self.oss = "SNI-OSS-UK-Croxley Green"
        elif location == "UK - Field":
            self.oss = "SNI-OSS-UK-Croxley Green"
        elif location[0:3] == "IRL":
            self.oss = "SNI-OSS-UK-Croxley Green"
        elif location[0:2] == "US":
            self.oss = "US/UK HW/SW Sourcing"
        elif location[0:3] == "CAN":
            self.oss = "SNI-OSS-NA-Mississauga"
        else:
            self.oss = "OSS not found!"
