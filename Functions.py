"""
Problem 1:

Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
"""

def calc_final_price(item_p, prime_member):
    black_friday_discount = item_p *0.92

    if prime_member:
        discount = black_friday_discount*0.85
    else:
        discount= black_friday_discount
    
    return discount
item_p = 98
prime_member = True
final_price = calc_final_price(item_p, prime_member)
print(final_price)

"""
Problem 2:

Chit Chat Application - Function:

(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.


(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
"""
def t_message(message):
    if len(message) > 200:
        return message[:200]
    else:
        return message
message = "This is a long message that is over 200 characters. We need to truncate it."
restricted_message = t_message(message)
print(restricted_message)