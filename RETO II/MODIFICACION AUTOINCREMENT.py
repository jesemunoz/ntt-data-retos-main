# Conectar con BBDD
import mysql.connector

conexion = mysql.connector.connect(host="localhost", user="root", password="", database="")

# Crear cursor
cursor = conexion.cursor()

# Ejecutar código SQL
sql = """
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema RETO_ESTADOS
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `RETO_ESTADOS`;
USE `RETO_ESTADOS`;

-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`ESTADOS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`ESTADOS` (
  `idESTADO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NOT NULL,
  `LATITUD` VARCHAR(500) NOT NULL,
  `LONGITUD` VARCHAR(500) NOT NULL,
  `FECHA_FUNDACION` DATE NOT NULL,
  PRIMARY KEY (`idESTADO`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`POBLACIONES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`POBLACIONES` (
  `idPOBLACION` INT NOT NULL AUTO_INCREMENT,
  `AÑO` YEAR NOT NULL,
  `POBLACION_TOTAL` VARCHAR(45) NOT NULL,
  `idESTADO` INT NOT NULL,
  PRIMARY KEY (`idPOBLACION`),
  FOREIGN KEY (`idESTADO`)
    REFERENCES `RETO_ESTADOS`.`ESTADOS` (`idESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`DEFUNCIONES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`DEFUNCIONES` (
  `idDEFUNCIONES` INT NOT NULL AUTO_INCREMENT,
  `AÑO` YEAR NOT NULL,
  `DEFUNCIONES_TOTAL` VARCHAR(45) NOT NULL,
  `idESTADO` INT NOT NULL,
  PRIMARY KEY (`idDEFUNCIONES`),
  FOREIGN KEY (`idESTADO`)
    REFERENCES `RETO_ESTADOS`.`ESTADOS` (`idESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`RESIDENTES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`RESIDENTES` (
  `idRESIDENTES` INT NOT NULL AUTO_INCREMENT,
  `AÑO` YEAR NOT NULL,
  `MENORES_65` VARCHAR(45) NOT NULL,
  `idESTADO` INT NOT NULL,
  PRIMARY KEY (`idRESIDENTES`),
  FOREIGN KEY (`idESTADO`)
    REFERENCES `RETO_ESTADOS`.`ESTADOS` (`idESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;
"""

# Dividir el código SQL en consultas individuales
queries = sql.split(';')

# Ejecutar cada consulta individualmente
for query in queries:
    cursor.execute(query)

# Cerrar la conexión
conexion.close()
