-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2024 at 04:16 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `can_bo_nhan_vien`
--

CREATE TABLE `can_bo_nhan_vien` (
  `ma_can_bo` int(11) NOT NULL,
  `ten_can_bo` varchar(300) NOT NULL,
  `chuc_vu_can_bo` varchar(300) NOT NULL,
  `ma_khoa_phong_ban` int(11) NOT NULL,
  `dien_thoai_can_bo` varchar(300) NOT NULL,
  `email_can_bo` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `hoc_phi`
--

CREATE TABLE `hoc_phi` (
  `id` int(11) NOT NULL,
  `ma_nganh` varchar(45) NOT NULL,
  `gia_tien` int(11) NOT NULL,
  `ma_nam_hoc` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `hoc_phi`
--

INSERT INTO `hoc_phi` (`id`, `ma_nganh`, `gia_tien`, `ma_nam_hoc`) VALUES
(1, 'y-khoa', 44100000, ''),
(2, 'rang-ham-mat', 44100000, ''),
(3, 'duoc-hoc', 44100000, ''),
(4, 'y-hoc-co-truyen', 39200000, ''),
(5, 'y-hoc-du-phong', 39200000, ''),
(6, 'dieu-duong', 39200000, ''),
(7, 'ky-thuat-xet-nghiem-y-hoc', 39200000, ''),
(8, 'ho-sinh', 20400000, ''),
(9, 'ky-thuat-hinh-anh-y-hoc', 20400000, ''),
(10, 'y-te-cong-cong', 20400000, '');

-- --------------------------------------------------------

--
-- Table structure for table `intents`
--

CREATE TABLE `intents` (
  `intent_id` int(11) NOT NULL,
  `intent_name` varchar(255) NOT NULL,
  `status_file` int(11) NOT NULL,
  `selected` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `khoa_phong_ban`
--

CREATE TABLE `khoa_phong_ban` (
  `ma_khoa_phong_ban` int(11) NOT NULL,
  `ten_khoa_phong_ban` varchar(300) NOT NULL,
  `dia_chi_khoa_phong_ban` varchar(300) NOT NULL,
  `dien_thoai_khoa_phong_ban` varchar(300) NOT NULL,
  `email_khoa_phong_ban` varchar(300) NOT NULL,
  `fax` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `khoa_phong_ban`
--

INSERT INTO `khoa_phong_ban` (`ma_khoa_phong_ban`, `ten_khoa_phong_ban`, `dia_chi_khoa_phong_ban`, `dien_thoai_khoa_phong_ban`, `email_khoa_phong_ban`, `fax`) VALUES
(1, 'Phòng Công tác sinh viên ctsv', 'Tầng trệt, Tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3733554', 'ctsv@ctump.edu.vn', ''),
(2, 'Phòng Đào tạo đại học', 'Tầng trệt, Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3 831 531', 'daotao@ctump.edu.vn', ''),
(3, 'Phòng Đào tạo sau đại học', 'Tầng 2, Khu Nhà tròn Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3508917', 'sdh@ctump.edu.vn', ''),
(4, 'Phòng Hành chánh tổng hợp ', 'Tầng trệt, Khu nhà tròn Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3739 730', 'hcth@ctump.edu.vn', ' 0292. 3740 221'),
(5, 'Phòng NCKH-HTQT', 'Tầng 2, Khu Nhà tròn Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3739 809', 'nckh@ctump.edu.vn', ''),
(6, 'Phòng Quản trị thiết bị', 'Tầng 4, Khu nhà tròn Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3600404', 'qttb@ctump.edu.vn', ''),
(7, 'Phòng Tổ chức cán bộ', 'Tầng 3, Khu Nhà tròn Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 379 811', 'tccb@ctump.edu.vn', ''),
(8, 'Quản lý Dự án xây dựng Trường', 'Tầng 1, Khu Nhà tròn tòa nhà Khoa Dược - Răng Hàm Mặt, Trường Đại học Y Dược Cần Thơ', '0292. 3898422', 'qlda@ctump.edu.vn', ''),
(9, 'Phòng Thông tin và Truyền thông', 'Tầng 1, Khoa Điều Dưỡng, Trường Đại học Y Dược Cần Thơ', '0292. 3731 535', 'it@ctump.edu.vn', ''),
(10, 'Phòng Đảm bảo chất lượng', 'Tầng 3, Khu nhà Tròn tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292.3811120', 'dbcl@ctump.edu.vn', ''),
(11, ' Phòng Khảo thí', 'Tầng 4, Tòa Nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', ' 0292. 3508919', 'khaothi@ctump.edu.vn', ''),
(12, 'Phòng Thanh tra - Pháp chế', 'Tầng 4, Tòa Nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '', 'ttpc@ctump.edu.vn', ''),
(13, 'Trung tâm Đào tạo theo nhu cầu xã hội', 'Tầng trệt, Tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292.3508176', 'ttdtlt@ctump.edu.vn', ''),
(14, 'Trung tâm dịch vụ và hỗ trợ sinh viên', 'Tầng trệt, Tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '', 'ttdvhtsv@ctump.edu.vn', ''),
(15, 'Thư viện', 'Tầng 2, Tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3508133', 'thuvien@ctump.edu.vn', ''),
(16, ' Đơn vị HLKN', 'Tầng 3, Tòa nhà khoa Dược - Răng Hàm Mặt, Trường Đại học Y Dược Cần Thơ', '', 'hlkn@ctump.edu.vn', ''),
(17, 'Bệnh viện', '179, Đường Nguyễn Văn Cừ, . An Khánh, Q. Ninh Kiều, Tp. Cần Thơ', '02923 899 444', 'bvdhydcantho@gmail.com', '02923 899 007'),
(18, 'Khoa y', 'Tầng 1, Tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 3830344', 'khoay@ctump.edu.vn', ''),
(19, 'Khoa Dược', 'Tầng 2, Tòa nhà Khoa Răng Hàm Mặt - Dược, Trường Đại học Y Dược Cần Thơ', '0292. 3731257', 'khoaduoc@ctump.edu.vn', ''),
(20, 'Khoa Y tế công cộng', 'Tầng trệt, Tòa nhà Khoa Y tế công cộng, Trường Đại học Y Dược Cần Thơ', '0292. 3730741', 'khoaytcc@ctump.edu.vn', ''),
(21, 'Khoa Điều dưỡng - Kỹ thuật y học', 'Tầng 1, Tòa nhà Khoa Điều Dưỡng - Kỹ thuật y học', '0292. 3897704', 'khoadieuduong@ctump.edu.vn', ''),
(22, 'Khoa Răng Hàm Mặt', 'Tầng 2, Tòa Nhà Răng Hàm Mặt - Dược, Trường Đại học Y Dược Cần Thơ', '0292. 3731 130', 'khoarhm@ctump.edu.vn', ''),
(23, 'Khoa Khoa học cơ bản', 'Tầng trệt, Tòa Nhà Khoa Khoa học cơ bản, Trường Đại học Y Dược Cần Thơ', '0292. 3897703', 'khoakhoahoccoban@ctump.edu.vn', ''),
(24, 'Đảng bộ cơ sở', 'Tầng trệt, Khu nhà tròn tòa nhà Khoa Y, Trường Đại học Y Dược Cần Thơ', '0292. 600376', 'danguy@ctump.edu.vn', ''),
(25, 'Công đoàn', 'Văn phòng Công đoàn, Tòa nhà Khoa Dược, Trường Đại học Y Dược Cần Thơ', '0292. 3739730', 'congdoan@ctump.edu.vn', ''),
(26, 'Đoàn thanh niên - Hội sinh viên', 'Tầng 1, Tòa nhà Khoa Răng Hàm Mặt-Khoa Dược', '02923.733553', 'doantn@ctump.edu.vn', ''),
(27, 'kỹ thuật hình ảnh y học', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật'),
(28, 'hộ sinh', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật'),
(29, 'kỹ thuật xét nghiệm y học', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật'),
(30, 'y học dự phòng', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật', ''),
(31, 'y học cổ truyền', 'đang cập nhật', 'đang cập nhật', 'đang cập nhật', '');

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
-- Indexes for table `can_bo_nhan_vien`
--
ALTER TABLE `can_bo_nhan_vien`
  ADD PRIMARY KEY (`ma_can_bo`),
  ADD KEY `ma_khoa_phong_ban` (`ma_khoa_phong_ban`);

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
  ADD PRIMARY KEY (`id`),
  ADD KEY `ma_nganh` (`ma_nganh`);

--
-- Indexes for table `intents`
--
ALTER TABLE `intents`
  ADD PRIMARY KEY (`intent_id`);

--
-- Indexes for table `khoa_phong_ban`
--
ALTER TABLE `khoa_phong_ban`
  ADD PRIMARY KEY (`ma_khoa_phong_ban`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=305;

--
-- AUTO_INCREMENT for table `can_bo_nhan_vien`
--
ALTER TABLE `can_bo_nhan_vien`
  MODIFY `ma_can_bo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chuong_trinh_dao_tao`
--
ALTER TABLE `chuong_trinh_dao_tao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `example_intent`
--
ALTER TABLE `example_intent`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=351;

--
-- AUTO_INCREMENT for table `hoc_phi`
--
ALTER TABLE `hoc_phi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `intents`
--
ALTER TABLE `intents`
  MODIFY `intent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=241;

--
-- AUTO_INCREMENT for table `khoa_phong_ban`
--
ALTER TABLE `khoa_phong_ban`
  MODIFY `ma_khoa_phong_ban` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

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
-- Constraints for table `can_bo_nhan_vien`
--
ALTER TABLE `can_bo_nhan_vien`
  ADD CONSTRAINT `can_bo_nhan_vien_ibfk_1` FOREIGN KEY (`ma_khoa_phong_ban`) REFERENCES `khoa_phong_ban` (`ma_khoa_phong_ban`);

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

--
-- Constraints for table `hoc_phi`
--
ALTER TABLE `hoc_phi`
  ADD CONSTRAINT `hoc_phi_ibfk_1` FOREIGN KEY (`ma_nganh`) REFERENCES `nganh` (`ma_nganh`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
