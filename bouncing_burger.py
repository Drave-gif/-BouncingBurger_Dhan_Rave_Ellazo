import tkinter as tk
from PIL import Image, ImageTk
import random

# --- Configuration ---
WIDTH, HEIGHT = 800, 600
VX, VY = 3, 2
IMAGE_FILE = "burger.png"  # Make sure this image is in the same folder
NAME_TEXT = "Dhanrave S. Ellazo"
FPS = 16  # ~60 FPS

class BouncingBurgerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Burger - Dhanrave S. Ellazo")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1a1a1a")
        self.canvas.pack()

        # Load and enlarge burger image
        self.burger_img = Image.open(IMAGE_FILE)
        self.burger_img = self.burger_img.resize((250, 250), Image.Resampling.LANCZOS)
        self.tk_burger = ImageTk.PhotoImage(self.burger_img)

        # Initial position and state
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.vx, self.vy = VX, VY
        self.paused = False

        # Draw image and text
        self.image_id = self.canvas.create_image(self.x, self.y, image=self.tk_burger)
        self.text_id = self.canvas.create_text(
            self.x, self.y,
            text=NAME_TEXT,
            fill="white",
            font=("Helvetica", 14, "bold"),
            justify="center"
        )

        # Bind keys
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Start animation
        self.animate()

    def animate(self):
        if not self.paused:
            self.x += self.vx
            self.y += self.vy

            # Adjusted margins for bigger image
            if self.x >= WIDTH - 125 or self.x <= 125:
                self.vx *= -1
                self.change_color()

            if self.y >= HEIGHT - 125 or self.y <= 125:
                self.vy *= -1
                self.change_color()

            # Move items
            self.canvas.coords(self.image_id, self.x, self.y)
            self.canvas.coords(self.text_id, self.x, self.y)

        self.root.after(FPS, self.animate)

    def toggle_pause(self, event):
        self.paused = not self.paused

    def change_color(self):
        # Random background color
        r = lambda: random.randint(0, 255)
        color = f'#{r():02x}{r():02x}{r():02x}'
        self.canvas.configure(bg=color)

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBurgerApp(root)
    root.mainloop()
