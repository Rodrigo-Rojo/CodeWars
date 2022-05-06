"""
Welcome to the world of the National Football League!

In the NFL the Triple Crown is given when a receiver has the most receiving yards, the most receiving touchdowns and the most receptions in a single season.

This year Cooper Kupp managed to get it, however it is quite rare because the last one was in 2005 by Steve Smith.

Now you will receive a dictionary with the following keys (will always contain each):

    Cooper Kupp

    Justin Jefferson

    Davante Adams

Each key will have another dictionary as their values with the following keys:

    Receiving yards (value between 1500-2000)

    Receiving touchdowns (value between 10-20)

    Receptions (value between 90-120)

If one receiver has the most in each category you have to return his name. If there is no receiver with the most values in all categories you should return 'None of them'.

Example:

{
  'Cooper Kupp': 
    {
    'Receiving yards': 1786, 
    'Receiving touchdowns': 18, 
    'Receptions': 117
    },
  'Justin Jefferson': 
    {
    'Receiving yards': 1700, 
    'Receiving touchdowns': 17, 
    'Receptions': 115
    },
  'Davante Adams': 
    {
    'Receiving yards': 1650, 
    'Receiving touchdowns': 16, 
    'Receptions': 110
    }
}

# The output should be 'Cooper Kupp' since he has more receiving yards, more receiving touchdowns and more receptions as well

Example with two receivers sharing values in at least one category:

{
  'Cooper Kupp': 
    {
    'Receiving yards': 1900, 
    'Receiving touchdowns': 18, 
    'Receptions': 117
    },
  'Justin Jefferson': 
    {
    'Receiving yards': 1800, 
    'Receiving touchdowns': 17, 
    'Receptions': 116
    },
  'Davante Adams': 
    {
    'Receiving yards': 1900, 
    'Receiving touchdowns': 18, 
    'Receptions': 110
    }
}

# The output should be 'None of them' since they are tied on receiving yards and receiving touchdowns
"""

def triple_crown(receivers):
    first = receivers['Cooper Kupp']
    second = receivers['Justin Jefferson']
    third = receivers['Davante Adams']
    winner = []
    for (k, v), (ke, va), (key, value) in zip(first.items(), second.items(), third.items()):
        if v > va and v > value:
            winner.append('Cooper Kupp')
        elif va > v and va > value:
            winner.append('Justin Jefferson')
        elif value > v and value > va:
            winner.append('Davante Adams')
    if all(x == winner[0] for x in winner) and len(winner) == 3:
        return winner[0]
    return "None of them"
  
 
