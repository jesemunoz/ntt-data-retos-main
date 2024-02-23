#Conectar con BBDD
import mysql.connector

conexion=mysql.connector.connect(host="localhost", user="root", password="", database="reto_estados")

#Crear cursor
cursor = conexion.cursor()

#Ejecutar código SQL
cursor.execute("SET @OLD_SQL_MODE=@@SQL_MODE")
cursor.execute("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS")
cursor.execute("SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS")

cursor.execute("SET SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'")
cursor.execute("SET FOREIGN_KEY_CHECKS=0")
cursor.execute("SET UNIQUE_CHECKS=0")

cursor.execute("SELECT * FROM reto_estados.estados")
result = cursor.fetchall()
for row in result:
    print(row)


cursor.execute("INSERT IGNORE INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('1', 'Alabama', '33.258.882', '-86.829.534', '1819-12-14')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('2', 'Florida', '27.756.767', '-81.463.983', '1845-03-03')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('3', 'Georgia', '32.329.381', '-83.113.737', '1733-02-12')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('4', 'South Carolina', '33.687.439', '-80.436.374', '1776-03-26')")
conexion.commit()

cursor.execute("SELECT * FROM reto_estados.defunciones")
result = cursor.fetchall()
for row in result:
    print(row)
    
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('1', 2000, '10.622', '1')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('2', 2001, '15.912', '1')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('3', 2000, '38.103', '2')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('4', 2001, '166.069', '2')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('5', 2000, '14.804', '3')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('6', 2001, '15.000', '3')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('7', 2000, '8.581', '4')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('8', 2001, '9.500', '4')")
conexion.commit()

cursor.execute("SELECT * FROM reto_estados.poblaciones")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('1', 2000, '4.447.100', '1')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('2', 2001, '4.451.493', '1')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('3', 2000, '15.982.378', '2')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('4', 2001, '17.054.000', '2')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('5', 2000, '8.186.453', '3')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('6', 2001, '8.229.823', '3')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('7', 2000, '4.012.012', '4')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('8', 2001, '4.023.438', '4')")
conexion.commit()

cursor.execute("SELECT * FROM reto_estados.residentes")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('1', 2000, '3.870.598', '1')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('2', 2001, '3.880.476', '1')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('3', 2000, '13.237.167', '2')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('4', 2001, '13.548.077', '2')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('5', 2000, '7.440.877', '3')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('6', 2001, '7.582.146', '3')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('7', 2000, '3.535.770', '4')")
cursor.execute("INSERT IGNORE INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('8', 2001, '3.567.172', '4')")
conexion.commit()
    
# Cerrar la conexión
conexion.close()
