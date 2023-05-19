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