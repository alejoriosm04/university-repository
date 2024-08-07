-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: aerotrack-reto-final
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
-- Table structure for table `aerolinea`
--

DROP TABLE IF EXISTS `aerolinea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aerolinea` (
  `codigo_IATA_aerolinea` varchar(45) NOT NULL,
  `nombre_aerolinea` varchar(127) NOT NULL,
  PRIMARY KEY (`codigo_IATA_aerolinea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aerolinea`
--

LOCK TABLES `aerolinea` WRITE;
/*!40000 ALTER TABLE `aerolinea` DISABLE KEYS */;
INSERT INTO `aerolinea` VALUES ('AA','American Airlines'),('AF','Air France'),('AI','Air India'),('AV','Avianca'),('AZ','Alitalia'),('BA','British Airways'),('CX','Cathay Pacific'),('DL','Delta Air Lines'),('EK','Emirates'),('EY','Etihad Airways'),('JL','Japan Airlines'),('LA','LATAM Airlines'),('LH','Lufthansa'),('MX','Aeroméxico'),('QF','Qantas'),('QR','Qatar Airways'),('SQ','Singapore Airlines'),('SU','Aeroflot'),('TK','Turkish Airlines'),('UA','United Airlines');
/*!40000 ALTER TABLE `aerolinea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aeropuerto`
--

DROP TABLE IF EXISTS `aeropuerto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aeropuerto` (
  `codigo_IATA_aeropuerto` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto` varchar(45) NOT NULL,
  `id_pais_aeropuerto` varchar(45) NOT NULL,
  `nombre_aeropuerto` varchar(127) NOT NULL,
  PRIMARY KEY (`codigo_IATA_aeropuerto`,`id_ciudad_aeropuerto`,`id_pais_aeropuerto`),
  KEY `fk_aeropuerto_ciudad1_idx` (`id_ciudad_aeropuerto`,`id_pais_aeropuerto`),
  CONSTRAINT `fk_aeropuerto_ciudad1` FOREIGN KEY (`id_ciudad_aeropuerto`, `id_pais_aeropuerto`) REFERENCES `ciudad` (`id_ciudad`, `id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeropuerto`
--

LOCK TABLES `aeropuerto` WRITE;
/*!40000 ALTER TABLE `aeropuerto` DISABLE KEYS */;
INSERT INTO `aeropuerto` VALUES ('BOG','BOG','COL','Aeropuerto Internacional El Dorado'),('CDG','PAR','FRA','Aeropuerto de París-Charles de Gaulle'),('DEL','DEL','IND','Aeropuerto Internacional Indira Gandhi'),('EZE','BUE','ARG','Aeropuerto Internacional Ministro Pistarini (Ezeiza)'),('FCO','ROM','ITA','Aeropuerto Internacional Leonardo da Vinci-Fiumicino'),('GIG','RIO','BRA','Aeropuerto Internacional Galeão - Antonio Carlos Jobim'),('HND','TOK','JPN','Aeropuerto Internacional de Haneda'),('ICN','SEO','KOR','Aeropuerto Internacional de Incheon'),('JFK','NYC','USA','Aeropuerto Internacional John F. Kennedy'),('JNB','JNB','ZAF','Aeropuerto Internacional OR Tambo'),('LHR','LON','GBR','Aeropuerto de Londres-Heathrow'),('LIM','LIM','PER','Aeropuerto Internacional Jorge Chávez'),('MAD','MAD','ESP','Aeropuerto Adolfo Suárez Madrid-Barajas'),('MEX','MEX','MEX','Aeropuerto Internacional de la Ciudad de México'),('PVG','SHA','CHN','Aeropuerto Internacional de Shanghái-Pudong'),('SCL','SCL','CHL','Aeropuerto Internacional Arturo Merino Benítez'),('SVO','MOS','RUS','Aeropuerto Internacional de Sheremétievo'),('SYD','SYD','AUS','Aeropuerto Internacional Kingsford Smith de Sídney'),('TXL','BER','DEU','Aeropuerto de Berlín-Tegel'),('YYZ','TOR','CAN','Aeropuerto Internacional Toronto Pearson');
/*!40000 ALTER TABLE `aeropuerto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudad`
--

DROP TABLE IF EXISTS `ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudad` (
  `id_ciudad` varchar(45) NOT NULL,
  `id_pais` varchar(45) NOT NULL,
  `nombre_ciudad` varchar(45) NOT NULL,
  PRIMARY KEY (`id_ciudad`,`id_pais`),
  KEY `fk_ciudad_pais_idx` (`id_pais`),
  CONSTRAINT `fk_ciudad_pais` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudad`
--

LOCK TABLES `ciudad` WRITE;
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` VALUES ('BER','DEU','Berlín'),('BOG','COL','Bogotá'),('BUE','ARG','Buenos Aires'),('DEL','IND','Delhi'),('JNB','ZAF','Johannesburgo'),('LIM','PER','Lima'),('LON','GBR','Londres'),('MAD','ESP','Madrid'),('MEX','MEX','Ciudad de México'),('MOS','RUS','Moscú'),('NYC','USA','Nueva York'),('PAR','FRA','París'),('RIO','BRA','Río de Janeiro'),('ROM','ITA','Roma'),('SCL','CHL','Santiago de Chile'),('SEO','KOR','Seúl'),('SHA','CHN','Shanghái'),('SYD','AUS','Sídney'),('TOK','JPN','Tokio'),('TOR','CAN','Toronto');
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL,
  `nombre_cliente` varchar(127) NOT NULL,
  `edad` int NOT NULL,
  `email_cliente` varchar(127) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Juan Pérez',35,'juanperez@example.com'),(2,'María González',28,'mariagonzalez@example.com'),(3,'Carlos López',42,'carloslopez@example.com'),(4,'Ana Martínez',31,'anamartinez@example.com'),(5,'Luis Herrera',47,'luisherrera@example.com'),(6,'Laura Torres',25,'latorres@example.com'),(7,'Andrés Sánchez',38,'andressanchez@example.com'),(8,'Patricia Romero',33,'patriciaromero@example.com'),(9,'Gabriel Ramírez',40,'gabrielramirez@example.com'),(10,'Sofía Rodríguez',29,'sofiarodriguez@example.com'),(11,'Alejandro Vargas',37,'alejandrovargas@example.com'),(12,'Carolina Medina',26,'carolinamedina@example.com'),(13,'Sergio Paredes',44,'sergioparedes@example.com'),(14,'Natalia Silva',30,'nataliasilva@example.com'),(15,'Javier Mendoza',36,'javiermendoza@example.com'),(16,'Gabriela Ortega',27,'gabrielaortega@example.com'),(17,'Andrés Morales',39,'andresmorales@example.com'),(18,'Valeria Ríos',32,'valeriaríos@example.com'),(19,'Eduardo Castro',34,'eduardocastro@example.com'),(20,'Alejandra Guzmán',41,'alejandraguzman@example.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pais`
--

DROP TABLE IF EXISTS `pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pais` (
  `id_pais` varchar(45) NOT NULL,
  `nombre_pais` varchar(45) NOT NULL,
  PRIMARY KEY (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pais`
--

LOCK TABLES `pais` WRITE;
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` VALUES ('ARG','Argentina'),('AUS','Australia'),('BRA','Brasil'),('CAN','Canadá'),('CHL','Chile'),('CHN','China'),('COL','Colombia'),('DEU','Alemania'),('ESP','España'),('FRA','Francia'),('GBR','Reino Unido'),('IND','India'),('ITA','Italia'),('JPN','Japón'),('KOR','Corea del Sur'),('MEX','México'),('PER','Perú'),('RUS','Rusia'),('USA','Estados Unidos'),('ZAF','Sudáfrica');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiquete_vuelo_cliente`
--

DROP TABLE IF EXISTS `tiquete_vuelo_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiquete_vuelo_cliente` (
  `id_tiquete` varchar(45) NOT NULL,
  `id_cliente` int NOT NULL,
  `id_vuelo_tiquete` varchar(45) NOT NULL,
  `codigo_IATA_aerolinea_vuelo_tiquete` varchar(45) NOT NULL,
  `codigo_IATA_aeropuerto_salida_tiquete` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_salida_tiquete` varchar(45) NOT NULL,
  `id_pais_aeropuerto_salida_tiquete` varchar(45) NOT NULL,
  `codigo_IATA_aeropuerto_llegada_tiquete` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_llegada_tiquete` varchar(45) NOT NULL,
  `id_pais_aeropuerto_llegada_tiquete` varchar(45) NOT NULL,
  `grupo` enum('A','B','C','D') NOT NULL,
  `asiento` varchar(45) NOT NULL,
  `categoria_pasajero` enum('First Class','Business Class','Low Class','Premium Low Class') NOT NULL,
  `equipaje_mano` float DEFAULT NULL,
  `equipaje_bodega` float DEFAULT NULL,
  PRIMARY KEY (`id_tiquete`,`id_cliente`,`id_vuelo_tiquete`,`codigo_IATA_aerolinea_vuelo_tiquete`,`codigo_IATA_aeropuerto_salida_tiquete`,`id_ciudad_aeropuerto_salida_tiquete`,`id_pais_aeropuerto_salida_tiquete`,`codigo_IATA_aeropuerto_llegada_tiquete`,`id_ciudad_aeropuerto_llegada_tiquete`,`id_pais_aeropuerto_llegada_tiquete`),
  KEY `fk_cliente_has_vuelo_vuelo1_idx` (`id_vuelo_tiquete`,`codigo_IATA_aerolinea_vuelo_tiquete`,`codigo_IATA_aeropuerto_salida_tiquete`,`id_ciudad_aeropuerto_salida_tiquete`,`id_pais_aeropuerto_salida_tiquete`,`codigo_IATA_aeropuerto_llegada_tiquete`,`id_ciudad_aeropuerto_llegada_tiquete`,`id_pais_aeropuerto_llegada_tiquete`),
  KEY `fk_cliente_has_vuelo_cliente1_idx` (`id_cliente`),
  CONSTRAINT `fk_cliente_has_vuelo_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `fk_cliente_has_vuelo_vuelo1` FOREIGN KEY (`id_vuelo_tiquete`, `codigo_IATA_aerolinea_vuelo_tiquete`, `codigo_IATA_aeropuerto_salida_tiquete`, `id_ciudad_aeropuerto_salida_tiquete`, `id_pais_aeropuerto_salida_tiquete`, `codigo_IATA_aeropuerto_llegada_tiquete`, `id_ciudad_aeropuerto_llegada_tiquete`, `id_pais_aeropuerto_llegada_tiquete`) REFERENCES `vuelo` (`id_vuelo`, `codigo_IATA_aerolinea_vuelo`, `codigo_IATA_aeropuerto_salida`, `id_ciudad_aeropuerto_salida`, `id_pais_aeropuerto_salida`, `codigo_IATA_aeropuerto_llegada`, `id_ciudad_aeropuerto_llegada`, `id_pais_aeropuerto_llegada`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiquete_vuelo_cliente`
--

LOCK TABLES `tiquete_vuelo_cliente` WRITE;
/*!40000 ALTER TABLE `tiquete_vuelo_cliente` DISABLE KEYS */;
INSERT INTO `tiquete_vuelo_cliente` VALUES ('CX466',16,'MX122','MX','MEX','MEX','MEX','JFK','NYC','USA','B','B2','Business Class',10.2,0),('FS6545',4,'AI567','AI','DEL','DEL','IND','JNB','JNB','ZAF','B','B5','Business Class',23.1,10.36),('FU989',7,'JL567','JL','HND','TOK','JPN','PVG','SHA','CHN','A','A6','First Class',7.21,10.3),('GR5466',6,'SU789','SU','SVO','MOS','RUS','SYD','SYD','AUS','A','A2','First Class',6,9.3),('GS102',11,'MX122','MX','MEX','MEX','MEX','JFK','NYC','USA','C','CC6','Low Class',29.36,1.23),('HW5462',3,'EY777','EY','DEL','DEL','IND','PVG','SHA','CHN','B','B9','Business Class',4.36,2.31),('NB646',2,'AZ789','AZ','FCO','ROM','ITA','MAD','MAD','ESP','A','A1','First Class',7.25,42.3),('TY656',2,'MX122','MX','MEX','MEX','MEX','JFK','NYC','USA','C','C11','Low Class',5.2,23.6),('UI5645',9,'AI567','AI','DEL','DEL','IND','JNB','JNB','ZAF','A','A1','First Class',23.5,8.65);
/*!40000 ALTER TABLE `tiquete_vuelo_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuelo`
--

DROP TABLE IF EXISTS `vuelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vuelo` (
  `id_vuelo` varchar(45) NOT NULL,
  `codigo_IATA_aerolinea_vuelo` varchar(45) NOT NULL,
  `codigo_IATA_aeropuerto_salida` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_salida` varchar(45) NOT NULL,
  `id_pais_aeropuerto_salida` varchar(45) NOT NULL,
  `codigo_IATA_aeropuerto_llegada` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_llegada` varchar(45) NOT NULL,
  `id_pais_aeropuerto_llegada` varchar(45) NOT NULL,
  `fecha_salida_vuelo` datetime NOT NULL,
  `fecha_llegada_vuelo` datetime NOT NULL,
  `categoria_vuelo` enum('National Flight','International Flight','Regional Flight') NOT NULL,
  PRIMARY KEY (`id_vuelo`,`codigo_IATA_aerolinea_vuelo`,`codigo_IATA_aeropuerto_salida`,`id_ciudad_aeropuerto_salida`,`id_pais_aeropuerto_salida`,`codigo_IATA_aeropuerto_llegada`,`id_ciudad_aeropuerto_llegada`,`id_pais_aeropuerto_llegada`),
  KEY `fk_vuelo_aerolinea1_idx` (`codigo_IATA_aerolinea_vuelo`),
  KEY `fk_vuelo_aeropuerto1_idx` (`codigo_IATA_aeropuerto_salida`,`id_ciudad_aeropuerto_salida`,`id_pais_aeropuerto_salida`),
  KEY `fk_vuelo_aeropuerto2_idx` (`codigo_IATA_aeropuerto_llegada`,`id_ciudad_aeropuerto_llegada`,`id_pais_aeropuerto_llegada`),
  CONSTRAINT `fk_vuelo_aerolinea1` FOREIGN KEY (`codigo_IATA_aerolinea_vuelo`) REFERENCES `aerolinea` (`codigo_IATA_aerolinea`),
  CONSTRAINT `fk_vuelo_aeropuerto1` FOREIGN KEY (`codigo_IATA_aeropuerto_salida`, `id_ciudad_aeropuerto_salida`, `id_pais_aeropuerto_salida`) REFERENCES `aeropuerto` (`codigo_IATA_aeropuerto`, `id_ciudad_aeropuerto`, `id_pais_aeropuerto`),
  CONSTRAINT `fk_vuelo_aeropuerto2` FOREIGN KEY (`codigo_IATA_aeropuerto_llegada`, `id_ciudad_aeropuerto_llegada`, `id_pais_aeropuerto_llegada`) REFERENCES `aeropuerto` (`codigo_IATA_aeropuerto`, `id_ciudad_aeropuerto`, `id_pais_aeropuerto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuelo`
--

LOCK TABLES `vuelo` WRITE;
/*!40000 ALTER TABLE `vuelo` DISABLE KEYS */;
INSERT INTO `vuelo` VALUES ('AA123','AA','JFK','NYC','USA','YYZ','TOR','CAN','2023-05-17 10:00:00','2023-05-17 12:00:00','International Flight'),('AI567','AI','DEL','DEL','IND','JNB','JNB','ZAF','2023-05-21 12:30:00','2023-05-21 20:45:00','International Flight'),('AV238','AV','BOG','BOG','COL','BOG','BOG','COL','2023-05-24 08:00:00','2023-05-24 11:30:00','National Flight'),('AV345','AV','BOG','BOG','COL','LIM','LIM','PER','2023-05-22 09:00:00','2023-05-22 12:15:00','International Flight'),('AV567','AV','BOG','BOG','COL','EZE','BUE','ARG','2023-05-30 11:30:00','2023-05-30 16:15:00','International Flight'),('AZ789','AZ','FCO','ROM','ITA','MAD','MAD','ESP','2023-05-19 09:30:00','2023-05-19 12:00:00','International Flight'),('BA789','BA','EZE','BUE','ARG','LHR','LON','GBR','2023-05-18 08:45:00','2023-05-18 20:15:00','International Flight'),('EY777','EY','DEL','DEL','IND','PVG','SHA','CHN','2023-05-29 13:15:00','2023-05-29 17:30:00','International Flight'),('JL567','JL','HND','TOK','JPN','PVG','SHA','CHN','2023-05-19 16:45:00','2023-05-19 19:30:00','International Flight'),('MX122','MX','MEX','MEX','MEX','JFK','NYC','USA','2023-05-26 12:30:00','2023-05-26 14:00:00','International Flight'),('MX456','MX','MEX','MEX','MEX','GIG','RIO','BRA','2023-05-17 14:30:00','2023-05-17 19:00:00','International Flight'),('SQ452','SQ','ICN','SEO','KOR','PVG','SHA','CHN','2023-05-31 14:00:00','2023-05-31 16:30:00','International Flight'),('SU789','SU','SVO','MOS','RUS','SYD','SYD','AUS','2023-05-20 07:00:00','2023-05-20 23:30:00','International Flight'),('UA987','UA','YYZ','TOR','CAN','JFK','NYC','USA','2023-05-25 14:00:00','2023-05-25 15:30:00','International Flight');
/*!40000 ALTER TABLE `vuelo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-17 13:56:49