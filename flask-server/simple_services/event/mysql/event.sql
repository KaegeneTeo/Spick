-- Database: `event`
--
CREATE DATABASE IF NOT EXISTS `events` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `event`;

-- ---------------------------------------------------------------- --
--                              EVENT TABLE                         --
-- ---------------------------------------------------------------- --
DROP TABLE IF EXISTS `events`;
CREATE TABLE IF NOT EXISTS `events` (
    `event_id` INT PRIMARY KEY AUTO_INCREMENT,
    `event_name` varchar(64) NOT NULL,
    `event_desc` varchar(256),
    `start_time` timestamp,
    `end_time` timestamp,
    `time_out` timestamp,
    `event_location` varchar(64),
    `user_id` INT FOREIGN KEY REFERENCES `user`(`user_id`),
)   ENGINE=InnoDB DEFAULT CHARSET=utf8;

