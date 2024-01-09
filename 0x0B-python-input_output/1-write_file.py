#!/usr/bin/python3
"""
Module 1-write_file

Contains function that writes to text file and returns num chars written
"""

def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
