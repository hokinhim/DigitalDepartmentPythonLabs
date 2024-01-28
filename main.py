class TransportVehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор класса TransportVehicle.
        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def move(self, destination: str) -> str:
        """
        Возвращает перемещение транспортного средства.
        :param destination: Место назначения.
        :return: Строка с информацией о перемещении.
        """
        return f"{self.brand} {self.model} is moving to {destination}."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        :return: Строковое представление объекта.
        """
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        :return: Формальное строковое представление объекта.
        """
        return f"TransportVehicle(brand={self.brand}, model={self.model}, year={self.year})"


class Car(TransportVehicle):
    """
    Дочерний класс, представляющий легковой автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str, fuel_level: float = None):
        """
        Конструктор класса Car.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param fuel_type: Тип топлива, используемый автомобилем.
        :param fuel_level: Уровень топлива (по умолчанию None, чтобы не устанавливать начальное значение).
        """
        super().__init__(brand, model, year)
        self._fuel_type = fuel_type
        self._fuel_level = 0.0 if fuel_level is None or fuel_level <= 0 else fuel_level

    def honk(self) -> str:
        """
        Метод, представляющий звук автомобильного сигнала.
        :return: Строка со звуком сигнала.
        """
        return "Honk! Honk!"

    def move(self, destination: str) -> str:
        """
        Перегруженный метод перемещения для автомобиля.
        :param destination: Место назначения.
        :return: Строка с информацией о перемещении автомобиля.

        Причина перегрузки: Метод move() перегружен для автомобиля с целью уточнения количества топлива.
        """
        return f"{self.brand} {self.model} is driving to {destination} with {self._fuel_level} gallons."

    def refuel(self, fuel_amount: float) -> None:
        """
        Заправляет автомобиль указанным количеством топлива.
        :param fuel_amount: Количество топлива для заправки.
        """
        if fuel_amount > 0:
            self._fuel_level += fuel_amount

    @property
    def fuel_level(self) -> float:
        """
        Возвращает текущий уровень топлива в автомобиле.
        :return: Уровень топлива.
        """
        return self._fuel_level

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        :return: Строковое представление объекта.
        """
        return f"{super().__str__()} ({self._fuel_type})"


class Bicycle(TransportVehicle):
    """
    Дочерний класс, представляющий велосипед.
    """

    def __init__(self, brand: str, model: str, year: int, frame_material: str):
        """
        Конструктор класса Bicycle.
        :param brand: Марка велосипеда.
        :param model: Модель велосипеда.
        :param year: Год выпуска велосипеда.
        :param frame_material: Материал рамы велосипеда.
        """
        super().__init__(brand, model, year)
        self.frame_material = frame_material

    def pedal(self) -> str:
        """
        Возвращает педалирование велосипеда.
        :return: Строка с информацией о педалировании.
        """
        return "Pedaling the bicycle."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        :return: Строковое представление объекта.
        """
        return f"{super().__str__()} ({self.frame_material} frame)"


if __name__ == "__main__":
    # Создание экземпляров объектов
    vehicle1 = TransportVehicle(brand="Generic", model="Vehicle", year=2022)
    car1 = Car(brand="Toyota", model="Camry", year=2022, fuel_type="Gasoline", fuel_level=35.0)
    bicycle1 = Bicycle(brand="Giant", model="Defy", year=2022, frame_material="Carbon Fiber")

    # Использование методов и атрибутов объектов TransportVehicle
    print(vehicle1.move("destination"))
    print(vehicle1.__str__())

    print()

    # Использование методов и атрибутов объектов Car
    print(car1.move("work"))
    print(car1.honk())
    print(f"Current Fuel Level: {car1.fuel_level:.2f} gallons")
    car1.refuel(10.0)
    print(f"Refueled! Current Fuel Level: {car1.fuel_level:.2f} gallons")
    print(car1.__str__())

    print()

    # Использование методов и атрибуты объектов Bicycle
    print(bicycle1.move("park"))
    print(bicycle1.pedal())
    print(bicycle1.__str__())
