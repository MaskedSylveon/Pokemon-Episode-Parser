import urllib.request

# Headers used for every API request
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

def getEverySpeciesInfo():
    everySpeciesInfo = []
    try:
        # This page has a list of every Pokemon
        url = 'https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=php&page=List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number&redirects=1&prop=wikitext'
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        pageText = str(resp.read().decode('UTF-8')).splitlines()

        id = 1
        # There can be multiple forms of one species on the list, so check to make sure we only accept one
        previousName = "" 

        # Each line of the page has information on each Pokemon that we can parse
        for line in pageText:
            pokeInfo = line.split("|")
            if len(pokeInfo) > 5:
                pkDexNum = pokeInfo[2]
                name = pokeInfo[3]
                if ("{{rdex|" in line and ((pokeInfo[2].isnumeric() and int(pokeInfo[2]) == id) or pokeInfo[2] == "???") and name != previousName):
                    primaryType = pokeInfo[5].split("}}")[0]

                    secondaryType = ''
                    image = ''

                    # Fifth element of pokeInfo tells us if a Pokemon has two types
                    if pokeInfo[4] == '2':
                        secondaryType = pokeInfo[6].split("}}")[0]
                    '''
                    # Either get an image for the Pokemon if the PokeDex number exists or use a default picture
                    if pkDexNum.isnumeric():
                        image = getPokemonImage(pkDexNum)
                    else:
                        image = 'https://cdn.bulbagarden.net/upload/a/ab/000MS.png'
                    '''
                    everySpeciesInfo.append({
                        'id': id,
                        'pkDexNum': pkDexNum,
                        'name': name,
                        'primaryType': primaryType,
                        'secondaryType': secondaryType,
                        'image': image,
                        })
                    id = id + 1
                    previousName = name
        return everySpeciesInfo    

    except Exception as e:
        print(str(e))

'''
def getPokemonImage(pkDexNum):
    try:
        # This page has a list of every Pokemon
        url = 'https://archives.bulbagarden.net/w/api.php?action=parse&format=php&page=File:' + pkDexNum + 'MS.png&redirects=1&prop=text'
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        pageText = str(resp.read().decode('UTF-8')).splitlines


    except Exception as e:
        print(str(e))
        return -1
'''