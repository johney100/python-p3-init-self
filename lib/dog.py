#!/usr/bin/env python3

class Dog:
    # Remember that all methods use "self." We'll elaborate on this in a moment.
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed