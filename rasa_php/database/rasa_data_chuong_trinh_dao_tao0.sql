-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: rasa_data
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chuong_trinh_dao_tao`
--

DROP TABLE IF EXISTS `chuong_trinh_dao_tao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chuong_trinh_dao_tao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ma_nganh` varchar(45) COLLATE utf8mb3_unicode_ci NOT NULL,
  `chuong_trinh_dao_tao` varchar(450) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_nganh_ma_nganh` (`ma_nganh`),
  CONSTRAINT `chuong_trinh_dao_tao_ibfk_1` FOREIGN KEY (`ma_nganh`) REFERENCES `nganh` (`ma_nganh`),
  CONSTRAINT `fk_nganh_ma_nganh` FOREIGN KEY (`ma_nganh`) REFERENCES `nganh` (`ma_nganh`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chuong_trinh_dao_tao`
--

LOCK TABLES `chuong_trinh_dao_tao` WRITE;
/*!40000 ALTER TABLE `chuong_trinh_dao_tao` DISABLE KEYS */;
INSERT INTO `chuong_trinh_dao_tao` VALUES (1,'y-khoa','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9079_Nganh-Y-khoa.pdf'),(2,'rang-ham-mat','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9220_2019.-BAN-MO-TA-CTDT-RHM.pdf'),(3,'y-hoc-co-truyen','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8831_Ban-mo-ta-CTDT-YHCT2019.pdf'),(4,'y-hoc-du-phong','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8819_CTDT-tin-chi-YHDP-2013.pdf'),(5,'dieu-duong','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/3618_1.-DDDK-VLVH-24-11-17.pdf'),(6,'ky-thuat-xet-nghiem-y-hoc','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9218_Mota_CTDT_XN-2019.pdf'),(7,'ho-sinh','Chưa cập nhật'),(8,'y-te-cong-cong','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8801_CTDT-tin-chi-YTCC-2013.pdf'),(9,'ky-thuat-hinh-anh-y-hoc','Chưa cập nhật'),(10,'duoc-hoc','http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/5478_3625_CTDT-tin-chi-Duoc-24-11-17.pdf');
/*!40000 ALTER TABLE `chuong_trinh_dao_tao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-13 16:05:22
