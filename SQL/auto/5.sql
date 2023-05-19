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