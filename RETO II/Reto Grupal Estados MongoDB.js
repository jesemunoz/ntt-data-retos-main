use("Reto_Estados")
db.createCollection("Estados")
db.Estados.insertMany([
    {
    "Nombre": "Alabama",
    "2000": {"Poblacion": 4447100,
            "Residentes < 65 años":3870598,
            "Muertes":10622,    
            },
    "2001": {"Poblacion": 4451493,
            "Residentes < 65 años":3880476,
            "Muertes":15912,    
            },      
    "Latitud": 33.258882,
    "Longitud": -86.829534,
    "Fecha fundación": "14-12-1819"
    },
    {
    "Nombre": "Florida",
    "2000": {"Poblacion": 15982378,
            "Residentes < 65 años":13237167,
            "Muertes":38103,    
            },
    "2001": {"Poblacion": 17054000,
             "Residentes < 65 años":13548077,
             "Muertes":166069,    
            },      
    "Latitud": 27.756767,
    "Longitud": -81.463983,
    "Fecha fundación": "03-03-1845"
    },
    {
    "Nombre": "Georgia",
    "2000": {"Poblacion": 8186453,
            "Residentes < 65 años":7440877,
            "Muertes":14804,    
            },
    "2001": {"Poblacion": 8229823,
            "Residentes < 65 años":7582146,
            "Muertes":15000,    
            },      
    "Latitud": 32.329381,
    "Longitud": -83.113737,
    "Fecha fundación": "12-02-1733"
    },
    {
    "Nombre": "South Carolina",
    "2000": {"Poblacion": 4012012,
            "Residentes < 65 años":3535770,
            "Muertes":8581,    
            },
    "2001": {"Poblacion": 4023438,
            "Residentes < 65 años":3567172,
            "Muertes":9500,    
            },      
    "Latitud": 33.687439,
    "Longitud": -80.436374,
    "Fecha fundación": "26-03-1776"
    }
])      