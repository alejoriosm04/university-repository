-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: aerotrack-reto
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
INSERT INTO `aerolinea` VALUES ('AA','American Airlines'),('AF','Air France'),('AM','Aeroméxico'),('AV','Avianca'),('BA','British Airways'),('DL','Delta Airlines'),('EK','Emirates'),('IB','Iberia'),('KL','KLM'),('LA','LATAM Airlines'),('LH','Lufthansa'),('QR','Qatar Airways'),('TK','Turkish Airlines'),('UA','United Airlines'),('VS','Virgin Atlantic'),('WN','Southwest Airlines'),('Y4','Volaris'),('YQ','Polet Airlines'),('YX','Republic Airways'),('ZE','Eastar Jet');
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
  `nombre_aeropuerto` varchar(127) NOT NULL,
  `id_pais_aeropuerto` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto` varchar(45) NOT NULL,
  PRIMARY KEY (`codigo_IATA_aeropuerto`,`id_pais_aeropuerto`,`id_ciudad_aeropuerto`),
  KEY `fk_aeropuerto_pais_idx` (`id_pais_aeropuerto`),
  KEY `fk_aeropuerto_ciudad1_idx` (`id_ciudad_aeropuerto`),
  CONSTRAINT `fk_aeropuerto_ciudad1` FOREIGN KEY (`id_ciudad_aeropuerto`) REFERENCES `ciudad` (`id_ciudad`),
  CONSTRAINT `fk_aeropuerto_pais` FOREIGN KEY (`id_pais_aeropuerto`) REFERENCES `pais` (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeropuerto`
--

