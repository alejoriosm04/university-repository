-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema superstore_sales
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema superstore_sales
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `superstore_sales` DEFAULT CHARACTER SET utf8 ;
USE `superstore_sales` ;

-- -----------------------------------------------------
-- Table `superstore_sales`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`city` (
  `id_city` INT NOT NULL,
  `city_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_city`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`state`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`state` (
  `id_state` INT NOT NULL,
  `state_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_state`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`postal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`postal` (
  `id_postal` INT NOT NULL,
  `postal_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_postal`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`location` (
  `id_location` INT NOT NULL,
  `country` ENUM('United States', 'Canada') NOT NULL,
  `region` ENUM('Central', 'East', 'South', 'West', 'North') NOT NULL,
  `city_idcity` INT NOT NULL,
  `state_idstate` INT NOT NULL,
  `postal_idpostal` INT NOT NULL,
  PRIMARY KEY (`id_location`, `city_idcity`, `state_idstate`, `postal_idpostal`),
  INDEX `fk_location_city1_idx` (`city_idcity` ASC) VISIBLE,
  INDEX `fk_location_state1_idx` (`state_idstate` ASC) VISIBLE,
  INDEX `fk_location_postal1_idx` (`postal_idpostal` ASC) VISIBLE,
  CONSTRAINT `fk_location_city1`
    FOREIGN KEY (`city_idcity`)
    REFERENCES `superstore_sales`.`city` (`id_city`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_location_state1`
    FOREIGN KEY (`state_idstate`)
    REFERENCES `superstore_sales`.`state` (`id_state`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_location_postal1`
    FOREIGN KEY (`postal_idpostal`)
    REFERENCES `superstore_sales`.`postal` (`id_postal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`sale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`sale` (
  `id_sale` INT NOT NULL,
  `sales` FLOAT NOT NULL,
  `quantity` INT NOT NULL,
  `discount` FLOAT NOT NULL,
  `profit` FLOAT NOT NULL,
  `ship_date` DATE NOT NULL,
  `id_location` INT NOT NULL,
  PRIMARY KEY (`id_sale`, `id_location`),
  INDEX `fk_sale_location1_idx` (`id_location` ASC) VISIBLE,
  CONSTRAINT `fk_sale_location1`
    FOREIGN KEY (`id_location`)
    REFERENCES `superstore_sales`.`location` (`id_location`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`customer` (
  `id_customer` INT NOT NULL,
  `customer_name` VARCHAR(45) NULL,
  `segment` ENUM('Consumer', 'Corporate', 'Home Office') NULL,
  PRIMARY KEY (`id_customer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`ship_mode`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`ship_mode` (
  `idship_mode` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idship_mode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`subcategory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`subcategory` (
  `id_subcategory` INT NOT NULL,
  `subcategory_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_subcategory`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`product` (
  `id_product` INT NOT NULL,
  `category` ENUM('Furniture', 'Technology', 'Office Supplies') NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `id_subcategory` INT NOT NULL,
  PRIMARY KEY (`id_product`, `id_subcategory`),
  INDEX `fk_product_subcategory1_idx` (`id_subcategory` ASC) VISIBLE,
  CONSTRAINT `fk_product_subcategory1`
    FOREIGN KEY (`id_subcategory`)
    REFERENCES `superstore_sales`.`subcategory` (`id_subcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `superstore_sales`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `superstore_sales`.`order` (
  `id_customer` INT NOT NULL,
  `id_sale` INT NOT NULL,
  `id_sale_location` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `id_ship_mode` INT NOT NULL,
  `id_product` INT NOT NULL,
  `id_product_subcategory` INT NOT NULL,
  PRIMARY KEY (`id_customer`, `id_sale`, `id_sale_location`, `id_ship_mode`, `id_product`, `id_product_subcategory`),
  INDEX `fk_customer_has_sale_sale1_idx` (`id_sale` ASC, `id_sale_location` ASC) VISIBLE,
  INDEX `fk_customer_has_sale_customer1_idx` (`id_customer` ASC) VISIBLE,
  INDEX `fk_order_ship_mode1_idx` (`id_ship_mode` ASC) VISIBLE,
  INDEX `fk_order_product1_idx` (`id_product` ASC, `id_product_subcategory` ASC) VISIBLE,
  CONSTRAINT `fk_customer_has_sale_customer1`
    FOREIGN KEY (`id_customer`)
    REFERENCES `superstore_sales`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_customer_has_sale_sale1`
    FOREIGN KEY (`id_sale` , `id_sale_location`)
    REFERENCES `superstore_sales`.`sale` (`id_sale` , `id_location`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_ship_mode1`
    FOREIGN KEY (`id_ship_mode`)
    REFERENCES `superstore_sales`.`ship_mode` (`idship_mode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_product1`
    FOREIGN KEY (`id_product` , `id_product_subcategory`)
    REFERENCES `superstore_sales`.`product` (`id_product` , `id_subcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
