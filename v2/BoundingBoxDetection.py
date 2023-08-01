import tkinter as tk

def on_mouse_move(event):
    # Get the cursor position
    x, y = event.x, event.y
    # Perform bounding box detection on the region of interest around the cursor position
    # Update the bounding boxes and redraw the frame with the detected boxes

# Create a tkinter window
root = tk.Tk()
root.title("Real-Time Bounding Box Detection")

# Load your frame or image (replace with your own code to load the frame)
frame = tk.PhotoImage(file="path_to_your_frame.png")

# Create a canvas to display the frame
canvas = tk.Canvas(root, width=frame.width(), height=frame.height())
canvas.pack()

# Bind the mouse movement event to the on_mouse_move function
canvas.bind("<Motion>", on_mouse_move)

# Display the frame
canvas.create_image(0, 0, anchor=tk.NW, image=frame)

# Run the tkinter event loop
root.mainloop()
