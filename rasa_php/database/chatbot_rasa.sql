-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2024 at 05:49 AM
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
-- Table structure for table `chuong_trinh_dao_tao`
--

CREATE TABLE `chuong_trinh_dao_tao` (
  `id` int(11) NOT NULL,
  `ma_nganh` varchar(45) NOT NULL,
  `chuong_trinh_dao_tao` varchar(450) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chuong_trinh_dao_tao`
--

INSERT INTO `chuong_trinh_dao_tao` (`id`, `ma_nganh`, `chuong_trinh_dao_tao`) VALUES
(1, 'y-khoa', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9079_Nganh-Y-khoa.pdf'),
(2, 'rang-ham-mat', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9220_2019.-BAN-MO-TA-CTDT-RHM.pdf'),
(3, 'y-hoc-co-truyen', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8831_Ban-mo-ta-CTDT-YHCT2019.pdf'),
(4, 'y-hoc-du-phong', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8819_CTDT-tin-chi-YHDP-2013.pdf'),
(5, 'dieu-duong', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/3618_1.-DDDK-VLVH-24-11-17.pdf'),
(6, 'ky-thuat-xet-nghiem-y-hoc', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9218_Mota_CTDT_XN-2019.pdf'),
(7, 'ho-sinh', 'Chưa cập nhật'),
(8, 'y-te-cong-cong', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8801_CTDT-tin-chi-YTCC-2013.pdf'),
(9, 'ky-thuat-hinh-anh-y-hoc', 'Chưa cập nhật'),
(10, 'duoc-hoc', 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/5478_3625_CTDT-tin-chi-Duoc-24-11-17.pdf');

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
-- Table structure for table `hoc_phi`
--

CREATE TABLE `hoc_phi` (
  `id` int(11) NOT NULL,
  `ma_nganh` varchar(45) NOT NULL,
  `gia_tien` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `hoc_phi`
--

INSERT INTO `hoc_phi` (`id`, `ma_nganh`, `gia_tien`) VALUES
(1, 'y-khoa', 44100000),
(2, 'rang-ham-mat', 44100000),
(3, 'duoc-hoc', 44100000),
(4, 'y-hoc-co-truyen', 39200000),
(5, 'y-hoc-du-phong', 39200000),
(6, 'dieu-duong', 39200000),
(7, 'ky-thuat-xet-nghiem-y-hoc', 39200000),
(8, 'ho-sinh', 20400000),
(9, 'ky-thuat-hinh-anh-y-hoc', 20400000),
(10, 'y-te-cong-cong', 20400000);

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

-- --------------------------------------------------------

--
-- Table structure for table `nganh`
--

CREATE TABLE `nganh` (
  `id` int(11) NOT NULL,
  `ma_nganh` varchar(45) DEFAULT NULL,
  `ten_nganh` varchar(450) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `nganh`
--

INSERT INTO `nganh` (`id`, `ma_nganh`, `ten_nganh`) VALUES
(1, 'y-khoa', 'Y Khoa'),
(2, 'y-hoc-co-truyen', 'Y học cổ truyền'),
(3, 'rang-ham-mat', 'Răng hàm mặt'),
(4, 'duoc-hoc', 'Dược học'),
(5, 'y-hoc-du-phong', 'Y học dụ phòng'),
(6, 'dieu-duong', 'Điều dưỡng'),
(7, 'ky-thuat-xet-nghiem-y-hoc', 'Kỹ thuật xét nghiệm y học'),
(8, 'ho-sinh', 'Hộ sinh'),
(9, 'ky-thuat-hinh-anh-y-hoc', 'Kỹ thuật hình ảnh y học'),
(10, 'y-te-cong-cong', 'Y tế công cộng');

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
-- Indexes for table `chuong_trinh_dao_tao`
--
ALTER TABLE `chuong_trinh_dao_tao`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_nganh_ma_nganh` (`ma_nganh`);

--
-- Indexes for table `example_intent`
--
ALTER TABLE `example_intent`
  ADD PRIMARY KEY (`id`),
  ADD KEY `intent_id` (`intent_id`);

--
-- Indexes for table `hoc_phi`
--
ALTER TABLE `hoc_phi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `intents`
--
ALTER TABLE `intents`
  ADD PRIMARY KEY (`intent_id`);

--
-- Indexes for table `nganh`
--
ALTER TABLE `nganh`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ma_nganh_index` (`ma_nganh`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answer_intent`
--
ALTER TABLE `answer_intent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=273;

--
-- AUTO_INCREMENT for table `chuong_trinh_dao_tao`
--
ALTER TABLE `chuong_trinh_dao_tao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `example_intent`
--
ALTER TABLE `example_intent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=318;

--
-- AUTO_INCREMENT for table `hoc_phi`
--
ALTER TABLE `hoc_phi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `intents`
--
ALTER TABLE `intents`
  MODIFY `intent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202;

--
-- AUTO_INCREMENT for table `nganh`
--
ALTER TABLE `nganh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answer_intent`
--
ALTER TABLE `answer_intent`
  ADD CONSTRAINT `answer_intent_ibfk_1` FOREIGN KEY (`intent_id`) REFERENCES `intents` (`intent_id`);

--
-- Constraints for table `chuong_trinh_dao_tao`
--
ALTER TABLE `chuong_trinh_dao_tao`
  ADD CONSTRAINT `chuong_trinh_dao_tao_ibfk_1` FOREIGN KEY (`ma_nganh`) REFERENCES `nganh` (`ma_nganh`),
  ADD CONSTRAINT `fk_nganh_ma_nganh` FOREIGN KEY (`ma_nganh`) REFERENCES `nganh` (`ma_nganh`);

--
-- Constraints for table `example_intent`
--
ALTER TABLE `example_intent`
  ADD CONSTRAINT `example_intent_ibfk_1` FOREIGN KEY (`intent_id`) REFERENCES `intents` (`intent_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
