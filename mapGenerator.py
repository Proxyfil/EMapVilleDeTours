import folium
import webbrowser
import json

def heatmap(data, max):
    baseColor = (0,0,255)
    max = max/2

    if(data < max/2):
        baseColor = (0,int(255*(data/(max/2))),int(255-245*(data/(max/2))))
    else:
        baseColor = (int(255*((data/2)/(max/2))),int(255-245*((data/2)/(max/2))),0)
    if(baseColor[0] > 255):
        baseColor = (255,baseColor[1],baseColor[2])
    if(baseColor[1] > 255):
        baseColor = (baseColor[0],255,baseColor[2])
    if(baseColor[2] > 255):
        baseColor = (baseColor[0],baseColor[1],255)
    return '#%02x%02x%02x' % baseColor

def heatmapLigne(data):
    baseColor = (0,0,255)
    max = 17158667

    if(data < max/2):
        baseColor = (0,int(255*(data/(max/2))),int(255-245*(data/(max/2))))
    else:
        baseColor = (int(255*((data/2)/(max/2))),int(255-245*((data/2)/(max/2))),0)

    if(baseColor[0] > 255):
        baseColor = (255,baseColor[1],baseColor[2])
    if(baseColor[1] > 255):
        baseColor = (baseColor[0],255,baseColor[2])
    if(baseColor[2] > 255):
        baseColor = (baseColor[0],baseColor[1],255)

    baseColor = '#%02x%02x%02x' % baseColor
    return {"fillColor":baseColor, "color":baseColor, "opacity":0.25}

def mystere(dictionnaire):
    '''
    Etant donné un dictionnaire passé en argument retourne une chaîne de caractères
    dont la spécification est l'objet d'une question de l'énoncé
    '''
    code = "<p> <table>"
    for cle, valeur in dictionnaire.items():
        code = code + ("<tr><td>" + str(cle) + "</td>" + "<td>" + str(valeur) + "</td></tr>")
    code = code + "</table></p>"
    return code

def generer_popup(dictionnaire):
    contenu_de_la_popup = mystere(dictionnaire)
    iframe = folium.IFrame(html = contenu_de_la_popup, width = 300, height = 200)
    popup = folium.Popup(iframe, max_width = 500)
    return popup

def ajouter_marqueur(carte, latitude, longitude, dictionnaire, couleur):
    '''
    carte : de type folium.Map
    latitude et longitude : de type float
    dictionnaire : de type dict avec clées et valeurs de type str
    couleur : au format '#RRGGBB' où RR, GG, BB sont des entiers entre 0 et 255 en hexadécimal
              représentant les composant Rouge, Verte et Bleue de la couleur
    '''
    radius = 4
    folium.CircleMarker(
        location = [latitude, longitude],
        radius = radius,
        popup = generer_popup(dictionnaire),
        color = couleur,
        fill = True
    ).add_to(carte)

def creer_dict_popup(arret):
    dico_extrait = {'Nom': arret['name'], 'Passages': arret['amount']}
    return dico_extrait

def donner_latitude(aeroport):
    latitude = arret["lat"]
    return float(latitude)


def donner_longitude(aeroport):
    longitude = arret["lon"]
    return float(longitude)

def charger_fichier( nom_fic ):
    ficher = open(nom_fic,'r', encoding='utf-8')
    contenu = json.loads(ficher.read())

    return contenu


#étape 1 : création de la carte
ma_carte = folium.Map(location=(45, 0), zoom_start=4)

#étape 2 : ajout de marqueurs
f = charger_fichier("./output/stopsHours.json")

for arret in f.values():
    ajouter_marqueur(ma_carte, donner_latitude(arret), donner_longitude(arret), creer_dict_popup(arret), heatmap(arret["amount"], 6465))

f = charger_fichier("./reseau-fil-bleu-2021-2022-syndicat-des-mobilites.geojson")
frequency = {'A': {'amount': 17158667.0}, 'B': {'amount': 14178.0}, '2': {'amount': 5346350.0}, '3': {'amount': 3071358.0}, '4': {'amount': 2433522.0}, '5': {'amount': 2903152.0}, '10': {'amount': 1457266.0}, '11': {'amount': 672531.0}, '12': {'amount': 464914.0}, '13': {'amount': 0.0}, '14': {'amount': 1300441.0}, '15': {'amount': 841429.0}, '16': {'amount': 900593.0}, '17': {'amount': 524736.0}, '18': {'amount': 104379.0}, '19': {'amount': 34237.0}, '20': {'amount': 13472.0}, 'C1': {'amount': 0.0}, 'C2': {'amount': 4595.0}, 'C1 (anc. C)': {'amount': 97885.0}, 'C3': {'amount': 2570.0}, 'C4': {'amount': 2873.0}, '30': {'amount': 142827.0}, '31': {'amount': 113191.0}, '32': {'amount': 26101.0}, '34': {'amount': 45541.0}, '35': {'amount': 42323.0}, '36': {'amount': 53250.0}, '50': {'amount': 872121.0}, '51': {'amount': 71081.0}, '52': {'amount': 94635.0}, '53': {'amount': 134716.0}, '54': {'amount': 192048.0}, '56': {'amount': 172436.0}, '57': {'amount': 18172.0}, 'R1': {'amount': 48.0}, 'R2': {'amount': 153.0}, 'R3': {'amount': 3771.0}, 'R4': {'amount': 709.0}, 'R5': {'amount': 1836.0}, 'R6': {'amount': 2017.0}, 'R7': {'amount': 69.0}, 'R8': {'amount': 185.0}, 'R9': {'amount': 1197.0}, 'R11': {'amount':0}, 'F30': {'amount': 2479.0}, 'F31': {'amount': 4070.0}, 'F55': {'amount': 1362.0}, 'F57': {'amount': 282.0}, 'TAD soignants (+vaccinations)': {'amount': 0.0}, '60': {'amount': 64571.0}, '61': {'amount': 8436.0}, '62': {'amount': 37514.0}, '63': {'amount': 34612.0}, '64': {'amount': 6847.0}, '65': {'amount': 5446.0}, '66': {'amount': 8441.0}, '67': {'amount': 15017.0}, '68': {'amount': 26483.0}, '69': {'amount': 10435.0}, '70': {'amount': 17493.0}, '71': {'amount': 9899.0}, '72': {'amount': 42130.0}, '73': {'amount': 21419.0}, '74': {'amount': 5451.0}, '75': {'amount': 6524.0}, '76': {'amount': 660.0}, '106': {'amount': 0.0}, '117': {'amount': 1903.0}, '140': {'amount': 366.0}, '83': {'amount': 3746.0}, 'Spéciaux et occasionnels': {'amount': 3121.0}, 'Navette TRAIN': {'amount': 15700.0}, 'Non reconnu *': {'amount': 114269.0}, 'M-ticket bus': {'amount': 0.0}, '3A':{"amount":3071358},'3B':{"amount":3071358}, 'R10': {'amount':0}}
try:
    l = folium.GeoJson(f, name="Lignes", style_function=lambda x: heatmapLigne(frequency[x["properties"]["route_short_name"]]['amount'])).add_to(ma_carte)
    l.add_child(folium.features.GeoJsonTooltip(fields=['route_short_name']))
except ValueError:
    pass

folium.LayerControl().add_to(ma_carte)

#étape 3 : sauvegarde de la carte au format HTML dans le dossier courant
ma_carte.save('carte.html')

#étape 4 : ouverture du fichier dans le navigateur par défaut
webbrowser.open('carte.html')