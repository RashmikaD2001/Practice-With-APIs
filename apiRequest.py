import requests
import json

base = 'http://universities.hipolabs.com'

def apiDetail():
    response = requests.get(base)
    responseJson = response.json()
    if(response.status_code == 200):
        return responseJson["author"]["name"] + " " + responseJson["author"]["website"]
    else:
        return f'status code - {response.status_code}'

def getAllUniversitiesByCountry(country):
    if(country.isspace()):
        country = "%20".join(country.split(" "))
    url = base + '/search?country='+country
    response = requests.get(url)
    responseJson = response.json()
    if(response.status_code == 200):
        return responseJson
    else:
        return f'status code - {response.status_code}'

def compareNumberOfUniversitiesInCountries(countries):
    data = dict()
    for i in countries:
        res = getAllUniversitiesByCountry(i)
        data.update({i:len(res)})
    return data

def searchYourUniversity(name):
    url = base + '/search?name=' + name
    if(name.isspace()):
        name = "%20".join(name.split(" "))
    response = requests.get(url)
    responseJson = response.json()
    if(response.status_code == 200):
        university = responseJson[0]
        msg = f'result - {university["name"]}, {university["country"]}, {university["web_pages"][0]}'
        return msg
    else:
        return f'status code - {response.status_code}'

if __name__ == '__main__':
    print('Inside API python script')
