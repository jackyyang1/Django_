create table students (
	id int unsigned primary key auto_increment not null,
	name varchar(20) default '',
	age tinyint unsigned default 0,
	height decimal(5,2),
	gender enum('男','女','中性','保密') default '保密',
	cls_id int unsigned default 0,
	is_delete bit default 0


)

# id 有可能是很多位，远远超过256，那就需要多个字节，就要用int ，id没有默认值，设置为自动递增和非空之后，系统会自动从1开始添加，
# 
#  name 有var 和varchar两种，var会自动补充空格填充位置，20是最大名字长度，默认为空
#  
#  age：因为年龄最多也就100来岁，所以远远小于256，用tinyint就可以搞定，unsigned无符号即不是负数，默认为0
#  
#  height：decimal（5,2）长度为5，有效数字为5，小数点后面有两位
#  
#  gender： enum（），枚举出好几种性别，再默认一个性别
#  
#  cls_id:  int 班级数未知，无符号，默认为0，default0
#  
#  id_delete :设置是否为逻辑删除，即不是真正意义上的删除，bit（字段），default 0，即1是逻辑删除
 注：除了height有decimal ，id有not null，其他任意数字类型的字段 都默认为 default 0，  



-- classes 表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);
 

-- 向students表中插入数据
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0);


-- 向classes表中插入数据
insert into classes values (0, "python5"), (0, "python6"),
(0, "python7"), (0, "python8");


注：插入的数据，其中 第一个0，表示插入的位置，这里用的是0，是占位符，因为是自动递增的
  所以它会自动填补
