import pytest
from model import PlantModel

# Stan poczatkowy
def test_initial_state():
    plant = PlantModel() #klasa rosliny
    assert plant.get_moisture() == 50
    assert plant.get_light() == 60
    assert plant.get_temperature() == 22
    assert plant.get_time_of_day() == 12
    assert plant.get_health_status() == "Dobry"
    assert "roślinko" in plant.get_message()

#Podlewanie
def test_watering():
    plant = PlantModel()
    plant.water()
    assert 65 <= plant.get_moisture() <= 75
    assert plant.get_message() == "Podlano!"
    # Zdrowie nie powinno być "Potrzebuje wody!" po podlaniu
    assert plant.get_health_status() != "Potrzebuje wody!"

#Czy obnizane jest wilgotnosc
def test_simulate_one_hour_moisture_drops():
    plant = PlantModel()
    initial_moisture = plant.get_moisture()
    plant.simulate_time()

    assert plant.get_moisture() < initial_moisture
    assert 0 <= plant.get_moisture() <= 100
    assert 0 <= plant.get_light() <= 100
    assert 0 <= plant.get_temperature() <= 40


def test_simulate_day():
    plant = PlantModel()
    plant.simulate_day()
    assert 0 <= plant.get_moisture() <= 100
    assert 0 <= plant.get_light() <= 100
    assert 15 <= plant.get_temperature() <= 30
    assert isinstance(plant.get_message(), str)

#Wilgotnosc
@pytest.mark.parametrize("moisture, expected", [
    (10, "Potrzebuje wody!"),
    (95, "Za dużo wody!"),
    (50, "Dobry"),
])
def test_health_by_moisture(moisture, expected):
    plant = PlantModel()
    plant._moisture = moisture
    plant._update_health()
    assert plant.get_health_status() == expected

#Swiatlo
@pytest.mark.parametrize("light, expected", [
    (10, "Za mało światła!"),
    (50, "Dobry"),
])
def test_health_by_light(light, expected):
    plant = PlantModel()
    plant._light = light
    plant._update_health()
    assert plant.get_health_status() == expected

#temperatura
@pytest.mark.parametrize("temperature, expected", [
    (5, "Za zimno!"),
    (35, "Za gorąco!"),
    (22, "Dobry"),
])
def test_health_by_temperature(temperature, expected):
    plant = PlantModel()
    plant._temperature = temperature
    plant._update_health()
    assert plant.get_health_status() == expected
