# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Subclass with inheritance
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera...")

# Creating instances
phone = Smartphone("Apple", "iPhone 13", 999)
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 799, 108)
camera_phone.take_photo()
