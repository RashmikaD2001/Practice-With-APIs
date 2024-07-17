import apiRequest
import numpy as np
import matplotlib.pyplot as plt 

intro = """press 1 for search your university
press 2 for get all university by country
press 3 for compare number of universities in different countries
press 4 for api details
press 5 for exit"""
print(intro)

run = True

while(run):
    try:
        inp = input("your input = ")

        match inp:
            case "1":
                name = input("enter your university: ")
                print(apiRequest.searchYourUniversity(name))
                print(type(apiRequest.searchYourUniversity(name)))

            case "2":
                country = input("enter your country: ")
                universities = apiRequest.getAllUniversitiesByCountry(country)
                for i in universities:
                    print(i["name"])

            case "3":
                countries = countries = input("Enter countries (space-separated): ").split()
                dataDict = apiRequest.compareNumberOfUniversitiesInCountries(countries)

                courses = list(dataDict.keys())
                values = list(dataDict.values())
                fig = plt.figure(figsize = (10, 5))

                plt.bar(courses, values, color ='maroon', width = 0.4)
                plt.xlabel("Countries")
                plt.ylabel("No. of universities")
                plt.title("No. of universities in different countries")
                plt.show()

            case "4":
                print(apiRequest.apiDetail())

            case "5":
                print("Thank you!!!")
                run = False

            case _:
                print("Check your input")
    except Exception as e:
        print(e)

