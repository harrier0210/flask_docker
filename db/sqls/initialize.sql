CREATE DATABASE IF NOT EXISTS sfor_db;
use sfor_db;

CREATE TABLE `users` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL UNIQUE,
  `password` varchar(60) NOT NULL,
  `jti` varchar(36) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `users` (`name`, `password`) VALUES ('python', '$2a$10$uV4LqxyBTfsS4WUssHf03.at3Ww8518XxMN8bhWFeJe./nZGBrI72');
INSERT INTO `users` (`name`, `password`) VALUES ('aaaa', '$2a$10$uV4LqxyBTfsS4WUssHf03.at3Ww8518XxMN8bhWFeJe./nZGBrI72');