LOCK TABLES `aeropuerto` WRITE;
/*!40000 ALTER TABLE `aeropuerto` DISABLE KEYS */;
INSERT INTO `aeropuerto` VALUES ('AMS','Aeropuerto de Ámsterdam-Schiphol','NLD','AMS'),('BCN','Aeropuerto de Barcelona-El Prat','ESP','BCN'),('BOG','Aeropuerto Internacional El Dorado','COL','BOG'),('CUN','Aeropuerto Internacional de Cancún','MEX','CUN'),('FRA','Aeropuerto de Fráncfort del Meno','DEU','FRA'),('HNL','Aeropuerto Internacional de Honolulu','USA','HNL'),('JFK','Aeropuerto Internacional John F. Kennedy','USA','JFK'),('LAX','Aeropuerto Internacional de Los Ángeles','USA','LAX'),('MAD','Aeropuerto Adolfo Suárez Madrid-Barajas','ESP','MAD'),('MEX','Aeropuerto Internacional de la Ciudad de México','MEX','MEX'),('MIA','Aeropuerto Internacional de Miami','USA','MIA'),('MVD','Aeropuerto Internacional de Carrasco','URY','MVD'),('SCL','Aeropuerto Internacional Comodoro Arturo Merino Benítez','CHL','SCL'),('SYD','Aeropuerto Internacional de Sídney','AUS','SYD');
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
  `nombre_ciudad` varchar(45) NOT NULL,
  PRIMARY KEY (`id_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudad`
--

LOCK TABLES `ciudad` WRITE;
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` VALUES ('AMS','Ámsterdam'),('BCN','Barcelona'),('BOG','Bogotá'),('CDG','París'),('CUN','Cancún'),('EZE','Buenos Aires'),('FCO','Roma'),('FRA','Fráncfort'),('GRU','São Paulo'),('HKG','Hong Kong'),('HNL','Honolulu'),('JFK','Nueva York'),('LAX','Los Ángeles'),('LHR','Londres'),('MAD','Madrid'),('MEX','Ciudad de México'),('MIA','Miami'),('MVD','Montevideo'),('SCL','Santiago de Chile'),('SYD','Sídney');
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
INSERT INTO `cliente` VALUES (1,'Juan Pérez',25,'juan.perez@example.com'),(2,'María Gómez',30,'maria.gomez@example.com'),(3,'Luisa González',40,'luisa.gonzalez@example.com'),(4,'Pedro Rodríguez',20,'pedro.rodriguez@example.com'),(5,'Ana Martínez',27,'ana.martinez@example.com'),(6,'Javier Sánchez',35,'javier.sanchez@example.com'),(7,'Carmen López',45,'carmen.lopez@example.com'),(8,'Miguel Álvarez',28,'miguel.alvarez@example.com'),(9,'Sofía Fernández',33,'sofia.fernandez@example.com'),(10,'Jorge Ramírez',22,'jorge.ramirez@example.com'),(11,'Adriana Torres',29,'adriana.torres@example.com'),(12,'Roberto Castro',38,'roberto.castro@example.com'),(13,'Paola Ortiz',42,'paola.ortiz@example.com'),(14,'Diego Moreno',26,'diego.moreno@example.com'),(15,'Valeria Navarro',31,'valeria.navarro@example.com'),(16,'Andrés Jiménez',37,'andres.jimenez@example.com'),(17,'Carolina Romero',41,'carolina.romero@example.com'),(18,'Pablo García',24,'pablo.garcia@example.com'),(19,'Lucía Torres',36,'lucia.torres@example.com'),(20,'Ricardo Medina',39,'ricardo.medina@example.com');
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
INSERT INTO `pais` VALUES ('ARG','Argentina'),('AUS','Australia'),('BRA','Brasil'),('CAN','Canadá'),('CHL','Chile'),('CHN','China'),('COL','Colombia'),('CRI','Costa Rica'),('DEU','Alemania'),('ESP','España'),('FRA','Francia'),('GBR','Reino Unido'),('ITA','Italia'),('JPN','Japón'),('MEX','México'),('NLD','Países Bajos'),('RUS','Rusia'),('URY','Uruguay'),('USA','Estados Unidos'),('ZAF','Sudáfrica');
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
  `id_vuelo_tiquete` varchar(45) NOT NULL,
  `codigo_IATA_aerolinea_vuelo_tiquete` varchar(45) NOT NULL,
  `codigo_IATA_aeropuerto_salida_tiquete` varchar(45) NOT NULL,
  `codigo_IATA_aeropuerto_llegada_tiquete` varchar(45) NOT NULL,
  `id_pais_aeropuerto_salida_tiquete` varchar(45) NOT NULL,
  `id_pais_aeropuerto_llegada_tiquete` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_salida_tiquete` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_llegada_tiquete` varchar(45) NOT NULL,
  `id_cliente` int NOT NULL,
  `grupo` enum('A','B','C','D') NOT NULL,
  `asiento` varchar(45) NOT NULL,
  `categoria_pasajero` enum('First Class','Business Class','Low Class','Premium Low Class') NOT NULL,
  `equipaje_mano` float DEFAULT NULL,
  `equipaje_bodega` float DEFAULT NULL,
  PRIMARY KEY (`id_tiquete`,`id_vuelo_tiquete`,`codigo_IATA_aerolinea_vuelo_tiquete`,`codigo_IATA_aeropuerto_salida_tiquete`,`codigo_IATA_aeropuerto_llegada_tiquete`,`id_pais_aeropuerto_salida_tiquete`,`id_pais_aeropuerto_llegada_tiquete`,`id_ciudad_aeropuerto_salida_tiquete`,`id_ciudad_aeropuerto_llegada_tiquete`,`id_cliente`),
  KEY `fk_vuelo_has_cliente_cliente1_idx` (`id_cliente`),
  KEY `fk_vuelo_has_cliente_vuelo1_idx` (`id_vuelo_tiquete`,`codigo_IATA_aerolinea_vuelo_tiquete`,`codigo_IATA_aeropuerto_salida_tiquete`,`codigo_IATA_aeropuerto_llegada_tiquete`,`id_pais_aeropuerto_salida_tiquete`,`id_pais_aeropuerto_llegada_tiquete`,`id_ciudad_aeropuerto_salida_tiquete`,`id_ciudad_aeropuerto_llegada_tiquete`),
  CONSTRAINT `fk_vuelo_has_cliente_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `fk_vuelo_has_cliente_vuelo1` FOREIGN KEY (`id_vuelo_tiquete`, `codigo_IATA_aerolinea_vuelo_tiquete`, `codigo_IATA_aeropuerto_salida_tiquete`, `codigo_IATA_aeropuerto_llegada_tiquete`, `id_pais_aeropuerto_salida_tiquete`, `id_pais_aeropuerto_llegada_tiquete`, `id_ciudad_aeropuerto_salida_tiquete`, `id_ciudad_aeropuerto_llegada_tiquete`) REFERENCES `vuelo` (`id_vuelo`, `codigo_IATA_aerolinea_vuelo`, `codigo_IATA_aeropuerto_salida`, `codigo_IATA_aeropuerto_llegada`, `id_pais_aeropuerto_salida`, `id_pais_aeropuerto_llegada`, `id_ciudad_aeropuerto_salida`, `id_ciudad_aeropuerto_llegada`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiquete_vuelo_cliente`
--

LOCK TABLES `tiquete_vuelo_cliente` WRITE;
/*!40000 ALTER TABLE `tiquete_vuelo_cliente` DISABLE KEYS */;
INSERT INTO `tiquete_vuelo_cliente` VALUES ('TQ001','AA123','AA','BOG','MIA','COL','USA','BOG','MIA',1,'A','14A','Business Class',7.5,15),('TQ002','AV321','AV','JFK','MIA','USA','USA','JFK','MIA',6,'B','18C','First Class',10,20),('TQ023','TK456','TK','AMS','BOG','NLD','COL','AMS','BOG',8,'C','6C','Low Class',10.8,22.3),('TQ023','TK456','TK','AMS','BOG','NLD','COL','AMS','BOG',16,'B','18C','First Class',10,20),('TQ0423','DL987','DL','MIA','LAX','USA','USA','MIA','LAX',16,'B','18C','First Class',10,20),('TQ2221','AV446','AV','LAX','BOG','USA','COL','LAX','BOG',12,'B','7B','First Class',11.8,NULL),('TQ2222','AV446','AV','LAX','BOG','USA','COL','LAX','BOG',12,'D','11D','Premium Low Class',17.8,20.3),('TQ7654','AA123','AA','BOG','MIA','COL','USA','BOG','MIA',20,'A','12A','Business Class',16.8,22.3),('TQ7664','AA123','AA','BOG','MIA','COL','USA','BOG','MIA',10,'A','13A','Business Class',17.8,32.3),('TQ964','KL910','KL','HNL','CUN','USA','MEX','HNL','CUN',17,'A','13A','Business Class',11.8,19.3);
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
  `codigo_IATA_aeropuerto_llegada` varchar(45) NOT NULL,
  `id_pais_aeropuerto_salida` varchar(45) NOT NULL,
  `id_pais_aeropuerto_llegada` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_salida` varchar(45) NOT NULL,
  `id_ciudad_aeropuerto_llegada` varchar(45) NOT NULL,
  `fecha_salida_vuelo` datetime NOT NULL,
  `fecha_llegada_vuelo` datetime NOT NULL,
  `categoria_vuelo` enum('National Flight','International Flight','Regional Flight') NOT NULL,
  PRIMARY KEY (`id_vuelo`,`codigo_IATA_aerolinea_vuelo`,`codigo_IATA_aeropuerto_salida`,`codigo_IATA_aeropuerto_llegada`,`id_pais_aeropuerto_salida`,`id_pais_aeropuerto_llegada`,`id_ciudad_aeropuerto_salida`,`id_ciudad_aeropuerto_llegada`),
  KEY `fk_vuelo_aerolinea1_idx` (`codigo_IATA_aerolinea_vuelo`),
  KEY `fk_vuelo_aeropuerto1_idx` (`codigo_IATA_aeropuerto_salida`,`id_pais_aeropuerto_salida`,`id_ciudad_aeropuerto_salida`),
  KEY `fk_vuelo_aeropuerto2_idx` (`codigo_IATA_aeropuerto_llegada`,`id_pais_aeropuerto_llegada`,`id_ciudad_aeropuerto_llegada`),
  CONSTRAINT `fk_vuelo_aerolinea1` FOREIGN KEY (`codigo_IATA_aerolinea_vuelo`) REFERENCES `aerolinea` (`codigo_IATA_aerolinea`),
  CONSTRAINT `fk_vuelo_aeropuerto1` FOREIGN KEY (`codigo_IATA_aeropuerto_salida`, `id_pais_aeropuerto_salida`, `id_ciudad_aeropuerto_salida`) REFERENCES `aeropuerto` (`codigo_IATA_aeropuerto`, `id_pais_aeropuerto`, `id_ciudad_aeropuerto`),
  CONSTRAINT `fk_vuelo_aeropuerto2` FOREIGN KEY (`codigo_IATA_aeropuerto_llegada`, `id_pais_aeropuerto_llegada`, `id_ciudad_aeropuerto_llegada`) REFERENCES `aeropuerto` (`codigo_IATA_aeropuerto`, `id_pais_aeropuerto`, `id_ciudad_aeropuerto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuelo`
--

LOCK TABLES `vuelo` WRITE;
/*!40000 ALTER TABLE `vuelo` DISABLE KEYS */;
INSERT INTO `vuelo` VALUES ('AA123','AA','BOG','MIA','COL','USA','BOG','MIA','2023-05-10 14:00:00','2023-05-10 17:00:00','National Flight'),('AA542','AA','MAD','BCN','ESP','ESP','MAD','BCN','2023-05-14 11:00:00','2023-05-14 14:00:00','Regional Flight'),('AA756','AA','LAX','JFK','USA','USA','LAX','JFK','2023-05-19 15:00:00','2023-05-19 21:00:00','National Flight'),('AF456','KL','BOG','MEX','COL','MEX','BOG','MEX','2023-05-12 16:00:00','2023-05-12 23:00:00','International Flight'),('AV321','AV','JFK','MIA','USA','USA','JFK','MIA','2023-05-13 08:00:00','2023-05-13 14:00:00','National Flight'),('AV446','AV','LAX','BOG','USA','COL','LAX','BOG','2023-05-19 15:00:00','2023-05-19 21:00:00','International Flight'),('AV555','AV','MIA','BOG','USA','COL','MIA','BOG','2023-05-14 11:00:00','2023-05-14 14:00:00','International Flight'),('DL987','DL','MIA','LAX','USA','USA','MIA','LAX','2023-05-15 07:00:00','2023-05-15 10:00:00','National Flight'),('KL910','KL','HNL','CUN','USA','MEX','HNL','CUN','2023-05-18 14:00:00','2023-05-18 20:00:00','International Flight'),('TK456','TK','AMS','BOG','NLD','COL','AMS','BOG','2023-05-19 15:00:00','2023-05-19 21:00:00','International Flight');
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

-- Dump completed on 2023-05-02 23:10:27
