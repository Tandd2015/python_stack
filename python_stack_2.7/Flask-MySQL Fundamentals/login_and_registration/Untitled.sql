-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Log
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Log
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Log` DEFAULT CHARACTER SET utf8 ;
USE `Log` ;

-- -----------------------------------------------------
-- Table `Log`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Log`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email_address` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `salt` VARCHAR(255) NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
