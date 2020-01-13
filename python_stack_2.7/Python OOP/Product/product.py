class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self):
        self.price = float(self.price) + (float(self.price) * .09)
        self.price = "{:.2f}".format(self.price)
        return self

    def Return(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.price = 0
            self.status = "defective"
        elif self.reason == "returned in the box, like new":
            self.status = "for sale"
        elif self.reason == "the box has been opened":
            self.status = "used"
            self.price -= float(self.price) * .20
            self.price = "{:.2f}".format(self.price)
        else:
            print "Please refer to operator that filed return application transcript."
        return self 
    
    def display_info(self):
        print "Price: " + str(self.price) + " USD"
        print "Item Name: " + self.item_name
        print "Weight: " + str(self.weight) + " lbs"
        print "Brand: " + self.brand
        print "Status: " + self.status
        return self

product_a = Product(20, "untold_ancient_knowledge", 666666, "spiritually energy")
print product_a.Return("returned in the box, like new").add_tax().display_info()

