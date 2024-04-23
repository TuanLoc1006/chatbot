-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2024 at 02:53 PM
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
(135, 75, 'dhct', 0),
(137, 77, 'sao ban vui the', 0);

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
(164, 75, 'ctu viet tat la gi', 0),
(165, 77, 'hom nay vui qua', 0);

-- --------------------------------------------------------

--
-- Table structure for table `intents`
--

CREATE TABLE `intents` (
  `intent_id` int(11) NOT NULL,
  `intent_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `intents`
--

INSERT INTO `intents` (`intent_id`, `intent_name`) VALUES
(75, 'ctu'),
(77, 'happy');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=138;

--
-- AUTO_INCREMENT for table `example_intent`
--
ALTER TABLE `example_intent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=166;

--
-- AUTO_INCREMENT for table `intents`
--
ALTER TABLE `intents`
  MODIFY `intent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

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
