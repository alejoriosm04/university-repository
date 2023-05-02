-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema aerotrack-reto
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema aerotrack-reto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aerotrack-reto` DEFAULT CHARACTER SET utf8 ;
USE `aerotrack-reto` ;

-- -----------------------------------------------------
-- Table `aerotrack-reto`.`aerolinea`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`aerolinea` (
  `codigo_IATA_aerolinea` VARCHAR(45) NOT NULL,
  `nombre_aerolinea` VARCHAR(127) NOT NULL,
  PRIMARY KEY (`codigo_IATA_aerolinea`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aerotrack-reto`.`pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`pais` (
  `id_pais` VARCHAR(45) NOT NULL,
  `nombre_pais` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_pais`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aerotrack-reto`.`ciudad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`ciudad` (
  `id_ciudad` VARCHAR(45) NOT NULL,
  `nombre_ciudad` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_ciudad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aerotrack-reto`.`aeropuerto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`aeropuerto` (
  `codigo_IATA_aeropuerto` VARCHAR(45) NOT NULL,
  `nombre_aeropuerto` VARCHAR(127) NOT NULL,
  `id_pais_aeropuerto` VARCHAR(45) NOT NULL,
  `id_ciudad_aeropuerto` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`codigo_IATA_aeropuerto`, `id_pais_aeropuerto`, `id_ciudad_aeropuerto`),
  INDEX `fk_aeropuerto_pais_idx` (`id_pais_aeropuerto` ASC) VISIBLE,
  INDEX `fk_aeropuerto_ciudad1_idx` (`id_ciudad_aeropuerto` ASC) VISIBLE,
  CONSTRAINT `fk_aeropuerto_pais`
    FOREIGN KEY (`id_pais_aeropuerto`)
    REFERENCES `aerotrack-reto`.`pais` (`id_pais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_aeropuerto_ciudad1`
    FOREIGN KEY (`id_ciudad_aeropuerto`)
    REFERENCES `aerotrack-reto`.`ciudad` (`id_ciudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aerotrack-reto`.`vuelo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`vuelo` (
  `id_vuelo` VARCHAR(45) NOT NULL,
  `codigo_IATA_aerolinea_vuelo` VARCHAR(45) NOT NULL,
  `codigo_IATA_aeropuerto_salida` VARCHAR(45) NOT NULL,
  `codigo_IATA_aeropuerto_llegada` VARCHAR(45) NOT NULL,
  `id_pais_aeropuerto_salida` VARCHAR(45) NOT NULL,
  `id_pais_aeropuerto_llegada` VARCHAR(45) NOT NULL,
  `id_ciudad_aeropuerto_salida` VARCHAR(45) NOT NULL,
  `id_ciudad_aeropuerto_llegada` VARCHAR(45) NOT NULL,
  `fecha_salida_vuelo` DATETIME NOT NULL,
  `fecha_llegada_vuelo` DATETIME NOT NULL,
  `categoria_vuelo` ENUM('National Flight', 'International Flight', 'Regional Flight') NOT NULL,
  PRIMARY KEY (`id_vuelo`, `codigo_IATA_aerolinea_vuelo`, `codigo_IATA_aeropuerto_salida`, `codigo_IATA_aeropuerto_llegada`, `id_pais_aeropuerto_salida`, `id_pais_aeropuerto_llegada`, `id_ciudad_aeropuerto_salida`, `id_ciudad_aeropuerto_llegada`),
  INDEX `fk_vuelo_aerolinea1_idx` (`codigo_IATA_aerolinea_vuelo` ASC) VISIBLE,
  INDEX `fk_vuelo_aeropuerto1_idx` (`codigo_IATA_aeropuerto_salida` ASC, `id_pais_aeropuerto_salida` ASC, `id_ciudad_aeropuerto_salida` ASC) VISIBLE,
  INDEX `fk_vuelo_aeropuerto2_idx` (`codigo_IATA_aeropuerto_llegada` ASC, `id_pais_aeropuerto_llegada` ASC, `id_ciudad_aeropuerto_llegada` ASC) VISIBLE,
  CONSTRAINT `fk_vuelo_aerolinea1`
    FOREIGN KEY (`codigo_IATA_aerolinea_vuelo`)
    REFERENCES `aerotrack-reto`.`aerolinea` (`codigo_IATA_aerolinea`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_aeropuerto1`
    FOREIGN KEY (`codigo_IATA_aeropuerto_salida` , `id_pais_aeropuerto_salida` , `id_ciudad_aeropuerto_salida`)
    REFERENCES `aerotrack-reto`.`aeropuerto` (`codigo_IATA_aeropuerto` , `id_pais_aeropuerto` , `id_ciudad_aeropuerto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_aeropuerto2`
    FOREIGN KEY (`codigo_IATA_aeropuerto_llegada` , `id_pais_aeropuerto_llegada` , `id_ciudad_aeropuerto_llegada`)
    REFERENCES `aerotrack-reto`.`aeropuerto` (`codigo_IATA_aeropuerto` , `id_pais_aeropuerto` , `id_ciudad_aeropuerto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aerotrack-reto`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`cliente` (
  `id_cliente` INT NOT NULL,
  `nombre_cliente` VARCHAR(127) NOT NULL,
  `edad` INT NOT NULL,
  `email_cliente` VARCHAR(127) NULL,
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aerotrack-reto`.`tiquete_vuelo_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aerotrack-reto`.`tiquete_vuelo_cliente` (
  `id_tiquete` VARCHAR(45) NOT NULL,
  `id_vuelo_tiquete` VARCHAR(45) NOT NULL,
  `codigo_IATA_aerolinea_vuelo_tiquete` VARCHAR(45) NOT NULL,
  `codigo_IATA_aeropuerto_salida_tiquete` VARCHAR(45) NOT NULL,
  `codigo_IATA_aeropuerto_llegada_tiquete` VARCHAR(45) NOT NULL,
  `id_pais_aeropuerto_salida_tiquete` VARCHAR(45) NOT NULL,
  `id_pais_aeropuerto_llegada_tiquete` VARCHAR(45) NOT NULL,
  `id_ciudad_aeropuerto_salida_tiquete` VARCHAR(45) NOT NULL,
  `id_ciudad_aeropuerto_llegada_tiquete` VARCHAR(45) NOT NULL,
  `id_cliente` INT NOT NULL,
  `grupo` ENUM('A', 'B', 'C', 'D') NOT NULL,
  `asiento` VARCHAR(45) NOT NULL,
  `categoria_pasajero` ENUM('First Class', 'Business Class', 'Low Class', 'Premium Low Class') NOT NULL,
  `equipaje_mano` FLOAT NULL,
  `equipaje_bodega` FLOAT NULL,
  PRIMARY KEY (`id_tiquete`, `id_vuelo_tiquete`, `codigo_IATA_aerolinea_vuelo_tiquete`, `codigo_IATA_aeropuerto_salida_tiquete`, `codigo_IATA_aeropuerto_llegada_tiquete`, `id_pais_aeropuerto_salida_tiquete`, `id_pais_aeropuerto_llegada_tiquete`, `id_ciudad_aeropuerto_salida_tiquete`, `id_ciudad_aeropuerto_llegada_tiquete`, `id_cliente`),
  INDEX `fk_vuelo_has_cliente_cliente1_idx` (`id_cliente` ASC) VISIBLE,
  INDEX `fk_vuelo_has_cliente_vuelo1_idx` (`id_vuelo_tiquete` ASC, `codigo_IATA_aerolinea_vuelo_tiquete` ASC, `codigo_IATA_aeropuerto_salida_tiquete` ASC, `codigo_IATA_aeropuerto_llegada_tiquete` ASC, `id_pais_aeropuerto_salida_tiquete` ASC, `id_pais_aeropuerto_llegada_tiquete` ASC, `id_ciudad_aeropuerto_salida_tiquete` ASC, `id_ciudad_aeropuerto_llegada_tiquete` ASC) VISIBLE,
  CONSTRAINT `fk_vuelo_has_cliente_vuelo1`
    FOREIGN KEY (`id_vuelo_tiquete` , `codigo_IATA_aerolinea_vuelo_tiquete` , `codigo_IATA_aeropuerto_salida_tiquete` , `codigo_IATA_aeropuerto_llegada_tiquete` , `id_pais_aeropuerto_salida_tiquete` , `id_pais_aeropuerto_llegada_tiquete` , `id_ciudad_aeropuerto_salida_tiquete` , `id_ciudad_aeropuerto_llegada_tiquete`)
    REFERENCES `aerotrack-reto`.`vuelo` (`id_vuelo` , `codigo_IATA_aerolinea_vuelo` , `codigo_IATA_aeropuerto_salida` , `codigo_IATA_aeropuerto_llegada` , `id_pais_aeropuerto_salida` , `id_pais_aeropuerto_llegada` , `id_ciudad_aeropuerto_salida` , `id_ciudad_aeropuerto_llegada`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_has_cliente_cliente1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `aerotrack-reto`.`cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
