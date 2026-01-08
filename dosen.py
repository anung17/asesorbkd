#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2026 Anung <anung@trisakti.ac.id>
# 2026-01-08 11:43
# Distributed under terms of the MIT license.

"""
Dosen Class definition
"""

class Dosen():
    def __init__(self, nama, jabamik, pendidikan):
        self.__name = nama
        self.__jabamik = jabamik
        self.__pendidikan = pendidikan

    def get_asesor(self, d1):
        pass

    def __str__(self):
        return f"Nama {self.__name}. Jabamik {self.__jabamik}.  Pendidikan terakhir {self.__pendidikan}"

    def __repr__(self):
        return f"Nama {self.__name}. Jabamik {self.__jabamik}.  Pendidikan terakhir {self.__pendidikan}"

