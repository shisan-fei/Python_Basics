'''
数据库设计：
    id      nikename 昵称    info 留言信息     datetime留言时间
    1         张三             房屋出租           2021-09-25
语句：
    create database wlflt charset=utf8mb4;
    create table lyb(id int unsigned not null auto_increment primary key,
                    nikename varchar(6) not null,
                    info text not null,
                    datetime datetime not null
                    )engine=innodb default charset=utf8mb4
    insert into lyb values(null,'张三丰','房屋出租','2021-09-25');
    insert into lyb values(null,'渣渣辉','砍我','2021-09-25');
    insert into lyb values(null,'王龙飞','大家好','2021-09-25');
'''