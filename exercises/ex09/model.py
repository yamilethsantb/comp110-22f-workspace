"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations

from math import cos, pi, sin, sqrt
from random import random

from exercises.ex09 import constants

__author__ = "730361444"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Distance between two points."""
        the_distance: float = sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return the_distance 


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        self.sickness = constants.VULNERABLE
 
    def tick(self) -> None:
        """To reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        if self.is_infected:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable(): 
            return "gray"
        if self.is_infected(): 
            return "red"
        if self.is_immune():
            return "green"
    
    def contract_disease(self) -> None: 
        """For cell to contract disease."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """If cell is vulerable."""
        if self.sickness == constants.VULNERABLE:
            return True 
        else: 
            return False 

    def is_infected(self) -> bool:
        """If cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False

    def contact_with(self, other: Cell) -> None:
        """Determines contact between cells."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()

    def immunize(self) -> None:
        """Immunize the cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Determines whether the cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True 
        else:
            False 


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0 

    def __init__(self, cells: int, speed: float, infected_cells: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells >= cells:
            raise ValueError("Incorrect number of cell objects infected.")
        if infected_cells <= 0: 
            raise ValueError("Incorrect number of cell objects infected.")
        m: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_location: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_location)
            self.population.append(cell)
            if m < infected_cells:
                cell.sickness = constants.INFECTED
            m += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0 
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0 

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        return False
        # while i > len(self.population):
        #     for cells in self.population:
        #         if cells.sickness == constants.VULNERABLE or constants.IMMUNE:
        #             i += 1
        #         else: 
        #             return False 
        # return True

    def check_contacts(self) -> None: 
        """Checks the contact between two cells."""
        start: Cell = self.population[0]
        second_point: Point = start.location
        for cell in self.population: 
            first_point: Point = cell.location 
            the_distance: float = first_point.distance(second_point)
            if the_distance < constants.CELL_RADIUS:
                start.contact_with(cell)