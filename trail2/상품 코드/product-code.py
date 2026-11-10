product_name, product_code = input().split()
product_code = int(product_code)

class product :
    def __init__(self,pn,pc) :
        self.pn = pn
        self.pc = pc

product1 = product("codetree",50)
product2 = product(product_name,product_code)

print(f"product {product1.pc} is {product1.pn}")
print(f"product {product2.pc} is {product2.pn}")
# Please write your code here.