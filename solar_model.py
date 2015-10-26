# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += (gravitational_constant*body.m*obj.m/(r**2))*(abs(body.x-obj.x)/r)
        body.Fy += (gravitational_constant*body.m*obj.m/(r**2))*(abs(body.y-obj.y)/r)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.
    Параметры:
    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    ay=body.Fy/body.m
    body.x += body.Vx*dt+ax*dt**2/2  # FIXME: не понимаю как менять...
    body.Vx += ax*dt
    body.y+=body.Vy*dt+ay*dt**2/2
    body.Vy+=ay*dt
    # FIXME: not done recalculation of y coordinate!
