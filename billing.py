#this is space to write the billing code for the github demo

def process_payment(amount, card_number, expiration_date, cvv):
    # Placeholder for payment processing logic
    if amount > 0 and len(card_number) == 16 and len(cvv) == 3:
        return True
    else:
        return False
    

    