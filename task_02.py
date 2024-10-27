import turtle
import math

def draw_branch(t, branch_length, angle, level):
    """
    Функція для рекурсивного малювання дерева Піфагора.
    
    Аргументи:
    - t: об'єкт turtle, який малює дерево.
    - branch_length: довжина поточної гілки.
    - angle: кут нахилу гілки.
    - level: поточний рівень рекурсії.
    """

    if level == 0:
        return
    
    t.forward(branch_length)

    position = t.position()
    heading = t.heading()

    t.left(angle)
    draw_branch(t, branch_length * 0.7, angle, level - 1)

    t.setposition(position)
    t.setheading(heading)

    t.right(angle)
    draw_branch(t, branch_length * 0.7, angle, level - 1)

    t.setposition(position)
    t.setheading(heading)

def main():
    window = turtle.Screen()
    window.title("фрактал “дерево Піфагора”")

    t = turtle.Turtle()
    t.speed('fastest')
    t.left(90)

    branch_length = 100
    angle = 30
    recursion_level = int(input("Введіть рівень рекурсії: "))

    draw_branch(t, branch_length, angle, recursion_level)
    window.mainloop()

main()

