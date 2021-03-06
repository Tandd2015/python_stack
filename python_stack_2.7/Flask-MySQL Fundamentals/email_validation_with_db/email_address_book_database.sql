-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE='TRADITIONAL, ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `email_address_book_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `email_address_book_db`;

-- -----------------------------------------------------
-- Table `mydb`.`email_addresses`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `email_address_book_db` . `email_addresses` (
	`id` INT NOT NULL AUTO_INCREMENT, 
    `email_address` VARCHAR(255) NULL,
    `created_at` DATETIME NULL,
    `updated_at` DATETIME NULL,
	PRIMARY KEY (`id`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;