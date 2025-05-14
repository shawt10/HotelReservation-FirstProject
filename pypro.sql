-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2025 at 03:49 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pypro`
--

-- --------------------------------------------------------

--
-- Table structure for table `ad_login`
--

CREATE TABLE `ad_login` (
  `ID` int(4) NOT NULL,
  `user` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ad_login`
--

INSERT INTO `ad_login` (`ID`, `user`, `password`) VALUES
(1, 'SEAN', '1234'),
(2, 'WAW', '1233'),
(4, '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `checkedin`
--

CREATE TABLE `checkedin` (
  `id` int(225) NOT NULL,
  `stay_ID` varchar(225) NOT NULL,
  `RoomType` varchar(225) NOT NULL,
  `Price` int(225) NOT NULL,
  `CheckInDate` date NOT NULL,
  `CheckStatus` varchar(225) NOT NULL,
  `RoomNo` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `checkedin`
--

INSERT INTO `checkedin` (`id`, `stay_ID`, `RoomType`, `Price`, `CheckInDate`, `CheckStatus`, `RoomNo`) VALUES
(24, '18DAPSRK', 'Single', 150, '2025-05-13', 'out', 103),
(25, '1GFPENH3', 'Deluxe', 150, '2025-05-13', 'checked ', 105),
(26, 'N676BVDX', 'Double', 150, '2025-05-13', 'checked ', 104),
(27, '3MVRYQ5W', 'Deluxe', 150, '2025-05-13', 'checked ', 205),
(28, 'YGK08FID', 'Deluxe', 150, '2025-05-21', 'out', 101);

-- --------------------------------------------------------

--
-- Table structure for table `information_desk`
--

CREATE TABLE `information_desk` (
  `ID` int(4) NOT NULL,
  `stay_ID` varchar(225) NOT NULL,
  `fName` varchar(225) NOT NULL,
  `mName` varchar(225) DEFAULT NULL,
  `lName` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `contactNo` int(11) NOT NULL,
  `address` varchar(225) NOT NULL,
  `child` int(5) NOT NULL,
  `adult` int(5) NOT NULL,
  `roomNo` int(5) NOT NULL,
  `dateStart` date NOT NULL,
  `dateOut` date NOT NULL,
  `checkStatus` varchar(225) NOT NULL,
  `paymentStatus` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `information_desk`
--

INSERT INTO `information_desk` (`ID`, `stay_ID`, `fName`, `mName`, `lName`, `email`, `contactNo`, `address`, `child`, `adult`, `roomNo`, `dateStart`, `dateOut`, `checkStatus`, `paymentStatus`) VALUES
(26, 'MUDXP6QW', 'a1', 'a1', 'a1', 'a1', 1, 'a1', 1, 1, 210, '2025-05-13', '2025-05-14', '', ''),
(27, 'M1U8MQ5I', 'a1', 'a1', 'a1', 'a1', 1, 'a1', 1, 1, 215, '2025-05-13', '2025-05-14', '', ''),
(28, 'TZCEJBTM', 'a1', 'a1', 'a1', 'a1', 1, '1', 1, 1, 215, '2025-05-13', '2025-05-14', '', ''),
(29, 'JQSF768V', 'g', 'g', 'g', '1', 1, '1', 1, 1, 105, '2025-05-30', '2025-05-14', '', ''),
(30, 'QS72QSJC', 'as', '1da', '1da', '1', 1, '1', 1, 1, 207, '2025-05-13', '2025-05-14', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `paymentID` int(225) NOT NULL,
  `TotalPaid` int(225) NOT NULL,
  `stay_ID` varchar(225) NOT NULL,
  `mop` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `room_id` int(11) NOT NULL,
  `floor_number` int(11) DEFAULT NULL,
  `room_number` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `Roomtype` varchar(225) NOT NULL,
  `Price` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`room_id`, `floor_number`, `room_number`, `status`, `Roomtype`, `Price`) VALUES
(1, 1, 101, 'Available', 'Deluxe', 150),
(2, 1, 102, 'Available', 'Suite', 150),
(3, 1, 103, 'Available', 'Single', 150),
(4, 1, 104, 'Occupied', 'Double', 150),
(5, 1, 105, 'Occupied', 'Deluxe', 150),
(6, 1, 106, 'Available', 'Suite', 150),
(7, 1, 107, 'Available', 'Single', 150),
(8, 1, 108, 'Available', 'Double', 150),
(9, 1, 109, 'Available', 'Deluxe', 150),
(10, 1, 110, 'Available', 'Suite', 150),
(11, 1, 111, 'Available', 'Single', 150),
(12, 1, 112, 'Available', 'Double', 150),
(13, 1, 113, 'Available', 'Deluxe', 150),
(14, 1, 114, 'Available', 'Suite', 150),
(15, 1, 115, 'Available', 'Double', 150),
(16, 1, 116, 'Available', 'Double', 150),
(17, 1, 117, 'Available', 'Deluxe', 150),
(18, 1, 118, 'Available', 'Suite', 150),
(19, 1, 119, 'Available', 'Single', 150),
(20, 1, 120, 'Available', 'Double', 150),
(21, 2, 201, 'Available', 'Deluxe', 150),
(22, 2, 202, 'Available', 'Suite', 150),
(23, 2, 203, 'Available', 'Single', 150),
(24, 2, 204, 'Available', 'Double', 150),
(25, 2, 205, 'Occupied', 'Deluxe', 150),
(26, 2, 206, 'Available', 'Suite', 150),
(27, 2, 207, 'Available', 'Single', 150),
(28, 2, 208, 'Available', 'Double', 150),
(29, 2, 209, 'Available', 'Deluxe', 150),
(30, 2, 210, 'Available', 'Suite', 150),
(31, 2, 211, 'Available', '', 0),
(32, 2, 212, 'Available', '', 0),
(33, 2, 213, 'Available', '', 0),
(34, 2, 214, 'Available', '', 0),
(35, 2, 215, 'Available', '', 0),
(36, 2, 216, 'Available', '', 0),
(37, 2, 217, 'Available', '', 0),
(38, 2, 218, 'Available', '', 0),
(39, 2, 219, 'Available', '', 0),
(40, 2, 220, 'Available', '', 0),
(41, 3, 301, 'Available', '', 0),
(42, 3, 302, 'Available', '', 0),
(43, 3, 303, 'Available', '', 0),
(44, 3, 304, 'Available', '', 0),
(45, 3, 305, 'Available', '', 0),
(46, 3, 306, 'Available', '', 0),
(47, 3, 307, 'Available', '', 0),
(48, 3, 308, 'Available', '', 0),
(49, 3, 309, 'Available', '', 0),
(50, 3, 310, 'Available', '', 0),
(51, 3, 311, 'Available', '', 0),
(52, 3, 312, 'Available', '', 0),
(53, 3, 313, 'Available', '', 0),
(54, 3, 314, 'Available', '', 0),
(55, 3, 315, 'Available', '', 0),
(56, 3, 316, 'Available', '', 0),
(57, 3, 317, 'Available', '', 0),
(58, 3, 318, 'Available', '', 0),
(59, 3, 319, 'Available', '', 0),
(60, 3, 320, 'Available', '', 0),
(76, 1, 115, 'Available', 'Double', 150);

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `ID` int(11) NOT NULL,
  `stay_ID` varchar(225) NOT NULL,
  `ServiceID` int(11) NOT NULL,
  `Price` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`ID`, `stay_ID`, `ServiceID`, `Price`) VALUES
(14, 'ZEZIBV50', 1, '100'),
(20, 'TQLCL1WW', 1, '100'),
(24, 'QA5QR8MP', 1, '100'),
(31, 'R3LW1SD7', 1, '100'),
(42, '18DAPSRK', 1, '100'),
(43, '18DAPSRK', 6, '20'),
(44, '18DAPSRK', 7, '150'),
(45, '18DAPSRK', 8, '40'),
(46, '18DAPSRK', 9, '250'),
(47, '18DAPSRK', 10, '0'),
(48, '18DAPSRK', 1, '100'),
(49, '18DAPSRK', 6, '20'),
(50, '18DAPSRK', 7, '150'),
(51, '18DAPSRK', 8, '40'),
(52, '18DAPSRK', 9, '250'),
(53, '18DAPSRK', 10, '0'),
(54, '18DAPSRK', 15, '0'),
(55, '18DAPSRK', 16, '30'),
(56, 'YGK08FID', 1, '100'),
(57, 'YGK08FID', 13, '1500');

-- --------------------------------------------------------

--
-- Table structure for table `servicestable`
--

CREATE TABLE `servicestable` (
  `ServiceID` int(11) NOT NULL,
  `Sevice_Name` varchar(225) NOT NULL,
  `Description` varchar(225) NOT NULL,
  `Price` varchar(225) NOT NULL,
  `Availability` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `servicestable`
--

INSERT INTO `servicestable` (`ServiceID`, `Sevice_Name`, `Description`, `Price`, `Availability`) VALUES
(1, 'Room Service', 'In-room dining delivered to your door', '100', '24/7'),
(6, 'Breakfast', 'Daily selection of hot and cold breakfast items', '20', '6:00 AM - 10:30 AM'),
(7, 'Restaurant', 'Upscale on-site restaurant offering gourmet cuisine', '150', '6:00 PM - 11:00 PM'),
(8, 'Lobby Bar', 'Casual setting for drinks and light fare', '40', '12:00 PM - 1:00 AM'),
(9, 'Spa', 'Various massage and body treatments', '250', '9:00 AM - 8:00 PM'),
(10, 'Fitness Center', '24-hour access to exercise equipment', '0', '24/7'),
(11, 'Pool', 'Indoor or outdoor pool facilities', '0', '7:00 AM - 10:00 PM'),
(12, 'Sauna', 'Heat therapy rooms for relaxation', '0', '7:00 AM - 10:00 PM'),
(13, 'Meeting Room', 'Private spaces for business gatherings', '1500', 'Based on availability'),
(14, 'Business Center', 'Computers, printing, and office services', '1', '24/7'),
(15, 'Wi-Fi', 'Premium internet connection', '0', '24/7'),
(16, 'Airport Transfer', 'Private transportation between hotel and airport', '30', 'By reservation'),
(17, 'Valet Parking', 'Attended vehicle parking service', '75', '24/7'),
(18, 'Concierge', 'Personalized assistance with reservations and arrangements', '0', '7:00 AM - 11:00 PM'),
(19, 'Laundry', 'Clothing care services', '20', 'Drop-off by 10AM, same-day service');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ad_login`
--
ALTER TABLE `ad_login`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `checkedin`
--
ALTER TABLE `checkedin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `information_desk`
--
ALTER TABLE `information_desk`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `stay_ID` (`stay_ID`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`paymentID`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`room_id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `servicestable`
--
ALTER TABLE `servicestable`
  ADD PRIMARY KEY (`ServiceID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ad_login`
--
ALTER TABLE `ad_login`
  MODIFY `ID` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `checkedin`
--
ALTER TABLE `checkedin`
  MODIFY `id` int(225) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `information_desk`
--
ALTER TABLE `information_desk`
  MODIFY `ID` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `paymentID` int(225) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `room_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `servicestable`
--
ALTER TABLE `servicestable`
  MODIFY `ServiceID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
