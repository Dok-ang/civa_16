import mysql.connector
# З'єднання з базою даних
connection = mysql.connector.connect(
    host='localhost',  # або 'localhost' для локального сервера
    user='root',
    password='root',
    port=2023  # порт, на якому працює MySQL
)
# Створення об'єкта курсора
cursor = connection.cursor()
# Створення бази даних (якщо її ще не існує)
name_base="civilization122"
cursor.execute(f'DROP DATABASE IF EXISTS {name_base}')
connection.commit()
create_database_query = "CREATE DATABASE IF NOT EXISTS {0}".format(name_base)
cursor.execute(create_database_query)
# Вибір бази даних
cursor.execute("USE {0}".format(name_base))
users="users"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(16) NOT NULL,
    name VARCHAR(32) NOT NULL,
    email VARCHAR(50)
)""".format(users))

resource="resource"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_resource INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    mining_speed BIGINT
)""".format(resource))


# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_speed) VALUES (%s, %s)".format(resource)
data = ("people", 500)
cursor.execute(command, data)
data = ("food", 10)
cursor.execute(command, data)
data = ("tree", 60)
cursor.execute(command, data)
data = ("stone", 90)
cursor.execute(command, data)
data = ("oil", 450)
cursor.execute(command, data)
data = ("iron", 150)
cursor.execute(command, data)
data = ("gold", 300)
cursor.execute(command, data)

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_people INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("people",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_food INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("food",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tree INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("tree",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_stone INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("stone",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_oil INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("oil",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_iron INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("iron",users))

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_gold INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("gold",users))


buildings="buildings"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_building INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    mining_speed INT NOT NULL,   
    resource_multiplier INT NOT NULL,   
    people INT NOT NULL,
    food INT NOT NULL,
    tree INT NOT NULL,
    stone INT NOT NULL,
    oil INT NOT NULL,
    iron INT NOT NULL,
    gold INT NOT NULL  )""".format(buildings))
# mining_speed - швидкість побудови
# resource_multiplier - доданок за кожен ресурс

# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_speed, resource_multiplier, people, food, tree, stone, oil, iron, gold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(buildings)
data = ("farm", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("sawmill", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("mine_stone", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("oil_well", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("mine_iron", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("mine_gold", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("barracks_soldiers", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("transport", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("barracks_arrows", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("barracks_berserkers", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("tank_factory", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)
data = ("airfield", 1000, 1, 2, 1, 10, 5, 0, 0, 50)
cursor.execute(command, data)


# buildings_time - час останньої побудови
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_farm INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("farm",users)) # ферма

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_sawmill INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("sawmill",users)) # лісопилка

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine_stone INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("mine_stone",users)) # шахтя камня

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_oil_well INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("oil_well",users)) # нафта

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine_iron INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("mine_iron",users)) # шахтя заліза

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_mine_gold INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("mine_gold",users)) # шахтя золота





cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_barracks_soldiers INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("barracks_soldiers",users)) # казарма солдат баланс

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_transport INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT, 
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("transport",users)) # transport

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_barracks_arrows INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("barracks_arrows",users)) # стрілки захисні

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_barracks_berserkers INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,  
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("barracks_berserkers",users)) # berserkers атакуючі

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tank_factory INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,   
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("tank_factory",users)) # танк

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_airfield INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,  
    new_buildings_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("airfield",users)) # аеродром вертольотів


army="army"
cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_army INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    mining_speed BIGINT NOT NULL,
    people INT NOT NULL,
    food INT NOT NULL,
    tree INT NOT NULL,
    stone INT NOT NULL,
    oil INT NOT NULL,
    iron INT NOT NULL,
    gold INT NOT NULL,
    health INT NOT NULL,
    attack INT NOT NULL,
    protection INT NOT NULL,
    coefficient FLOAT NOT NULL,
    inventory_capacity INT NOT NULL,
    service INT NOT NULL              
)""".format(army))
# coefficient 0.5 - +50% захисту, -50% атаки і навпаки при 1.5
# 

# Вставка даних в таблицю
command = "INSERT INTO {0} (name, mining_speed, people, food, tree, stone, oil, iron, gold, health, attack, protection, coefficient, inventory_capacity, service) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(buildings)
data = ("soldiers", 1000, 1, 2, 1, 1, 0, 0, 50, 100, 60, 20, 0.5, 2, 1)
cursor.execute(command, data)
data = ("transport", 1000, 2, 4, 0, 10, 0, 0, 100, 0, 0, 0, 1, 20, 1)
cursor.execute(command, data)
data = ("arrows", 1000, 1, 2, 1, 1, 0, 0, 50, 100, 60, 20, 1, 2, 1)
cursor.execute(command, data)
data = ("berserkers", 1000, 1, 2, 1, 1, 0, 0, 50, 100, 60, 20, 1, 2, 1)
cursor.execute(command, data)
data = ("tanks", 1000, 1, 2, 1, 1, 0, 0, 50, 100, 60, 20, 1, 2, 1)
cursor.execute(command, data)
data = ("helicopter", 1000, 1, 2, 1, 1, 0, 0, 50, 100, 60, 20, 1, 2, 1)
cursor.execute(command, data)


cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_soldiers INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,    
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("soldiers",users)) # soldiers

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_arrows INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,   
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("arrows",users)) # лучник

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_berserkers INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,  
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("berserkers",users)) # berserkers

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_tanks INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,   
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("tanks",users)) # tank

cursor.execute("""CREATE TABLE IF NOT EXISTS {0} (
    id_helicopter INT AUTO_INCREMENT PRIMARY KEY,
    count INT,
    last_update INT,  
    new_army_count INT,        
    id_user INT,
    FOREIGN KEY (id_user)  REFERENCES {1}(id_user) ON DELETE CASCADE ON UPDATE CASCADE                   
)""".format("helicopter",users)) # helicopter

#cursor.execute('DELETE FROM people WHERE user_id = %s',('admin'))


# Підтвердження змін
connection.commit()

# Закриття курсора та з'єднання
cursor.close()
connection.close()
