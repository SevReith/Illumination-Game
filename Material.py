class Material(object):
    """description of class"""

    def __init__(self, name, price, quality, init_amount, req_amount, seller_name = 'Ozeania' ):
        self.name = name
        self.price = price
        self.quality = quality
        self.amount = init_amount
        self.required_amount = req_amount
        self.seller_name = seller_name
        


class Glass_Bulb(Material):

    pass
