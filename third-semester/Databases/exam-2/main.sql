-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema exam-2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema exam-2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `exam-2` DEFAULT CHARACTER SET utf8 ;
USE `exam-2` ;

-- -----------------------------------------------------
-- Table `exam-2`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`city` (
  `id_city` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_city`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exam-2`.`location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`location` (
  `id_location` INT NOT NULL,
  `city_id_city` INT NOT NULL,
  `state` ENUM('Tamil Nadu') NOT NULL,
  `region` ENUM('North', 'West', 'East', 'South', 'Central') NOT NULL,
  PRIMARY KEY (`id_location`, `city_id_city`),
  INDEX `fk_location_city_idx` (`city_id_city` ASC) VISIBLE,
  CONSTRAINT `fk_location_city`
    FOREIGN KEY (`city_id_city`)
    REFERENCES `exam-2`.`city` (`id_city`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exam-2`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`customer` (
  `id_customer` INT NOT NULL,
  `customer_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_customer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exam-2`.`sale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`sale` (
  `id_sale` INT NOT NULL,
  `discount` FLOAT NOT NULL,
  `sales` INT NOT NULL,
  `profit` FLOAT NOT NULL,
  PRIMARY KEY (`id_sale`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exam-2`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`category` (
  `id_category` INT NOT NULL,
  `category_name` ENUM('Bakery', 'Beverages', 'Eggs, Meat & Fish', 'Food Grains', 'Fruits & Veggies', 'Oil & Masala', 'Snacks') NOT NULL,
  PRIMARY KEY (`id_category`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exam-2`.`subcategory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`subcategory` (
  `id_subcategory` INT NOT NULL,
  `subcategory_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_subcategory`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `exam-2`.`order_sale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `exam-2`.`order_sale` (
  `id_order` VARCHAR(45) NOT NULL,
  `customer_id_customer` INT NOT NULL,
  `sale_id_sale` INT NOT NULL,
  `category_id_category` INT NOT NULL,
  `subcategory_id_subcategory` INT NOT NULL,
  `location_id_location` INT NOT NULL,
  `location_city_id_city` INT NOT NULL,
  `order_date` DATE NULL,
  PRIMARY KEY (`id_order`, `customer_id_customer`, `sale_id_sale`, `category_id_category`, `subcategory_id_subcategory`, `location_id_location`, `location_city_id_city`),
  INDEX `fk_sale_has_customer_customer1_idx` (`customer_id_customer` ASC) VISIBLE,
  INDEX `fk_sale_has_customer_sale1_idx` (`sale_id_sale` ASC) VISIBLE,
  INDEX `fk_order_category1_idx` (`category_id_category` ASC) VISIBLE,
  INDEX `fk_order_location1_idx` (`location_id_location` ASC, `location_city_id_city` ASC) VISIBLE,
  INDEX `fk_order_sale_subcategory1_idx` (`subcategory_id_subcategory` ASC) VISIBLE,
  CONSTRAINT `fk_sale_has_customer_sale1`
    FOREIGN KEY (`sale_id_sale`)
    REFERENCES `exam-2`.`sale` (`id_sale`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sale_has_customer_customer1`
    FOREIGN KEY (`customer_id_customer`)
    REFERENCES `exam-2`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_category1`
    FOREIGN KEY (`category_id_category`)
    REFERENCES `exam-2`.`category` (`id_category`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_location1`
    FOREIGN KEY (`location_id_location` , `location_city_id_city`)
    REFERENCES `exam-2`.`location` (`id_location` , `city_id_city`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_sale_subcategory1`
    FOREIGN KEY (`subcategory_id_subcategory`)
    REFERENCES `exam-2`.`subcategory` (`id_subcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
