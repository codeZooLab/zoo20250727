### 简化版购物函数

class ProductsModel:
    products = [
        {"name": "苹果", "price": 5, "stock": 10},
        {"name": "香蕉", "price": 3, "stock": 20},
        {"name": "橙子", "price": 4, "stock": 15},
        {"name": "西瓜", "price": 10, "stock": 5},
    ]

class ProductsManageController:
    def __init__(self):
        self.__product_cart = []

    def is_number(self,value):  # 判断是否是数字
        if  value.isdigit():
            return True
        return False

    def check_product_id(self,value,product_info):  # 商品编号有效性校验
        if not self.is_number(value):
            return False
        product_index = int(value) - 1
        if product_index < 0 or product_index >= len(product_info):
            return False
        else:
            return True

    def ckeck_number(self,number, product_info):  # 商品数量有效性校验
        if not self.is_number(number):
            return False
        elif int(number) <= 0 or int(number) > product_info["stock"]:
            return False
        else:
            return True

    def add_cart(self,product_info,num):
        """
        根据选择的商品编号和数量添加购物车
        :param product_info: 选择的商品编号
        :param num: 数量
        """
        cart_item = {
            "name": product_info["name"],
            "price": product_info["price"],
            "quantity": num
        }
        self.__product_cart.append(cart_item)
        product_info["stock"] -= int(num)
        print(f"已添加 {num} 个 {product_info['name']} 到购物车!")

    def get_product_cart(self):  # 打印购物车信息
        print("\n购物车:")
        for item in self.__product_cart:
            print(f"{item['name']} - 价格: {item['price']}元 x {item['quantity']} = {float(item['price']) * int(item['quantity'])}元")

    def cart_total_price(self):  # 计算购物车总价
        total_price = 0
        for item in self.__product_cart:
            total_price += float(item["price"]) * int(item["quantity"])
        print("\n商品总价%.2f"%(total_price))
        return total_price

    def ckeck_payment(self,money,price):
        # 判断支付金额合法性
        if not self.is_number(money):
            return False
        if int(money) < price:
            return False
        else:
            return True

    def settlement(self,money,price):
        change = int(money) - price
        print(f"支付成功! 找零: {change}元")

class ProductsView:
    def __init__(self):
        self.__item_info = ProductsModel()
        self.__item_manage = ProductsManageController()

    def __get_product_info(self,product_info):  # 打印商品信息
        print("\n商品列表:")
        for i, product in enumerate(product_info):
            print(f"{i + 1}. {product['name']} - 价格: {product['price']}元, 库存: {product['stock']}")
    def __display_menu(self):
        print("\n1)选购商品")
        print("2)展示购物车")
        print("3)结算购物车")
        print("4)退出购物")

    def __select_menu(self):
        item = int(input("请输入:"))
        if item == 1:
            self.__input_product_cart()
        elif item == 2:
            self.__output_product_cart()
        elif item == 3:
            self.__settlement_product_cart()
        elif item == 4:
            print("购物结束")
            exit()

    def main(self):
        while True:
            self.__get_product_info(self.__item_info.products)
            self.__display_menu()
            self.__select_menu()

    def __input_product_cart(self):
        id = input("请输入加购的商品编号:")
        if not self.__item_manage.check_product_id(id,self.__item_info.products):
            print("请输入有效的商品编号!")
            return
        quantity = input("请输入购买的数量:")
        if not self.__item_manage.ckeck_number(quantity,self.__item_info.products[(int(id)-1)]):
            print("请输入库存范围内有效的商品数量!")
            return
        re01 = (self.__item_info.products[(int(id) - 1)])
        self.__item_manage.add_cart(re01,quantity)

    def __output_product_cart(self):
        self.__item_manage.get_product_cart()

    def __settlement_product_cart(self):
        price= self.__item_manage.cart_total_price()
        money = input("请支付金额:")
        if not self.__item_manage.ckeck_payment(money,price):
            print("请支付合理金额!")
            return
        self.__item_manage.settlement(money,price)

view = ProductsView()
view.main()