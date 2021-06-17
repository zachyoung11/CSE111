import tkinter as tk
import math
def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 250
    tree_height = 150
    draw_ground(canvas, 0, 350)
    draw_sky(canvas, 0, 0)
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center - 200, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center - 75, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center - 100, tree_top + 10, tree_height)
    draw_pine_tree(canvas, tree_center + 10, tree_top + 10, tree_height + 10)
    draw_pine_tree(canvas, tree_center + 240, tree_top, tree_height - 25)
    draw_pine_tree(canvas, tree_center + 50, tree_top, tree_height + 10)
    draw_pine_tree(canvas, tree_center + 110, tree_top + 30, tree_height)
    draw_pine_tree(canvas, tree_center + 70, tree_top + 15, tree_height + 10)
    draw_pine_tree(canvas, tree_center - 150, tree_top - 35, tree_height+80)
    draw_pine_tree(canvas, tree_center + 180, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center - 30, tree_top - 70, tree_height+ 200)
    draw_pine_tree(canvas, tree_center + 290, tree_top, tree_height+ 100)
    draw_pine_tree(canvas, tree_center - 275, tree_top + 35, tree_height- 75)
    draw_pine_tree(canvas, tree_center -240, tree_top + 20, tree_height)
    draw_pine_tree(canvas, tree_center - 410, tree_top, tree_height-10)
    draw_pine_tree(canvas, tree_center - 350, tree_top, tree_height+10)
    draw_pine_tree(canvas, tree_center - 380, tree_top, tree_height+40)
    draw_pine_tree(canvas, tree_center - 475, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center - 490, tree_top, tree_height+80)
    draw_pine_tree(canvas, tree_center - 300, tree_top + 75, tree_height)
    draw_moon(canvas, 50, 50)
    draw_stars(canvas, 200, 200)
    draw_stars(canvas, 450, 100)
    draw_stars(canvas, 750, 50)
    draw_stars(canvas, 499, 29)
    draw_stars(canvas, 600, 99)
    draw_stars(canvas, 100, 267)
    draw_stars(canvas, 290, 155)
    draw_stars(canvas, 225, 20)
    draw_stars(canvas, 530, 200)
    draw_stars(canvas, 620, 265)
    draw_stars(canvas, 715, 222)
    draw_clouds(canvas, 250, 150)
    draw_clouds(canvas, 280, 180)
    draw_clouds(canvas, 175, 200)
    draw_clouds(canvas, 580, 70)
    draw_clouds(canvas, 550, 0)
    draw_clouds(canvas, 600, 90)
    draw_clouds(canvas, 600, 20)
    draw_clouds(canvas, 700, 60)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_moon(canvas, x, y):
    moon_width = 100
    moon_height = 100
    canvas.create_oval(x, y, moon_width, moon_height, fill = "khaki1", width = False)

def draw_clouds(canvas, cloud_left, cloud_top):
    cloud_width = 150
    cloud_height = 60

    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
    cloud_center_x = cloud_left + (cloud_width/2)
    cloud_center_y = cloud_top + (cloud_height/2)

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill = "lightsteelblue1", width = False)

def draw_stars(canvas, star_left, star_top):
    star_width = 5
    star_height = 5
    ray_length = 6
    ray_width = 1
    ray_count = 10

    star_right = star_left + star_width
    star_bottom = star_top + star_height
    star_center_x = star_left + (star_width/2)
    star_center_y = star_top + (star_height/2)

    canvas.create_oval(star_left, star_top, star_right, star_bottom, fill = "yellow")
    
    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = star_center_x + math.cos(angle) * ray_length
        ray_y = star_center_y + math.sin(angle) * ray_length
        canvas.create_line(star_center_x, star_center_y, ray_x, ray_y, width = ray_width, fill = "yellow")

def draw_ground(canvas, x, y):
    ground_length = 800
    ground_height = 500
    canvas.create_rectangle(x, y, ground_length, ground_height, fill = "tan4")

def draw_sky(canvas, x, y):
    canvas.create_rectangle(x, y, 800, 350, fill = "midnightBlue")

    


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

# Call the main function so that
# this program will start executing.
main()