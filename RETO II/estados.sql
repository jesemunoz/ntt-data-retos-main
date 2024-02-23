-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema RETO_ESTADOS
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema RETO_ESTADOS
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `RETO_ESTADOS` ;
USE `RETO_ESTADOS` ;

-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`ESTADOS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`ESTADOS` (
  `idESTADO` INT NOT NULL,
  `NOMBRE` VARCHAR(45) NOT NULL,
  `LATITUD` VARCHAR(500) NOT NULL,
  `LONGITUD` VARCHAR(500) NOT NULL,
  `FECHA_FUNDACION` DATE NOT NULL,
  PRIMARY KEY (`idESTADO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`POBLACIONES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`POBLACIONES` (
  `idPOBLACION` INT NOT NULL,
  `AÑO` YEAR NOT NULL,
  `POBLACION_TOTAL` VARCHAR(45) NOT NULL,
  `idESTADO` INT NOT NULL,
  PRIMARY KEY (`idPOBLACION`),
  INDEX `fk_POBLACIÓNES_copy2_ESTADOS_copy11_idx` (`idESTADO` ASC) VISIBLE,
  CONSTRAINT `fk_POBLACIÓNES_copy2_ESTADOS_copy11`
    FOREIGN KEY (`idESTADO`)
    REFERENCES `RETO_ESTADOS`.`ESTADOS` (`idESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`DEFUNCIONES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`DEFUNCIONES` (
  `idDEFUNCIONES` INT NOT NULL,
  `AÑO` YEAR NOT NULL,
  `DEFUNCIONES_TOTAL` VARCHAR(45) NOT NULL,
  `idESTADO` INT NOT NULL,
  PRIMARY KEY (`idDEFUNCIONES`),
  INDEX `fk_DEFUNCIONES_copy1_ESTADOS_copy11_idx` (`idESTADO` ASC) VISIBLE,
  CONSTRAINT `fk_DEFUNCIONES_copy1_ESTADOS_copy11`
    FOREIGN KEY (`idESTADO`)
    REFERENCES `RETO_ESTADOS`.`ESTADOS` (`idESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RETO_ESTADOS`.`RESIDENTES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RETO_ESTADOS`.`RESIDENTES` (
  `idRESIDENTES` INT NOT NULL,
  `AÑO` YEAR NOT NULL,
  `MENORES_65` VARCHAR(45) NOT NULL,
  `idESTADO` INT NOT NULL,
  PRIMARY KEY (`idRESIDENTES`),
  INDEX `fk_RESIDENTES_copy1_ESTADOS_copy11_idx` (`idESTADO` ASC) VISIBLE,
  CONSTRAINT `fk_RESIDENTES_copy1_ESTADOS_copy11`
    FOREIGN KEY (`idESTADO`)
    REFERENCES `RETO_ESTADOS`.`ESTADOS` (`idESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

SELECT * FROM reto_estados.estados;

INSERT INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('1', 'Alabama', '33.258.882', '-86.829.534', '1819-12-14');
INSERT INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('2', 'Florida', '27.756.767', '-81.463.983', '1845-03-03');
INSERT INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('3', 'Georgia', '32.329.381', '-83.113.737', '1733-02-12');
INSERT INTO `reto_estados`.`estados` (`idESTADO`, `NOMBRE`, `LATITUD`, `LONGITUD`, `FECHA_FUNDACION`) VALUES ('4', 'South Carolina', '33.687.439', '-80.436.374', '1776-03-26');


SELECT * FROM reto_estados.defunciones;
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('1', 2000, '10.622', '1');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('2', 2001, '15.912', '1');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('3', 2000, '38.103', '2');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('4', 2001, '166.069', '2');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('5', 2000, '14.804', '3');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('6', 2001, '15.000', '3');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('7', 2000, '8.581', '4');
INSERT INTO `reto_estados`.`defunciones` (`idDEFUNCIONES`, `AÑO`, `DEFUNCIONES_TOTAL`, `idESTADO`) VALUES ('8', 2001, '9.500', '4');

SELECT * FROM reto_estados.poblaciones;

INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('1', 2000, '4.447.100', '1');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('2', 2001, '4.451.493', '1');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('3', 2000, '15.982.378', '2');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('4', 2001, '17.054.000', '2');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('5', 2000, '8.186.453', '3');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('6', 2001, '8.229.823', '3');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('7', 2000, '4.012.012', '4');
INSERT INTO `reto_estados`.`poblaciones` (`idPOBLACION`, `AÑO`, `POBLACION_TOTAL`, `idESTADO`) VALUES ('8', 2001, '4.023.438', '4');

SELECT * FROM reto_estados.residentes;

INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('1', 2000, '3.870.598', '1');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('2', 2001, '3.880.476', '1');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('3', 2000, '13.237.167', '2');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('4', 2001, '13.548.077', '2');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('5', 2000, '7.440.877', '3');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('6', 2001, '7.582.146', '3');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('7', 2000, '3.535.770', '4');
INSERT INTO `reto_estados`.`residentes` (`idRESIDENTES`, `AÑO`, `MENORES_65`, `idESTADO`) VALUES ('8', 2001, '3.567.172', '4');