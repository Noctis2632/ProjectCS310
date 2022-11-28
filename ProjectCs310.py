user_list = []
product_list = []
calculate_list = []

def register() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"REGISTER"," "*37))
    print("=" * 86)
    with open("userdata.txt", "a") as file:
        ch = "Y"
        while ch != "N" :
            first_name, last_name = input("Enter Name Surname : ").split()
            while True:
                id_card = input("Enter ID card [13 digits] : ")
                while len(id_card) != 13:
                    print("ID card must be 13 digits")
                    id_card = input("Enter ID card [13 digits] : ")
                id_sum = ((int(id_card[0])*13) + (int(id_card[1])*12) + (int(id_card[2])*11) + (int(id_card[3])*10) + (int(id_card[4])*9) + (int(id_card[5])*8) + (int(id_card[6])*7) + (int(id_card[7])*6) + (int(id_card[8])*5) + (int(id_card[9])*4) + (int(id_card[10])*3) + (int(id_card[11])*2)) % 11
                id_true = (11 - id_sum) % 10
                if id_true == int(id_card[12]):
                    break
                else:
                    print("ID card False !")
                    print("Please try again")

            file.write("%-18s %-21s %-30s %s\n" % (first_name,last_name,id_card,str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1]))
            print("Your ID Member is",str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1])

            ch = input("Do you want to register again ? [Y/N] : ").upper()

        print("Register Complete")


def user_lists() :
    with open("userdata.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            user_list.append(item)

def product_lists() :
    with open("product.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            product_list.append(item)
 
def addstock_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    product_name = input("Enter Product Name : ")
    product_quantity = input("Enter Product Quantity : ")
    for i in range(len(product_list)):
        if product_name in product_list[i]:
            product_list[i][2] = int(product_list[i][2]) + int(product_quantity)
    with open("product.txt", "w") as file:
        for i in range(len(product_list)):
            file.write("%-13s %-23s %20s %28s\n" % (product_list[i][0],product_list[i][1],product_list[i][2],product_list[i][3]))
    print("Add Stock Product Complete")

def show_product() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    with open("product.txt", "r") as file:
        for line in file:
            print(line)
        
def show_user() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"USER"," "*41))
    print("=" * 86)
    with open("userdata.txt", "r") as file:
        for line in file:
            print(line)

def calculate() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"CALCULATE"," "*36))
    print("=" * 86)
    ch = "Y"
    while ch != "N" :
        code_number = input("Enter Code Number : ")
        product_quantity = input("Enter Product Quantity : ")
        for i in range(len(product_list)):
            if code_number in product_list[i]:
                calculate_list.append([product_list[i][1],product_quantity,(int(product_list[i][3])*int(product_quantity))])
                product_list[i][2] = int(product_list[i][2]) - int(product_quantity)

        with open("product.txt", "w") as file:
            for i in range(len(product_list)):
                file.write("%-13s %-23s %20s %28s\n" % (product_list[i][0],product_list[i][1],product_list[i][2],product_list[i][3]))
    
        ch = input("Do you want to calculate again ? [Y/N] : ").upper()

def dicount() :
    print("=" * 86)
    print("%s %s %s" % (" "*35,"DISCOUNT"," "*37))
    print("=" * 86)
    mem = input("Do you have ID Member ? [Y/N] : ").upper()
    if mem == "Y":
        id_member = input("Enter ID Member : ")
        for i in range(len(user_list)):
            if id_member in user_list[i]:
                for j in range(len(calculate_list)):
                    calculate_list[j][2] = int(calculate_list[j][2]) - int(calculate_list[j][2]) * 0.15
                    print(calculate_list[j])
        
            


# สมัครสมาชิก
# ลบสมาชิก
# เพิ่มสินค้า
# ลบสินค้า
# แสดงสินค้า
# แสดงสมาชิก
# ขายสินค้า
# คำนวณราคา

register()
show_user()
