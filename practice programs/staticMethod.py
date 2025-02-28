class employee:
    def __init__(self,name ,position):
        self.name =name
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position=["manager","cashier","cook","janitor"]
        return position in valid_position
    
    # here we need not create an object like a=employee( )