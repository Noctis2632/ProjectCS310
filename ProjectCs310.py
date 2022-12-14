user_list = []
user_idmember = []
product_list = []
p_code = []
p_name = []
p_quantity = []
p_price = []
calculate_list = []

def user_lists() : # เพิ่มข้อมูลสมาชิกลงlist
    user_list.clear()
    user_idmember.clear()
    with open("userdata.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            user_list.append(item)
            user_idmember.append(item[3])

def product_lists() : # เพิ่มข้อมูลสินค้าลงlist
    product_list.clear()
    p_code.clear()
    p_name.clear()
    p_quantity.clear()
    p_price.clear()
    with open("product.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            item = line.split()
            product_list.append(item)
            p_code.append(item[0])
            p_name.append(item[1])
            p_quantity.append(item[2])
            p_price.append(item[3])

def register() :   # สมัครสมาชิก
    print("=" * 86)
    print(" "*35,"REGISTER"," "*37)
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
            
            print("-" * 86)
            file.write("%-18s %-21s %-30s %s\n" % (first_name,last_name,id_card,str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1]))
            print("Your ID Member is",str((ord(first_name[0])+ord(last_name[1]))) + id_card[7] + id_card[3] + id_card[6] + id_card[8] + id_card[5] + id_card[12] + id_card[1])
            print("-" * 86)

            ch = input("Do you want to register again ? [Y/N] : ").upper()
            print("-" * 86)

        print(" "*31,"Register Complete")

def delete_member() : # ลบข้อมูลสมาชิก
    print("=" * 86)
    print("%s %s %s" % (" "*31,"DELETE MEMBER"," "*37))
    print("=" * 86)
    ch = "Y"
    while ch != "N" :
        id_member = input("Enter ID Member : ")
        while id_member not in user_idmember:
            print("ID Member Not found")
            id_member = input("Enter ID Member : ")
        index = user_idmember.index(id_member)
        user_list.pop(index)
        print("-" * 86)
        print(" "*26,"Delete Member Complete")
        print("-" * 86)
        with open("userdata.txt", "w") as file:
            for i in range(len(user_list)):
                file.write("%-18s %-21s %-30s %s\n" % (user_list[i][0],user_list[i][1],user_list[i][2],user_list[i][3]))
        ch = input("Do you want to delete again ? [Y/N] : ").upper()

def addstock_product() :
    print("=" * 86)
    print(" "*32,"ADD STOCK PRODUCT"," "*39)
    print("=" * 86)
    ch = "Y"
    while ch != "N" :
        product_name = input("Enter Product Name : ")
        while product_name not in p_name: 
            print("Product Not found")
            product_name = input("Enter Product Name : ")
        index = p_name.index(product_name)
        product_quantity = input("Enter Product Quantity : ")
        p_quantity[index] = int(p_quantity[index]) + int(product_quantity)  # บวกจำนวนสินค้าเข้าไปในlist
        print("-" * 86)
        print(" "*32,"Add Stock Complete")
        print("-" * 86)

        with open("product.txt", "w") as file:
            for i in range(len(p_name)):
                file.write("%-13s %-23s %20s %27s\n" % (p_code[i],p_name[i],p_quantity[i],p_price[i]))

        ch = input("Do you want to add stock again ? [Y/N] : ").upper()
        print("-" * 86)

def show_user() : # แสดงข้อมูลสมาชิก
    print("=" * 86)
    print(" "*35,"USERDATA"," "*41)
    print("=" * 86)
    with open("userdata.txt", "r") as file:
        for line in file:
            print(line)

def show_product() : # แสดงข้อมูลสินค้า
    print("=" * 86)
    print("%s %s %s" % (" "*35,"PRODUCT"," "*39))
    print("=" * 86)
    with open("product.txt", "r") as file:
        for line in file:
            print(line)

def calculate() : # คำนวณราคาสินค้า ทำNot found ไม่ได้
    print("=" * 86)
    print(" "*35,"CALCULATE"," "*36)
    print("=" * 86)
    calculate_list.clear()
    ch = "Y"
    while ch != "N" :
        code_number = input("Enter Code Number : ")
        while code_number not in p_code:
            print("Code Number Not found")
            code_number = input("Enter Code Number : ")
        index = p_code.index(code_number)
        product_quantity = input("Enter Product Quantity : ")
        p_quantity[index] = int(p_quantity[index]) - int(product_quantity)  # ลบจำนวนสินค้าออกจากlist
        for i in range(len(p_name)):
            if p_code[i] == code_number:
                calculate_list.append([p_name[i],product_quantity,p_price[i]])
        print("-" * 86)
        print(" "*30,"Calculate Complete")
        print("-" * 86)

        with open("product.txt", "w") as file:
            for i in range(len(p_name)):
                file.write("%-13s %-23s %20s %27s\n" % (p_code[i],p_name[i],p_quantity[i],p_price[i]))
    
        ch = input("Do you want to calculate again ? [Y/N] : ").upper()
        print("-" * 86)

def dicount() : # คำนวณส่วนลด
    print("=" * 86)
    print(" "*35,"DISCOUNT"," "*37)
    print("=" * 86)
    mem = input("Do you have ID Member ? [Y/N] : ").upper()
    print("-" * 86)
    if mem == "Y":
        id_member = input("Enter ID Member : ")
        while id_member not in user_idmember:
            print("ID Member Not found")
            id_member = input("Enter ID Member : ")
        for i in range(len(calculate_list)):
            calculate_list[i][2] = int(calculate_list[i][2]) - int(calculate_list[i][2]) * 0.15
        print("-" * 86)
        print(" "*30,"Discount Complete")
        print("-" * 86)

                    
def receipt() : # ใบเสร็จ
    print("=" * 86)
    print(" "*35,"RECEIPT"," "*39)
    print("=" * 86)
    print("%-30s %20s %30s" % ("Product Name","Quantity","Price"))
    for i in range(len(calculate_list)):
        print("%-30s %20s %30s" % (calculate_list[i][0],calculate_list[i][1],calculate_list[i][2]))
    print("=" * 86)
    print("%45s %s" % (("total price : "),(sum(calculate_list[i][2] for i in range(len(calculate_list))))))
    print("-" * 86)

def menu () : # หน้าเมนู
    print("=" * 86)
    print(" "*35,"MAIN MENU"," "*37)
    print("=" * 86)
    print("1. Register")
    print("2. Delete Member")
    print("3. Add Stock Product")
    print("4. Show UserData")
    print("5. Show Product")
    print("6. Sell Product")
    print("7. Exit")
    print("=" * 86)

def welcome() : # หน้ายินดีต้อนรับ
    print("=" * 86)
    print(" "*30,"WELCOME TO SHOP SYSTEM"," "*39)


welcome()
choice = 0
while choice != "7" :
    user_lists()
    product_lists()
    menu ()
    choice = input("Enter your choice : ")
    if choice == "1":
        register()
    elif choice == "2":
        delete_member()
    elif choice == "3":
        addstock_product()
    elif choice == "4":
        show_user()
    elif choice == "5":
        show_product()
    elif choice == "6":
        show_product()
        calculate()
        dicount()
        receipt()
    elif choice == "7":
        print("-" * 86)
        print(" "*35,"Exit Program")
        print("-" * 86)
    else:
        print("Choice Not Found")
