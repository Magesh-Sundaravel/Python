from pydantic import BaseModel


class User(BaseModel):
    id : int
    name : str
    is_active : bool = True


# Even if you give the DOUBLE QUOTES in ID variable it will take as INTEGER
u= User(id="101", name= "Magesh")
print(u)
print(type(u.id), u.id)


# You can also dump the values 
print(u.model_dump())


from pydantic import  ValidationError


class Product(BaseModel):
    id : int
    price : float
    in_stock : bool

# But here if you giving the mixture of STR and INTEGER it will throw a ERROR
try:
    p = Product(id="A1", price= "56.56", in_stock=True)
except ValidationError as e:
    print(e)



from pydantic import Field

class SignUp(BaseModel):
    username : str = Field(min_length=3, max_length=12)
    age : int = Field(ge=18, le=60)
    score : float = Field(default=0.0, ge=0, le=100)

# You can give the FIELD for the variables
try :
    s = SignUp(username="Magesh", age=27, score=200)
except ValidationError as e:
    print(e)

# Nested classes

class Address(BaseModel):
    city : str
    pincode : int

class Customer(BaseModel):
    name : str
    address : Address

payload = {
    "name" : "Magesh",
    "address" : {"city": "Chennai", "pincode" : "6062"} # string -> int
}



c = Customer(**payload)
print(c)

print(c.address.city)

print(c.name)
