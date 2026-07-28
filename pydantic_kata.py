from pydantic import BaseModel, Field, ValidationError
 
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
