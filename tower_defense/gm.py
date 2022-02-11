from enemy import Enemy
from projectile import Projectile
from fighter import Fighter
from vector import Vector

# Do to vectors occupy a close space (in this instance, vectors are in fact points)
def collision(rhs: Vector, lhs: Vector) -> bool:
    """"Finds collisions between enemies and projectiles, damages enemies and removes them if they die. Destroys projectiles."""
    distance_vector: Vector = lhs - rhs
    distance: Vector = distance_vector.magnitude()
    if(distance < 20):
        return True
    else: return False



