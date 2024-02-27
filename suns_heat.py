import time 

def suns_heat(planet_name):
    assert  type(planet_name) == str
    if planet_name in dict_name_heat:
        return dict_name_heat[planet_name]
    else:
	return "Unknown planet"

dict_name_heat = {'earth': 30}

planet_name = input("Which planet heat do you want?")

print(suns_heat(planet_name))git 

time.sleep(1)