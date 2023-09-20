def product_details():
    product_price = float(input('ป้อนราคาสินค้า : '))
    productname = input('ชื่อสินค้า : ')
    return productname, product_price

def calulateprice():
    realprice = product_price + (product_price*0.1)
    return realprice

def show_price() :
    print(f"สินค้าราคาคือ : {productname} {calulateprice()}บาท")

productname, product_price = product_details()

show_price()