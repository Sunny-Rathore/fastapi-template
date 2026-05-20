from passlib.context import CryptContext
pwt_context = CryptContext(schemes=['argon2'],deprecated="auto")

def hash_password(password:str)->str:
   print(f"Password : {password}")
   return pwt_context.hash(password)

def verify_password(password:str,hash:str,)-> bool:
    return pwt_context.verify(password,hash)