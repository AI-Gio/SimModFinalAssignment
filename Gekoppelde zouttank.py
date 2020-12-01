import numpy as np
import matplotlib.pyplot as plt

"""__==** TANKS INFO **==__"""
# info tank A
tank_inhoud = 100  # liter
instroom_a = 6 / 60  # liter/s
instroom_ab = 1 / 60  # liter/s
uitstroom_ab = 3 / 60  # liter/s
uitstroom_a = 4 / 60  # liter/s
concentratie_instroom = 0.2  # kg/L

# info tank B
# Tank inhoud is hetzelfde als bij tank a
instroom_b = uitstroom_ab  # liter/s
uitstroom_ba = 1 / 60  # liter/s
uitstroom_b = 2 / 60  # liter/s

"""__==** SIMULATION PREPARATION**==__"""
def simulation_set():
    """
    Set de variabelen voor de simulatie
    :return: stapgrootte: in seconden(int), aantal_stappen: hoeveel stappen er worden genomen over een duur van 36000 seconden(int)
    """
    duur = 10 * 3600          # 3600 seconden = 1 uur
    aantal_stappen = 100
    stapgrootte = duur / aantal_stappen     # in seconden
    return stapgrootte, aantal_stappen

def make_array(stapgrootte, aantal_stappen, xzero_value):
    """
    Creert een array met zeros(float) erin en maakt nog een array voor tijdsinterval aanduiding
    :param stapgrootte: in seconden
    :param aantal_stappen: 10 uur word verdeeld in "aantal_stappen"
    :param xzero_value: met hoeveel kg zout een tank begint
    :return: zout_array: een array waar zeros in staan(lst), tijd: array met stappen van "stapgrootte" met de lengte van "aantal_stappen"(lst)
    """
    zout_arr = np.zeros(aantal_stappen + 1)
    zout_arr[0] = xzero_value   # de tank begint met xzero_value in kg zout
    tijd = stapgrootte * np.arange(aantal_stappen + 1)
    return zout_arr, tijd

"""__==** CALCULATE AND SHOW **==__"""
def simulation(zout_a, zout_b, aantal_stappen, stapgrootte):
    """
    Berekent de zoutconcentratie van tank A en tank B voor elke stap in de arrays
    :param zout_a: array met zeros
    :param zout_b: array met zeros
    """
    # De totale uitstromingen van a en b
    tot_uit_a = uitstroom_ab + uitstroom_a
    tot_uit_b = uitstroom_b + uitstroom_ba

    for stap in range(1, aantal_stappen + 1):
        # De concentratie van de tanks van de vorige stap
        concen_a_t_min1 = zout_a[stap - 1] / tank_inhoud  # kg/L
        concen_b_t_min1 = zout_b[stap - 1] / tank_inhoud  # kg/L

        # uitleg staat in het verslag op github
        zout_a[stap] = zout_a[stap - 1] + stapgrootte * (((concentratie_instroom * instroom_a) + (concen_b_t_min1 * instroom_ab)) - (concen_a_t_min1 * tot_uit_a))
        zout_b[stap] = zout_b[stap - 1] + stapgrootte * ((concen_a_t_min1 * instroom_b) - (tot_uit_b * concen_b_t_min1))

def create_graph(zout_a, zout_b, tijd):
    """
    Creert een grafiek waar zout_a en zout_b zijn verwerkt tegenover de tijd
    :param zout_a: array met voor elke stap een zoutconcentratie in kg/L voor zouttank A
    :param zout_b: array met voor elke stap een zoutconcentratie in kg/L voor zouttank B
    :param tijd: array met tijdsinterval
    :return:
    """
    plt.plot(tijd, zout_a / 100, label="zouttank A")
    plt.plot(tijd, zout_b / 100, label="zouttank B")
    plt.xlabel('tijd (seconden)')
    plt.ylabel('zout concentratie (kg / liter)')
    plt.title('zoutconcentratie in de tank')
    plt.legend()
    plt.show()

stapgrootte, aantal_stappen = simulation_set()
zout_a, tijd = make_array(stapgrootte, aantal_stappen, 0)
zout_b, _ = make_array(stapgrootte, aantal_stappen, 20)
simulation(zout_a, zout_b, aantal_stappen, stapgrootte)
create_graph(zout_a, zout_b, tijd)