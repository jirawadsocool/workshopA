def product_details():
    product_name = (input("ชื่อสินค้า : "))
    product_price = (float(input("ราคาสินค้า : ")))
    return product_price,product_name

product_name, product_price = product_details()

def calculate():
    tax = int(product_price) * 7 / 100
    return tax

def show():
    print(f'ชื่อสินค้า : {product_name} ราคา : {product_price} รวมภาษี 7 % จะได้ : {float(calculate())}บาท')

show()