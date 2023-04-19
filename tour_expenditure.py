class HotelBill:
    def __init__(self, room_type: str, num_days: int, food_amount: float):
        self.room_type = room_type
        self.num_days = num_days
        self.food_amount = food_amount

    def calculate_bill(self):
        if self.room_type == 'Delux Room':
            room_tariff = 7500 * self.num_days
            food_tax = 0.18 * self.food_amount
        elif self.room_type == 'Non AC Room':
            room_tariff = 4500 * self.num_days
            food_tax = 0.05 * self.food_amount
        else:
            raise ValueError("Invalid room type")
        
        tip_amount = 0.1 * self.food_amount
        cgst = sgst = 0.5 * food_tax
        total_amount = room_tariff + self.food_amount + food_tax + tip_amount + cgst + sgst

        print(f"Room Tariff: {room_tariff:.2f}")
        print(f"GST on Food: CGST {cgst:.2f}, SGST {sgst:.2f}")
        print(f"Tip Amount: {tip_amount:.2f}")
        print(f"Total Bill: {total_amount:.2f}")
bill = HotelBill('Delux Room', 5, 3000)
bill.calculate_bill()