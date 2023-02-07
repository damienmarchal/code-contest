# Code elevator algorithme d'un ascenseur
# API Rest: Serveur de scoring.

# Bibliotheques a importer
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ascenseur import Ascenseur

import unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

app = FastAPI()  #créer un objet FastAPI
app.add_middleware(
    CORSMiddleware,   # Cors permet d'autoriser l'accès à des ressources d'origine différente ( ex requêtes fetch sur serveur API)
    allow_origins=["*"] , #permet d'éviter les erreurs d'accès au serveur API lors du fetch
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)    

ascenseur = Ascenseur(0,5,0)

#GET /nextCommand
#    The response body must contain either NOTHING, UP, DOWN, OPEN or CLOSE
#GET /call ?atFloor=[0-5]&to=[UP|DOWN]
#GET /go ?floorToGo=[0-5]
#GET /userHasEntered
#GET /userHasExited
#GET /reset ?cause=information+message

@app.get("/nextCommand") 
async def nextCommand():
    return ascenseur.nextCommand()

@app.get("/call")  
async def call(atFloor : int, to : str):
    return ascenseur.call(atFloor, to)

@app.get("/go")  
async def go(floorToGo):
    return ascenseur.go(floorToGo)

@app.get("/userHasEntered")  
async def userHasEntered():
    return ascenseur.userHasEntered()

@app.get("/userHasExited")  
async def userHasExited():
    return ascenseur.userHasExited()

@app.get("/reset")  
async def reset(cause):
    return ascenseur.reset(cause)


