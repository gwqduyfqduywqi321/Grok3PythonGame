# Orbital Animation with Asteroids

## Description
This Python project uses Pygame to create an interactive orbital animation simulating a spaceship orbiting Earth, with features like an internal and external camera view, a radar system, and randomly moving asteroids. The program allows users to switch between views, control the ship's speed, and observe objects (Earth, asteroids, and space) via a radar in the internal view.

## Features
- **External View**: Shows Earth, the spaceship orbiting it, and asteroids moving chaotically in space.
- **Internal View**: Displays the interior of the spaceship with a floating astronaut and a radar tracking Earth, space, and asteroids.
- **Radar**: A circular radar in the internal view that detects and displays the relative positions of Earth (green dot), space (blue dot), and asteroids (yellow dots).
- **Speed Control**: Adjust the ship's orbital speed using the UP and DOWN arrow keys (limited between 0.01 and 0.1).
- **Camera Toggle**: Switch between internal and external views using the 'C' key.

## Requirements
- Python 3.x
- Pygame library (`pip install pygame`)

## How to Run
1. Clone this repository or save the `orbital_animation.py` file to your local machine.
2. Ensure you have Python and Pygame installed.
3. Run the script from the command line: `python orbital_animation.py`.
4. Use the following controls:
   - Press 'C' to toggle between Internal View and External View.
   - Use UP/DOWN arrow keys to increase/decrease the ship's speed.
   - Close the window to exit the program.

## Known Issues
- Asteroids may occasionally overlap or move off-screen before respawning.
- No collision detection is implemented between asteroids, the ship, or Earth.

## Future Improvements
- Add collision detection for asteroids and the ship.
- Implement sound effects for a more immersive experience.
- Enhance asteroid movement patterns or add more interactive elements.

## Credits
- Developed with inspiration and assistance from Grok 3 by xAI.
- Uses Pygame for graphics and game mechanics.

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it, but please retain this README and credit the original author.

## Contact
For questions or contributions, contact [Your Name/Email] or open an issue on this repository.
