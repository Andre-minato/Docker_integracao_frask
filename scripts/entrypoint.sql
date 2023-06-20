DROP DATABASE IF EXISTS `teste`;

CREATE DATABASE `teste`;

USE `teste`;


CREATE TABLE `tbl_user`(
      `id` BIGINT NOT NULL AUTO_INCREMENT,
      `user_name` VARCHAR(45) NULL,
      `user_username` VARCHAR(45) NULL,
      `user_password` VARCHAR(45) NULL,
      PRIMARY KEY (id)
);