# Задание

1. Создать таблицу авто:
    ```SQL
    CREATE TABLE Avto (
      AvtoID INTEGER PRIMARY KEY, 
      CarBrand VARCHAR(255) NOT NULL, 
      Model VARCHAR(255) NOT NULL, 
      YearOfRelease INTEGER NOT NULL, 
      Price INTEGER NOT NULL
    ); 
    ```
    
    
2. Заполнить таблицу Auto 10 записями:
    ```SQL
    INSERT INTO Avto (
      CarBrand, Model, YearOfRelease, Price
    ) 
    VALUES 
      ('Toyota', 'Prius', 2000, 500000), 
      ('BMW', 'x5', 2010, 1000000), 
      ('Audi', 'f3', 2014, 1450000), 
      ('Toyota', 'Camry', 2004, 800000), 
      ('Mercedes', 'S-class', 2015, 6000000), 
      ('Nissan', 'Murano', 2018, 4000000), 
      ('Hyundai', 'Tucson', 2005, 900000), 
      ('Audi', 'A8', 2008, 700000), 
      ('Mazda', 'RX-8', 2015, 800000), 
      ('Toyota', 'Corolla', 2010, 550000)
    ```   
    Результат: 
    | AvtoID | CarBrand |  Model  | YearOfRelease |  Price  |
    |:------:|:--------:|:-------:|:-------------:|:-------:|
    | 1      | Toyota   | Prius   | 2000          | 500000  |
    | 2      | BMW      | x5      | 2010          | 1000000 |
    | 3      | Audi     | f3      | 2014          | 1450000 |
    | 4      | Toyota   | Camry   | 2004          | 800000  |
    | 5      | Mercedes | S-class | 2015          | 6000000 |
    | 6      | Nissan   | Murano  | 2018          | 4000000 |
    | 7      | Hyundai  | Tucson  | 2005          | 900000  |
    | 8      | Audi     | A8      | 2008          | 700000  |
    | 9      | Mazda    | RX-8    | 2015          | 800000  |
    | 10     | Toyota   | Corolla | 2010          | 550000  |
    
    
3. Создать запрос по выдаче авто только марки Toyota:
    ```SQL
    SELECT 
      * 
    FROM 
      Avto 
    WHERE 
      CarBrand = 'Toyota';
    ```
    Результат: 
    | AvtoID | CarBrand |  Model  | YearOfRelease | Price  |
    |:------:|:--------:|:-------:|:-------------:|:------:|
    | 1      | Toyota   | Prius   | 2000          | 500000 |
    | 4      | Toyota   | Camry   | 2004          | 800000 |
    | 10     | Toyota   | Corolla | 2010          | 550000 |
    
    
4. Создать запрос по выдаче последних 3 авто:
    ```SQL
    SELECT 
      * 
    FROM 
      Avto 
    ORDER By 
      AvtoID DESC 
    LIMIT 
      3;
     ```
    Результат: 
    | AvtoID | CarBrand |  Model  | YearOfRelease | Price  |
    |:------:|:--------:|:-------:|:-------------:|:------:|
    | 10     | Toyota   | Corolla | 2010          | 550000 |
    | 9      | Mazda    | RX-8    | 2015          | 800000 |
    | 8      | Audi     | A8      | 2008          | 700000 |
    
    
5. Создать запрос по выдаче самого дорого авто:
    ```SQL
    SELECT 
      * 
    FROM 
      Avto 
    WHERE 
      Price =(
        SELECT 
          max(Price) 
        FROM 
          Avto
      );
    ```
    Результат: 
    | AvtoID | CarBrand |  Model  | YearOfRelease |  Price  |
    |:------:|:--------:|:-------:|:-------------:|:-------:|
    | 5      | Mercedes | S-class | 2015          | 6000000 |
    
    
6. Создать запрос по выдаче самого старого авто:
    ```SQL
    SELECT 
      * 
    FROM 
      Avto 
    WHERE 
      YearOfRelease =(
        SELECT 
          min(YearOfRelease) 
        FROM 
          Avto
      );
    ```
    Результат: 
    | AvtoID | CarBrand | Model | YearOfRelease | Price  |
    |:------:|:--------:|:-----:|:-------------:|:------:|
    | 1      | Toyota   | Prius | 2000          | 500000 |
    
    
7. Создать запрос по выдаче авто стоимостью более 1 000 000 рублей и более:
    ```SQL
    SELECT 
      * 
    FROM 
      Avto 
    WHERE 
      Price >= 1000000;
    ```
    Результат: 
    | AvtoID | CarBrand |  Model  | YearOfRelease |  Price  |
    |:------:|:--------:|:-------:|:-------------:|:-------:|
    | 2      | BMW      | x5      | 2010          | 1000000 |
    | 3      | Audi     | f3      | 2014          | 1450000 |
    | 5      | Mercedes | S-class | 2015          | 6000000 |
    | 6      | Nissan   | Murano  | 2018          | 4000000 |
    