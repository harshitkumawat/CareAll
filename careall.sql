-- MySQL dump 10.13  Distrib 8.0.18, for Linux (x86_64)
--
-- Host: localhost    Database: careall
-- ------------------------------------------------------
-- Server version	8.0.18-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hired`
--

DROP TABLE IF EXISTS `hired`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hired` (
  `old_name` char(20) DEFAULT NULL,
  `old_mobile` varchar(10) DEFAULT NULL,
  `young_name` char(20) DEFAULT NULL,
  `young_mobile` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hired`
--

LOCK TABLES `hired` WRITE;
/*!40000 ALTER TABLE `hired` DISABLE KEYS */;
INSERT INTO `hired` VALUES ('Aaditya','8197205950','Aman','9223394455');
/*!40000 ALTER TABLE `hired` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oldfolk`
--

DROP TABLE IF EXISTS `oldfolk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oldfolk` (
  `name` char(15) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `mobile` varchar(10) NOT NULL,
  `address` char(30) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `couple` char(1) DEFAULT NULL,
  `ratings` int(11) DEFAULT NULL,
  `review` char(20) DEFAULT NULL,
  `available` char(1) DEFAULT NULL,
  PRIMARY KEY (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oldfolk`
--

LOCK TABLES `oldfolk` WRITE;
/*!40000 ALTER TABLE `oldfolk` DISABLE KEYS */;
INSERT INTO `oldfolk` VALUES ('Yogita',60,'F','1234567890','Mumbai',10000,'N',0,'','Y'),('Bhoomi',70,'F','7043377227','Chennai',15000,'N',0,'','Y'),('Aaditya',68,'M','8197205950','Bangalore',12000,'Y',0,'','N'),('Kishan',75,'M','8310440109','Hyderabad',20000,'Y',0,'','Y');
/*!40000 ALTER TABLE `oldfolk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `young_name` char(20) DEFAULT NULL,
  `young_mobile` varchar(10) DEFAULT NULL,
  `old_name` char(20) DEFAULT NULL,
  `old_mobile` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `youngfolk`
--

DROP TABLE IF EXISTS `youngfolk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `youngfolk` (
  `name` char(15) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `mobile` varchar(10) NOT NULL,
  `address` char(30) DEFAULT NULL,
  `ratings` int(11) DEFAULT NULL,
  `review` char(20) DEFAULT NULL,
  `descr` char(30) DEFAULT NULL,
  `available` char(1) DEFAULT NULL,
  `track` int(11) DEFAULT NULL,
  PRIMARY KEY (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `youngfolk`
--

LOCK TABLES `youngfolk` WRITE;
/*!40000 ALTER TABLE `youngfolk` DISABLE KEYS */;
INSERT INTO `youngfolk` VALUES ('Aman',22,'M','9223394455','Mumbai',0,'','Attentiveness','Y',1),('Prajakta',24,'F','9876543000','Hyderabad',0,'','Patience,Attentiveness.','Y',0),('Shiwangi',24,'F','9876543200','Chennai',0,'','Compassion','Y',0),('Harshit',21,'M','9876543210','Bangalore',0,'','Compassion, Patience.','Y',0);
/*!40000 ALTER TABLE `youngfolk` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-03 22:51:24
