# coding: utf-8
from enum import Enum


class StatusEnum(Enum):
    """Перечисление для статусов заявок"""

    NEW = 'НА РАССМОТРЕНИИ'
    NEED_REWORK = 'ТРЕБУЕТСЯ ДОРАБОТКА'
    DECLINE = 'ОТКЛОНЕНА'
    ACCEPT = 'ПРИНЯТА'


    # STATUSES_CHOICES = (
    #     (NEW, 'НОВАЯ'),
    #     (NEED_REWORK, 'ТРЕБУЕТСЯ ДОРАБОТКА'),
    #     (DECLINE, 'ОТКЛОНЕНА'),
    #     (ACCEPT, 'ПРИНЯТА')
    # )

    # @classmethod
    # def get_choices(cls):
    #     return tuple(key[0] for key in cls.STATUSES_CHOICES)
