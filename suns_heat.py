import time 

def suns_heat(planet_name):
    assert  type(planet_name) == str
    if planet_name in dict_name_heat:
        return dict_name_heat[planet_name]
    else:
	    return "Unknown planet"

dict_name_heat = {'earth': 30,
                  'mars': 60,
                  'venus': 10}

while True:
    planet_name = input("Which planet heat do you want? (all lower caps)")
    print(suns_heat(planet_name))

time.sleep(1)