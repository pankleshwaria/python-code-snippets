import logging
# Logging level in order of increasing severity
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


class Person:

    logger = logging.getLogger('Person')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('person.log')
    console_handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.logger.info(f"{first_name} {last_name} is born")

    def can_vote(self):
        if self.age < 18:
            self.logger.error("Boy you need to grow up for this")
            return False
        self.logger.info(f"{self.first_name} {self.last_name} can vote")

    def can_drink(self):
        if self.age < 21:
            self.logger.error("Nah, this is not the age to drink mate")
            return False
        self.logger.info(f"{self.first_name} drink responsibly")


john = Person("John", "Dow", 16)
john.can_vote()
john.can_drink()
