import json



def compatibility(json_data):
    variable = json.loads(json_data)
    team = variable["team"] #list of team members and their attributes
    applicants = variable["applicants"] #list of applicants and their attributes

    avgIntelligence = 0
    avgStrength = 0
    avgEndurance = 0
    avgSpice = 0

    for person in team:
        avgIntelligence += person["attributes"]["intelligence"]
        avgStrength += person["attributes"]["strength"]
        avgEndurance += person["attributes"]["endurance"]
        avgSpice += person["attributes"]["spicyFoodTolerance"]

    #average team score for each category  
    avgIntelligence /= len(team)
    avgStrength /= len(team)
    avgEndurance /= len(team)
    avgSpice /= len(team)

    applicantScores = []


    for person in applicants:
        dict = {}
        dict["name"] = person["name"]


        
        intelligenceCompatibility = 0
        strengthCompatibility = 0
        enduracneCompatibility = 0
        spiceCompatibility = 0
        

        #we score the applicant's compatibility for each category separately

        if(person["attributes"]["intelligence"] > avgIntelligence):
            diff = person["attributes"]["intelligence"] - avgIntelligence
            intelligenceCompatibility = (diff * 0.21097) / (1 + 0.1 * diff)

        if(person["attributes"]["strength"] > avgStrength):
            diff = person["attributes"]["strength"] - avgStrength
            strengthCompatibility = (diff * 0.21097) / (1 + 0.1 * diff)

        if(person["attributes"]["endurance"] > avgEndurance):
            diff = person["attributes"]["endurance"] - avgEndurance
            enduranceCompatibility = (diff * 0.21097) / (1 + 0.1 * diff)
            
        if(person["attributes"]["spicyFoodTolerance"] > avgSpice):
            diff = person["attributes"]["spicyFoodTolerance"] - avgSpice
            spiceCompatibility = (diff * 0.21097) / (1 + 0.1 * diff)

        totalCompatibility = (2*intelligenceCompatibility +strengthCompatibility + enduranceCompatibility + spiceCompatibility)/5 #intelligence is weighted more than other categories

        
        dict["score"] = totalCompatibility
        applicantScores.append(dict)

    return json.dumps({"scoredApplicants": applicantScores})





















    
