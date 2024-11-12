DROP TABLE IF EXISTS api_Ve;
DROP TABLE IF EXISTS api_Ghe;
DROP TABLE IF EXISTS api_LichChieu;
DROP TABLE IF EXISTS api_PhongChieu;
DROP TABLE IF EXISTS api_Rap;
DROP TABLE IF EXISTS api_DatVe;
DROP TABLE IF EXISTS api_user;
DROP TABLE IF EXISTS api_Phim;


CREATE TABLE api_phim (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Ten_Phim NVARCHAR(255),
    Dao_Dien NVARCHAR(100),
    Dien_Vien NVARCHAR(100),
    The_Loai NVARCHAR(100),
    Thoi_Luong INT,
    Mo_Ta TEXT,
    Ngay_Phat_Hanh DATE
);

ALTER TABLE api_phim
ADD COLUMN Image VARCHAR(255);

CREATE TABLE api_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Ho_Ten NVARCHAR(100),
    Email NVARCHAR(100),
    So_Dien_Thoai NVARCHAR(20),
    Mat_Khau NVARCHAR(50),
    Vai_Tro NVARCHAR(100),
    Luong DECIMAL(15,3)
);

CREATE TABLE api_rap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Ten_Rap NVARCHAR(255),
    Dia_Chi NVARCHAR(100),
    So_Dien_Thoai NVARCHAR(20),
    So_Phong_Chieu INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES api_user(id)
);

CREATE TABLE api_phongchieu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Ten_Phong NVARCHAR(100),
    So_Ghe INT,
    rap_id INT,
    FOREIGN KEY (rap_id) REFERENCES api_rap(id)
);

CREATE TABLE api_lichchieu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Thoi_Gian TIME,
    phim_id INT,
    phong_chieu_id INT,
    FOREIGN KEY (phim_id) REFERENCES api_phim(id),
    FOREIGN KEY (phong_chieu_id) REFERENCES api_phongchieu(id)
);

CREATE TABLE api_ghe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Loai_Ghe NVARCHAR(50),
    Trang_Thai ENUM('Trống', 'Đã Đặt'),
    phong_chieu_id INT,
    FOREIGN KEY (phong_chieu_id) REFERENCES api_phongchieu(id)
);

CREATE TABLE api_ve (
    id INT AUTO_INCREMENT PRIMARY KEY,
    So_Ghe VARCHAR(10),
	Ngay_Dat DATE,
    Tong_Tien DECIMAL(15,3),
    Phuong_Thuc NVARCHAR(50),
    user_id INT,
    lich_chieu_id INT,
    FOREIGN KEY (user_id) REFERENCES api_user(id),
    FOREIGN KEY (lich_chieu_id) REFERENCES api_lichchieu(id)
);

-- Insert data into api_phim
INSERT INTO api_phim (Ten_Phim, Dao_Dien, Dien_Vien, The_Loai, Thoi_Luong, Mo_Ta, Ngay_Phat_Hanh) VALUES
('Inception', 'Christopher Nolan', 'Leonardo DiCaprio', 'Sci-Fi', 148, 'A thief who steals corporate secrets through the use of dream-sharing technology.', '2010-07-16'),
('Parasite', 'Bong Joon-ho', 'Song Kang-ho', 'Thriller', 132, 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.', '2019-05-30'),
('The Godfather', 'Francis Ford Coppola', 'Marlon Brando', 'Crime', 175, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', '1972-03-24'),
('Spirited Away', 'Hayao Miyazaki', 'Rumi Hiiragi', 'Animation', 125, 'During her family\'s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.', '2001-07-20');

-- Insert data into api_user
INSERT INTO api_user (Ho_Ten, Email, So_Dien_Thoai, Mat_Khau, Vai_Tro, Luong) VALUES
('Nguyen Van A', 'nguyenvana@example.com', '0123456789', 'passwordA', 'Admin', 15000.000),
('Tran Thi B', 'tranthib@example.com', '0987654321', 'passwordB', 'User', 12000.000),
('Le Van C', 'levanc@example.com', '0111222333', 'passwordC', 'User', 13000.000),
('Pham Thi D', 'phamthid@example.com', '0999888777', 'passwordD', 'Manager', 14000.000);

-- Insert data into api_rap
INSERT INTO api_rap (Ten_Rap, Dia_Chi, So_Dien_Thoai, So_Phong_Chieu, user_id) VALUES
('CGV Vincom', '191 Ba Trieu, Hanoi', '0241234567', 10, 1),
('Lotte Cinema', '54 Lieu Giai, Hanoi', '0247654321', 8, 2),
('Galaxy Cinema', '87 Lang Ha, Hanoi', '0241122334', 7, 3),
('BHD Star', '2 Hai Trieu, Ho Chi Minh City', '0289988776', 9, 4);

-- Insert data into api_phongchieu
INSERT INTO api_phongchieu (Ten_Phong, So_Ghe, rap_id) VALUES
('Phong 1', 150, 1),
('Phong 2', 120, 2),
('Phong 3', 100, 3),
('Phong 4', 130, 4);

-- Insert data into api_lichchieu
INSERT INTO api_lichchieu (Thoi_Gian, phim_id, phong_chieu_id) VALUES
('10:00:00', 1, 1),
('12:00:00', 2, 2),
('14:00:00', 3, 3),
('16:00:00', 4, 4);

-- Insert data into api_ghe
INSERT INTO api_ghe (Loai_Ghe, Trang_Thai, phong_chieu_id) VALUES
('VIP', 'Trống', 1),
('Standard', 'Đã Đặt', 2),
('VIP', 'Trống', 3),
('Standard', 'Đã Đặt', 4);

-- Insert data into api_ve
INSERT INTO api_ve (So_Ghe, Ngay_Dat, Tong_Tien, Phuong_Thuc, user_id, lich_chieu_id) VALUES
('A1', '2024-01-01', 150.000, 'Credit Card', 1, 1),
('B1', '2024-02-01', 120.000, 'Cash', 2, 2),
('C1', '2024-03-01', 130.000, 'Credit Card', 3, 3),
('D1', '2024-04-01', 140.000, 'Cash', 4, 4);

