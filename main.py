from typing import Optional
from fastapi import FastAPI

# import numpy as np
import tsp_c as tsp
# from python_tsp.heuristics import solve_tsp_simulated_annealing

app = FastAPI()


distance_matrix = [
	[0.0, 290.7, 254.9, 172.9, 335.7, 108.8, 148.0, 83.0, 141.9, 32.9],
	[263.6, 0.0, 508.3, 185.0, 562.1, 364.0, 283.3, 322.8, 283.3, 349.0],
	[258.2, 497.1, 0.0, 405.6, 379.8, 209.5, 321.8, 187.3, 378.5, 229.2],
	[136.8, 190.7, 394.8, 0.0, 288.7, 206.2, 313.5, 209.9, 93.8, 190.2],
	[280.2, 557.7, 397.8, 282.9, 0.0, 220.0, 433.3, 298.2, 214.6, 296.0],
	[128.1, 393.0, 253.3, 194.9, 187.5, 0.0, 288.8, 105.2, 156.9, 97.7],
	[160.0, 276.8, 343.4, 287.7, 483.2, 299.8, 0.0, 157.4, 296.8, 185.2],
	[75.3, 364.5, 197.5, 202.5, 343.7, 114.7, 193.5, 0.0, 214.2, 50.8],
	[153.0, 301.0, 388.3, 110.8, 191.4, 136.7, 335.9, 209.6, 0.0, 162.5],
	[30.5, 323.9, 248.8, 170.2, 266.4, 87.1, 206.4, 52.4, 162.3, 0.0]
]

"""
distance_matrix = np.array([
    [0,  5, 4, 10],
    [5,  0, 8,  5],
    [4,  8, 0,  3],
    [10, 5, 3,  0]
])
"""

@app.get("/")
async def root():
    return {"message": "Hello! My name is Udom"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/tsp/greedy")
def tsp_greedy():
    tour, distance = tsp.solve_greedy(distance_matrix)
    return {"message": "Solution from Greedy", "distance": distance, "tour": tour}

@app.get("/tsp/sa")
def tsp_sa():
    tour, distance = tsp.solve_SA(distance_matrix)
    # tour, distance = tsp.solve_greedy_tsp(distance_matrix)
    # tour, distance = solve_tsp_simulated_annealing(distance_matrix)
    return {"message": "Solution from Simulated Annealing", "distance": distance, "tour": tour}

@app.get("/tsp/pso")
def tsp_pso():
    tour, distance = tsp.solve_PSO(distance_matrix)
    return {"message": "Solution from PSO", "distance": distance, "tour": tour}