-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: exam-2
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id_customer` int NOT NULL,
  `customer_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_customer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Harish'),(2,'Sudha'),(3,'Hussain'),(4,'Jackson'),(5,'Ridhesh'),(6,'Adavan'),(7,'Jonas'),(8,'Hafiz'),(9,'Krithika'),(10,'Ganesh'),(11,'Yadav'),(12,'Sharon'),(13,'Peer'),(14,'Sundar'),(15,'Ramesh'),(16,'Alan'),(17,'Arutra'),(18,'Haseena'),(19,'Verma'),(20,'Muneer'),(21,'Veronica'),(22,'Shah'),(23,'Mathew'),(24,'Akash'),(25,'Anu'),(26,'Sabeela'),(27,'James'),(28,'Willams'),(29,'Malik'),(30,'Amrish'),(31,'Vince'),(32,'Suresh'),(33,'Esther'),(34,'Yusuf'),(35,'Komal'),(36,'Veena'),(37,'Shree'),(38,'Roshan'),(39,'Sudeep'),(40,'Vinne'),(41,'Vidya'),(42,'Arvind'),(43,'Kumar'),(44,'Amy'),(45,'Ravi'),(46,'Sheeba'),(47,'Ram'),(48,'Rumaiza'),(49,'Aditi'),(50,'Surya');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-20  7:53:19
