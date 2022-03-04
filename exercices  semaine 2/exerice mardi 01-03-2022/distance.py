import math

 # Fonction de conversion de DMS en DD
def convertisseur_dms_dd(d,m,s):   
    return(d+((m*60+s)/3600))


 # Fontion de calcul de distance
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return (distance)


 # Calcule de distance entre Paris et le pole nord 
def distance_pole_nord(long_d, long_m, long_s, lat_d, lat_m, lat_s):  
    longitude_X = convertisseur_dms_dd(long_d, long_m, long_s)
    latitude_Y = convertisseur_dms_dd(lat_d,lat_m,lat_s)
    LONG_POLE_NORD=86
    LATITUDE_POLE_NORD=172

    return(distance(longitude_X, latitude_Y, LONG_POLE_NORD, LATITUDE_POLE_NORD))

D_LONG_PARIS = 2
M_LONG_PARIS = 21
S_LONG_PARIS = 7.99

D_LAT_PARIS = 48
M_LAT_PARIS = 51
S_LAT_PARIS = 7.99

print (distance_pole_nord(D_LONG_PARIS, M_LONG_PARIS, 
                          S_LONG_PARIS , D_LAT_PARIS, 
                          M_LAT_PARIS, S_LAT_PARIS))