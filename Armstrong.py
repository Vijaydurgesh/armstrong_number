from fastapi import FastAPI
app = FastAPI()
def is_armstrong(num: int):
    num_str = str(num)
    len_str = len(num_str)
    power = sum(int(digit)**len_str for digit in num_str)
    return num==power
@app.get("/armstrong")
def check_armstrong(n: int):
    if is_armstrong(n):
        return {"Armstrong Number"}
    else:
        return {"Not Armstrong number"}