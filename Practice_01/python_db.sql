

CREATE TABLE `store_data` (
  `id` int(100) NOT NULL,
  `line1` text NOT NULL,
  `line2` text NOT NULL,
  `line3` text NOT NULL,
  `file_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `store_data`
--
ALTER TABLE `store_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `store_data`
--
ALTER TABLE `store_data`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;
COMMIT;
