import random


def get_ticket():
    s='1234567890qwertyuiopasdfghjklzxcvbnm'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)
    return ticket