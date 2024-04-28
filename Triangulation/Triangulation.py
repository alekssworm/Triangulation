
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

# Tower coordinates (example)
tower_coordinates = [(0, 0), (1, 1), (2, 0), (0.5, 1.5), (1.5, 1.5)]

# Create triangulation based on tower coordinates
x = [coord[0] for coord in tower_coordinates]
y = [coord[1] for coord in tower_coordinates]
triang = Triangulation(x, y)

# Visualize triangulation
plt.figure(figsize=(8, 6))
plt.gca().set_aspect('equal')
plt.triplot(triang, 'ko--', lw=1)  # Black triangles
plt.plot(x, y, 'ro')  # Red points - tower coordinates
plt.title('Cell Tower Triangulation')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.grid(True)
plt.show()
