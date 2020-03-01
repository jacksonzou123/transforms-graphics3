from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, 'r')
    mode = 0
    for l in file:
        l = l.strip()
        if mode != 0:
            l = l.split(" ")
            if mode == "line":
                add_edge(points, int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]))
            if mode == "scale":
                transform = make_scale(int(l[0]), int(l[1]), int(l[2]))
            if mode == "move":
                transform = make_translate(int(l[0]), int(l[1]), int(l[2]))
            if mode == "rotate":
                if l[0] == "x":
                    transform = make_rotX(int(l[1]))
                if l[0] == "y":
                    transform = make_rotY(int(l[1]))
                if l[0] == "z":
                    transform = make_rotZ(int(l[1]))
            if mode == "save":
                clear_screen(screen)
                draw_lines(points, screen, color)
                save_ppm(screen, "test.ppm")
                save_extension(screen, l[0])
            mode = 0
        elif l == "line" or l == "scale" or l == "move" or l == "rotate" or l == "save":
            mode = l
        else: #l == "ident" or l == "apply" or l == "display" or l == "quit":
            if l == "ident":
                ident(transform)
            if l == "display":
                clear_screen(screen)
                draw_lines(points, screen, color)
                save_ppm_ascii(screen, "test.ppm")
                save_extension(screen, "test.png")
            if l == "apply":
                matrix_mult(transform, points)
