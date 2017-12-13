#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from datetime import datetime
from datetime import timedelta


# global variables of this module
date = datetime.now()

def increase_day():
    "Aumenta o dia global da aplicação em 1"
    global date
    date = date + timedelta(days=1)
    return date


def overlap_dates(start1, end1, start2, end2):
    "Calcula se dois intervalos (start, end) de dias sobrepõe"
    latest_start = max(start1, start2)
    earliest_end = min(start2, end2)
    overlap = (earliest_end - latest_start).days + 1

    return True if overlap > 0 else False


class Vehicle(object):
    """Classe que representa um veículo

    :brand: marca do veículo
    :model: modelo do veículo
    :year: ano do veículo
    :daily: valor da diária do veículo
    """

    code = 0 # sequential id
    objects = [] # set of objects to track

    def __init__(self, brand, model, year, daily):
        self.brand = brand
        self.modelo = model
        self.year = year
        self.daily = daily
        self.code = Vehicle.code
        Vehicle.code += 1
        Vehicle.objects.append(self)
        print(self)

    def __repr__(self):
        return "<{}>".format(tuple('{}:{}'.format(k, v) for k,v in vars(self).items()))

    @staticmethod
    def search(code):
        "Procura determinado objeto da memória baseado no id"
        for obj in Vehicle.objects:
            if obj.code == code:
                return obj

    @staticmethod
    def delete(code):
        "Remove determinado carro da lista de objetos"
        Vehicle.objects.remove(Vehicle.search(code))


class RentVehicle(Vehicle):
    """Veículo alugável

    Parâmetros adicionais:
    :clients: dicionário com clientes e as datas na forma
              {name: (start_date, days_to_rent)}

    """

    def __init__(self, brand, model, year, daily):
        super().__init__(brand, model, year, daily)
        self.clients = {}

    def rent(self, client, rent_date_start, rent_days):
        """Aluga ou reserva este determinado carro
        :client: string com nome do cliente
        :date_start: datetime object com a data de início de aluguel
        :rent_days: int com o prazo de dias para ser alugado
        """

        self.clients[client] = (rent_date_start, rent_days)


    def search_rent(self, rent_date_start , rent_days):
        "Procura por possíveis clientes alugando este carro"
        rent = []
        rent_date_end = rent_date_start + timedelta(days=rent_days)
        for client, (date_start, days) in self.clients.items():
            date_end = date_start + timedelta(days=days)
            if overlap_dates(rent_date_start, rent_date_end, date_start, date_end):
                rent.append((client, date_start, date_end))
        return rent


    @staticmethod
    def get_alugados():
        return [] # a ser implementado

    @staticmethod
    def get_atrasos():
        return 0 # a ser implementado

    def free(self, client):
        "Libera o carro de aluguel ou reserva"
        del self.clients[renter_name]


    @property
    def total_to_pay(self, client):
        "Valor a ser pago baseado na data atual e a data alugada"
        rent_date_start, rent_days = self.clients[client]
        total_days_rent = (rent_date_start - date)
        total_value = min(total_days_rent, rent_days) * daily
        # multa
        if total_days_rent > rent_days:
            total_value += (total_days_rent - rent_days)*daily*2
        return total_value
