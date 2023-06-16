from typing import Final, List, Set, Tuple

def walk(n_max: int, n: int, x: int, y: int, used: Set[Tuple[int, int]]) -> int:
  """
  Recursieve functie om het aantal self avoiding walks te berekenen. 
  De functie genereert SAWs in een depth-first manier en maakt gebruikt van backtracking
  om dubbele te verkomen en een hash-set om overlap te voorkomen.


  Args:
    n_max   - Lengte van de wandeling
    n       - Hoe ver we in de wandeling zijn
    x       - Huidige x locatie
    y       - Huidige y locatien

  Returns:
    Het aantal SAWs met een lengte n_max
    
  """
  # Mogelijke verplaatsingen op een vierkant rooster
  dr_vals: Final[List[Tuple[int, int]]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]

  # Einde van de recursie, er is een SAW gemaakt. 
  if n==n_max:
    return 1

  # Maak locatie (x,y) onbeschikbaar voor volgende stappen 
  used.add((x,y))

  # Recursie: stappen vanaf from (x,y)
  walks = 0

  # Kijk naar alle mogelijke kanten die de SAW op kan gaan
  for dr in dr_vals:
    # Bepaling van de volgende coordinaat
    nx = x + dr[0]
    ny = y + dr[1]
    # Check of de buren beschikbaar zijn
    if (nx, ny) in used:
      continue
    # Ga naar het buurvierkant en tel hoeveel wandelingen die heeft
    walks += walk(n_max, n + 1, nx, ny, used)

  

  # Terug naar de stack, dus (x,y) mag weer gebruikt worden
  used.remove((x,y))

  return walks

def main():
  # Geeft als output een table can hoeveel wandelingen er zijn voor lengte n
  # Door de exponentiele toename in computatietijd, wordt voor n>15 de bereking te lang
  for n in range(10):
    used: Set[Tuple[int, int]] = set([(1000, 1000)])
    print(n, walk(n, 0, 0, 0, used))

main()
