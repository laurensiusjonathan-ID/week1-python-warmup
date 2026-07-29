from pydantic import BaseModel, Field, ValidationError
from enum import Enum
 
class TraineeProfile(BaseModel):
    name: str
    years_experience: int = Field(ge=0)
    current_role: str
    target_role: str = "AI Engineer"
    skills: list[str] = []


good = '{"name":"Ana","years_experience":7,"current_role":"BA", "target_role":"AI","skills":["Python","SQL"]}'
print(TraineeProfile.model_validate_json(good))

bad = '{"name":"Ana","years_experience":-2,"current_role":"BA"}'
try:
    TraineeProfile.model_validate_json(bad)
except ValidationError as e:
    print("Rejected as expected:\n", e)

#=====================================================================================================================

class ServiceCode(str, Enum):                                                                                                                                                
    NORMAL = "00"                                                                                                                                                            
    CONTRACT = "01" 

class EmployeeProfile(BaseModel):
    name: str
    department: str
    service_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    service_code: ServiceCode = ServiceCode.NORMAL
    echelon: int = Field(ge=1, le=10)
    email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    phone: str = Field(pattern=r"^\+?\d{10,15}$")
    gender: str = Field(pattern=r"^(Male|Female|Other)$")

good_employee = '{"name":"Ana","department":"IT","service_date":"2023-01-01","service_code":"00",' \
'"echelon":5,"email":"ana@company.com","phone":"+1234567890","gender":"Female"}'
print(EmployeeProfile.model_validate_json(good_employee))

bad_employee = '{"name":"Ana","department":"IT","service_date":"202-01-01","service_code":"02",' \
'"echelon":5,"email":"ana@company.com","phone":"+1234567890","gender":"Female"}'
try:
    EmployeeProfile.model_validate_json(bad_employee)   
except ValidationError as e:
    print("Rejected as expected:\n", e)

#=====================================================================================================================

class movie_genre(str, Enum):
    ACTION = "Action"
    COMEDY = "Comedy"
    DRAMA = "Drama"
    HORROR = "Horror"
    ROMANCE = "Romance"
    SCIFI = "Sci-Fi"

class Movie(BaseModel):
    title: str
    director: str
    release_year: int = Field(ge=1888)
    genre: movie_genre
    rating: float = Field(ge=0, le=5)
    duration_minutes: int = Field(ge=1)

good_movie = Movie(title="Inception", director="Christopher Nolan", release_year=2010, genre=movie_genre.SCIFI,
                          rating=4.5, duration_minutes=148).model_dump_json()
print('MOVIE : ', Movie.model_validate_json(good_movie))
try:
    bad_movie = Movie(title="Inception", director="Christopher Nolan", release_year=2010, genre='Romance',
                          rating=9, duration_minutes=148)
except ValidationError as e:
    print("Rejected as expected:\n", e)