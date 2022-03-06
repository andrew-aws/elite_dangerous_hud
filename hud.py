from tkinter import colorchooser
import numpy as np
import webbrowser
import colorsys

def map_colors():
    input_colors = {
        "orange": [238,64,0],
        "green": [13,142,22],
        "blue": [114,210,255]
    }
    output_colors = {}

    for color in input_colors:
        color_rgb = colorchooser.askcolor(title =f"Choose color map for {color}")[0]
        output_colors[color] = color_rgb

    input_list = []

    for color in input_colors:
        input_list.append(input_colors[color] + [0 for i in range(6)])
        input_list.append([0 for i in range(3)] + input_colors[color] + [0 for i in range(3)])
        input_list.append([0 for i in range(6)] + input_colors[color])

    matrix = np.array(input_list)
    vector = np.array([x for color in output_colors for x in output_colors[color]])
    output = np.linalg.solve(matrix,vector)
    output_matrix = np.array([[output[3*i+j] for i in range(3)] for j in range(3)])

    w,v = np.linalg.eig(output_matrix)
    v = v*255
    print("Eigenvalues: ")
    print('{}'.format(", ".join(["{:.2f}".format(x) for x in w])))
    print("Eigenvectors: ")
    print('{}'.format(", ".join(["{:.2f}".format(x) for x in v[0]])))
    print('{}'.format(", ".join(["{:.2f}".format(x) for x in v[1]])))
    print('{}'.format(", ".join(["{:.2f}".format(x) for x in v[2]])))

    print(
        f"\t\t\t<MatrixRed>   {output_matrix[0][0]:.2f}, {output_matrix[0][1]:.2f}, {output_matrix[0][2]:.2f} </MatrixRed>\n"
        f"\t\t\t<MatrixGreen> {output_matrix[1][0]:.2f}, {output_matrix[1][1]:.2f}, {output_matrix[1][2]:.2f} </MatrixGreen>\n"
        f"\t\t\t<MatrixBlue>  {output_matrix[2][0]:.2f}, {output_matrix[2][1]:.2f}, {output_matrix[2][2]:.2f} </MatrixBlue>"
        )


    url = "http://arkku.com/elite/hud_editor/#theme_{}".format("_".join(["{:.2f}".format(x) for y in output_matrix for x in y]))

    webbrowser.open(url)


if __name__ == "__main__":
    map_colors()
