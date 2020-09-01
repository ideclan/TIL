## Courses

### Database Bootcamp

- [DATABASE 1&2 - MySQL](https://www.inflearn.com/course/database-2-mysql-%EA%B0%95%EC%A2%8C), 생활코딩, 2018
- [SQL/DB(MySQL) 기본부터 파이썬/데이터분석 활용까지!](https://www.inflearn.com/course/SQL-DB-MYSQL-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D), 인프런, 2019

### Theater Information Guide Database (MySQL)

- **Database create code**

```sql
CREATE DATABASE tig;
USE tig;

CREATE TABLE theaters(
    TheaterID int not null auto_increment,
    TheaterName varchar(50) not null,
    Period varchar(50) not null,
    Place varchar(50) not null,
    OpeningDay date null,
    ClosingDay date null,
    OpenRun varchar(50) default null,
    primary key(TheaterID)
);

CREATE TABLE theaters_details(
    TheaterID int not null,
    ViewingAge varchar(50) null,
    PerformanceTime varchar(50) null,
    Descriptions varchar(255) null,
    Price decimal(7) null,
    ShopTitle varchar(50) null,
    ShopLink longtext null,
    Image blob null,
    foreign key(TheaterID)
      references theaters(TheaterID) on delete cascade on update cascade
);

CREATE TABLE users(
    UserID int not null auto_increment,
    UserName varchar(50) not null,
    primary key(UserID)
);

CREATE TABLE comments(
    CommentID int not null auto_increment,
    UserID int not null,
    TheaterID int not null,
    Content varchar(255) null,
    Reply varchar(255) null,
    Likes int null,
    Image blob null,
    primary key(CommentID),
    foreign key(UserID)
      references users(UserID) on delete cascade on update cascade,
    foreign key(TheaterID)
      references theaters(TheaterID) on delete cascade on update cascade
);

LOAD DATA LOCAL INFILE 'C:/Users/LeeJiheon/Desktop/theater_df.csv'
INTO TABLE theaters
CHARACTER SET utf8
FIELDS TERMINATED BY ',';

# 8.0 version error
mysql -u root -p
show global variables like 'local_infile';
set global local_infile=true;

# 똑같은 error가 뜬다면
mysql --local-infile=1 -u root -p
```

<br>

- **Database ERD**

<br>

![tig_database_ERD](https://user-images.githubusercontent.com/48443734/73377954-35839480-4303-11ea-8d51-e2750ffd0d68.png)

<br>

- **Theaters Table**

<br>

![Theaters Table](https://user-images.githubusercontent.com/48443734/73336131-5b357d00-42b4-11ea-8dc6-bf4536152db6.png)

<br>

- **Theaters_details Table**

<br>

![Theaters_details](https://user-images.githubusercontent.com/48443734/73336132-5bce1380-42b4-11ea-876b-cad2a2dad0c7.png)
