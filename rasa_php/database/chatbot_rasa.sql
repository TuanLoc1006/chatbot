-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2024 at 04:08 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatbot_rasa`
--

-- --------------------------------------------------------

--
-- Table structure for table `answer_intent`
--

CREATE TABLE `answer_intent` (
  `id` int(11) NOT NULL,
  `intent_id` int(11) NOT NULL,
  `chat_answer` text NOT NULL,
  `status_file` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `answer_intent`
--

INSERT INTO `answer_intent` (`id`, `intent_id`, `chat_answer`, `status_file`) VALUES
(268, 199, 'ths khoa', 1),
(269, 199, 'khoa, bình', 1),
(270, 200, 'đường nvc', 1),
(271, 201, 'lộc', 1),
(272, 200, 'nvc', 1);

-- --------------------------------------------------------

--
-- Table structure for table `example_intent`
--

CREATE TABLE `example_intent` (
  `id` int(11) NOT NULL,
  `intent_id` int(11) NOT NULL,
  `example_question` text NOT NULL,
  `status_file` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `example_intent`
--

INSERT INTO `example_intent` (`id`, `intent_id`, `example_question`, `status_file`) VALUES
(313, 199, 'ai là trưởng phòng', 1),
(314, 199, 'ai quản lý', 1),
(315, 200, 'ctump ở đường nào', 1),
(316, 201, 'ai là hiệu trưởng', 1),
(317, 200, 'địa chỉ ctump', 1);

-- --------------------------------------------------------

--
-- Table structure for table `intents`
--

CREATE TABLE `intents` (
  `intent_id` int(11) NOT NULL,
  `intent_name` varchar(255) NOT NULL,
  `status_file` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `intents`
--

INSERT INTO `intents` (`intent_id`, `intent_name`, `status_file`) VALUES
(199, 'phòng truyền thông', 1),
(200, 'địa chỉ ctump', 1),
(201, 'hieu_truong_ctump', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answer_intent`
--
ALTER TABLE `answer_intent`
  ADD PRIMARY KEY (`id`),
  ADD KEY `intent_id` (`intent_id`);

--
-- Indexes for table `example_intent`
--
ALTER TABLE `example_intent`
  ADD PRIMARY KEY (`id`),
  ADD KEY `intent_id` (`intent_id`);

--
-- Indexes for table `intents`
--
ALTER TABLE `intents`
  ADD PRIMARY KEY (`intent_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answer_intent`
--
ALTER TABLE `answer_intent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=273;

--
-- AUTO_INCREMENT for table `example_intent`
--
ALTER TABLE `example_intent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=318;

--
-- AUTO_INCREMENT for table `intents`
--
ALTER TABLE `intents`
  MODIFY `intent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answer_intent`
--
ALTER TABLE `answer_intent`
  ADD CONSTRAINT `answer_intent_ibfk_1` FOREIGN KEY (`intent_id`) REFERENCES `intents` (`intent_id`);

--
-- Constraints for table `example_intent`
--
ALTER TABLE `example_intent`
  ADD CONSTRAINT `example_intent_ibfk_1` FOREIGN KEY (`intent_id`) REFERENCES `intents` (`intent_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
