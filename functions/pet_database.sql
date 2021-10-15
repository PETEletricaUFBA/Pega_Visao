CREATE DATABASE if not exists `pet_database`;
USE `pet_database`;
CREATE TABLE if not exists `petian` (
    -- Geral
    `pet_id` int AUTO_INCREMENT,
    `name_pet` varchar(20),
    `surname_pet` varchar(20),
    -- PET STATUS
    `status_pet` BOOL DEFAULT 1,
    `cod_RFID` int,
    PRIMARY KEY (`pet_id`)
);
