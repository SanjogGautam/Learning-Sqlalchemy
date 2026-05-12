from sqlalchemy import create_engine,Integer,Float,String,Boolean,ForeignKey
from sqlalchemy.orm import DeclarativeBase,sessionmaker,Mapped,mapped_column,relationship
from typing import List
#this shows the many to many relationship between courses and students
db_url="sqlite:///manytomany.db"
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()
class base(DeclarativeBase):
    pass
class association(base):
    __tablename__ = "association"
    student_id: Mapped[int]=mapped_column(ForeignKey("students.id"),primary_key=True)
    course_id: Mapped[int]=mapped_column(ForeignKey("courses.id"),primary_key=True)
    
class Students(base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String)
    courses: Mapped[List["Courses"]]=relationship(secondary="association",back_populates="students")
class Courses(base):
    __tablename__="courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String)
    students: Mapped[List["Students"]]=relationship(secondary="association",back_populates="courses")
base.metadata.create_all(engine)
# math=Courses(name="Maths")
# physics=Courses(name="Physics")
# sanjog=Students(name="Sanjog Gautam",courses=[math,physics])
# sarin=Students(name="Sarin Pradhan",courses=[math])
# session.add_all([math,physics,sanjog,sarin])
# session.commit()
from sqlalchemy import create_engine,Integer,Float,String,Boolean,ForeignKey
from sqlalchemy.orm import DeclarativeBase,sessionmaker,Mapped,mapped_column,relationship
from typing import List
#this shows the many to many relationship between courses and students
db_url="sqlite:///manytomany.db"
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()
class base(DeclarativeBase):
    pass
class association(base):
    __tablename__ = "association"
    student_id: Mapped[int]=mapped_column(ForeignKey("students.id"),primary_key=True)
    course_id: Mapped[int]=mapped_column(ForeignKey("courses.id"),primary_key=True)
    
class Students(base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String)
    courses: Mapped[List["Courses"]]=relationship(secondary="association",back_populates="students")
class Courses(base):
    __tablename__="courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String)
    students: Mapped[List["Students"]]=relationship(secondary="association",back_populates="coureses")
base.metadata.create_all(engine)
# math=Courses(name="Maths")
# physics=Courses(name="Physics")
# sanjog=Students(name="Sanjog Gautam",courses=[math,physics])
# sarin=Students(name="Sarin Pradhan",courses=[math])
# session.add_all([math,physics,sanjog,sarin])
# session.commit()
a = session.query(Students).filter(Students.name == "Sanjog Gautam").first()
print(f"Courses for {a.name}: {[course.name for course in a.courses]}")