import pymysql
db = pymysql.connect("127.0.0.1", "root", "", "moviesdata", charset="utf8mb4")
cursor = db.cursor()
sql = """
DROP TABLE IF EXISTS `temp`;
DROP TABLE IF EXISTS `temp2`;
CREATE TABLE `temp`(
	`id` INT(11) NOT NULL,
	`name` VARCHAR(1000)DEFAULT NULL,
	`Thunderlinks` VARCHAR(1000)DEFAULT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `temp2`(
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(1000)DEFAULT NULL,
	`Thunderlinks` VARCHAR(1000)DEFAULT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT into `temp`(
select * from links_pro where Thunderlinks in (select  Thunderlinks from links_pro  group  by  Thunderlinks   having  count(Thunderlinks) > 0)
and id not in (select min(id) from  links_pro  group by Thunderlinks  having count(Thunderlinks)>0));
delete a.* from links_pro a, temp b where a.id = b.id ;
insert into `temp2`(name, Thunderlinks)
(select name, Thunderlinks from links_pro);
DROP TABLE IF EXISTS `links_pro`;
DROP TABLE IF EXISTS `temp`;
alter table temp2 rename links_pro;
"""
try:
    cursor.execute(sql)
    db.commit()
    print("成功")
except Exception as e:
    db.rollback()
    print("删除重复数据失败", e)
db.close()
