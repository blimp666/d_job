# coding: utf-8
from enum import Enum


class StatusEnum(Enum):
    """Перечисление для статусов заявок"""

    NEW = 'НА РАССМОТРЕНИИ'
    DECLINE = 'ОТКЛОНЕНА'
    ACCEPT = 'ПРИНЯТА'

    STATUSES_CHOICES = (
        (NEW, 'НОВАЯ'),
        (DECLINE, 'ОТКЛОНЕНА'),
        (ACCEPT, 'ПРИНЯТА')
    )

    @classmethod
    def get_choices(cls):
        return tuple(key[1] for key in cls.STATUSES_CHOICES.value)
