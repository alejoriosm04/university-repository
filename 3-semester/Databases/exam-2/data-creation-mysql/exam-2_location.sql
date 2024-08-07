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
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `id_location` int NOT NULL,
  `state` enum('Tamil Nadu') NOT NULL,
  `region` enum('North','West','East','South','Central') NOT NULL,
  `city_id_city` int NOT NULL,
  PRIMARY KEY (`id_location`,`city_id_city`),
  KEY `fk_location_city_idx` (`city_id_city`),
  CONSTRAINT `fk_location_city` FOREIGN KEY (`city_id_city`) REFERENCES `city` (`id_city`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Tamil Nadu','North',1),(2,'Tamil Nadu','South',2),(3,'Tamil Nadu','West',3),(4,'Tamil Nadu','South',4),(5,'Tamil Nadu','South',5),(6,'Tamil Nadu','West',4),(7,'Tamil Nadu','West',6),(8,'Tamil Nadu','West',7),(9,'Tamil Nadu','West',8),(10,'Tamil Nadu','West',9),(11,'Tamil Nadu','West',10),(12,'Tamil Nadu','West',11),(13,'Tamil Nadu','South',12),(14,'Tamil Nadu','West',13),(15,'Tamil Nadu','Central',13),(16,'Tamil Nadu','Central',2),(17,'Tamil Nadu','Central',4),(18,'Tamil Nadu','West',14),(19,'Tamil Nadu','West',15),(20,'Tamil Nadu','West',1),(21,'Tamil Nadu','Central',10),(22,'Tamil Nadu','East',15),(23,'Tamil Nadu','West',5),(24,'Tamil Nadu','East',16),(25,'Tamil Nadu','East',2),(26,'Tamil Nadu','East',13),(27,'Tamil Nadu','East',4),(28,'Tamil Nadu','East',1),(29,'Tamil Nadu','East',6),(30,'Tamil Nadu','East',17),(31,'Tamil Nadu','Central',1),(32,'Tamil Nadu','Central',8),(33,'Tamil Nadu','Central',18),(34,'Tamil Nadu','Central',7),(35,'Tamil Nadu','Central',9),(36,'Tamil Nadu','Central',19),(37,'Tamil Nadu','Central',11),(38,'Tamil Nadu','Central',17),(39,'Tamil Nadu','Central',20),(40,'Tamil Nadu','East',9),(41,'Tamil Nadu','East',21),(42,'Tamil Nadu','Central',5),(43,'Tamil Nadu','Central',22),(44,'Tamil Nadu','East',20),(45,'Tamil Nadu','East',18),(46,'Tamil Nadu','East',23),(47,'Tamil Nadu','East',24),(48,'Tamil Nadu','East',3),(49,'Tamil Nadu','West',17),(50,'Tamil Nadu','West',21),(51,'Tamil Nadu','West',16),(52,'Tamil Nadu','South',22),(53,'Tamil Nadu','South',1),(54,'Tamil Nadu','Central',14),(55,'Tamil Nadu','Central',23),(56,'Tamil Nadu','South',9),(57,'Tamil Nadu','South',13),(58,'Tamil Nadu','West',19),(59,'Tamil Nadu','Central',16),(60,'Tamil Nadu','Central',3),(61,'Tamil Nadu','West',24),(62,'Tamil Nadu','East',5),(63,'Tamil Nadu','South',19),(64,'Tamil Nadu','South',8),(65,'Tamil Nadu','East',11),(66,'Tamil Nadu','Central',21),(67,'Tamil Nadu','Central',12),(68,'Tamil Nadu','East',10),(69,'Tamil Nadu','East',14),(70,'Tamil Nadu','East',19),(71,'Tamil Nadu','East',8),(72,'Tamil Nadu','Central',24),(73,'Tamil Nadu','West',23),(74,'Tamil Nadu','East',7),(75,'Tamil Nadu','West',22),(76,'Tamil Nadu','Central',15),(77,'Tamil Nadu','East',22),(78,'Tamil Nadu','West',18),(79,'Tamil Nadu','Central',6),(80,'Tamil Nadu','South',17),(81,'Tamil Nadu','South',24),(82,'Tamil Nadu','South',15),(83,'Tamil Nadu','South',11),(84,'Tamil Nadu','South',18),(85,'Tamil Nadu','South',16),(86,'Tamil Nadu','South',20),(87,'Tamil Nadu','West',12),(88,'Tamil Nadu','South',3),(89,'Tamil Nadu','South',23),(90,'Tamil Nadu','West',2),(91,'Tamil Nadu','West',20),(92,'Tamil Nadu','South',21),(93,'Tamil Nadu','East',12),(94,'Tamil Nadu','South',10),(95,'Tamil Nadu','South',6),(96,'Tamil Nadu','South',7),(97,'Tamil Nadu','South',14);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
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
