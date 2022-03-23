import json



def compatibility(variable):
    #variable = json.loads(json_data)
    team = variable["team"]
    applicants = variable["applicants"]

    avgIntelligence = 0
    avgStrength = 0
    avgEndurance = 0
    avgSpice = 0

    for person in team:
        avgIntelligence += person["attributes"]["intelligence"]
        avgStrength += person["attributes"]["strength"]
        avgEndurance += person["attributes"]["endurance"]
        avgSpice += person["attributes"]["spicyFoodTolerance"]

    
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

        totalCompatibility = (2*intelligenceCompatibility +strengthCompatibility +enduracneCompatibility + spiceCompatibility)/5 #intelligence is weighted more than other categories

        

        
        dict["score"] = totalCompatibility
        applicantScores.append(dict)


        

    
    return {"scoredApplicants": applicantScores}



print(compatibility({
"team" : [
{
"name" : "Eddie",
"attributes": {
"intelligence" : 1,
"strength" : 2,
"endurance" : 3,
"spicyFoodTolerance" : 1
}
}, {
"name" : "Will",
"attributes": {
"intelligence" : 7,
"strength" : 1,
"endurance" : 3,
"spicyFoodTolerance" : 4
}
}, {
"name" : "Mike",
"attributes": {
"intelligence" : 2,
"strength" : 2,
"endurance" : 1,
"spicyFoodTolerance" : 8
}
}
],
"applicants" : 
[
{"name" : "John", "attributes": {"intelligence" : 10, "strength" : 10, "endurance" : 10, "spicyFoodTolerance" : 10}},
{"name" : "Jane", "attributes": {"intelligence" : 7, "strength" : 4, "endurance" : 3, "spicyFoodTolerance" : 2}},
{"name" : "Joe", "attributes": {"intelligence" : 1, "strength" : 1, "endurance" : 1, "spicyFoodTolerance" : 1}}
]
}
))


















    
