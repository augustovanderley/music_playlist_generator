import os
import eyed3
import random
import shutil
import re


def retornaNomeArquivoNoPadrao(indiceMusicaAtual, indiceBlocoAtual, musicaAleatoria ):
    audioFile = eyed3.load("Forró/" + musicaAleatoria)
    tag = audioFile.tag
 
    if(tag.genre is None):
        return (str(indiceMusicaAtual).zfill(2) +
            indiceBlocoAtual + " (" + str(tag.bpm).zfill(3) + "bpm)" +
            tag.artist.replace("/", ",")+ " - " + tag.title +".mp3" )
    return (str(indiceMusicaAtual).zfill(2) +
            indiceBlocoAtual + " (" + str(tag.bpm).zfill(3) + "bpm)(" + tag.genre.name +") " +
            tag.artist.replace("/", ",")+ " - " + tag.title +".mp3" )
   


listaMusicasRapidas = [];
listaMusicasLentas = [];
for f in os.listdir("Forró"):
    audioFile = eyed3.load("Forró/" + f)
    tag = audioFile.tag
    ##100 pra cima é rápido
    #if(tag.genre is not None and tag.genre.name == "Xote"):
    if(tag.bpm > 100):
        listaMusicasRapidas.append(f);
    else:
        listaMusicasLentas.append(f)
        
print(listaMusicasRapidas)
print(listaMusicasLentas)
nomePlaylist="playlistMaio"
if not os.path.exists(nomePlaylist):
    os.mkdir(nomePlaylist)
else:
    shutil.rmtree(nomePlaylist)
    os.mkdir(nomePlaylist)
qntBlocos = 3;
indiceMusicaAtual = 1;
indiceBlocoAtual = 'A';
random.shuffle(listaMusicasRapidas)
random.shuffle(listaMusicasLentas)
musicaRapida = True;
for x in range(0,3):
    #blocox
    for y in range(0,2):
        if(musicaRapida == True):
            if(listaMusicasRapidas):
                musicaAleatoria = listaMusicasRapidas.pop();
            else:
                musicaAleatoria = None;
        else:
            if(listaMusicasLentas):
                musicaAleatoria = listaMusicasLentas.pop();
                print("Lista")
                print(listaMusicasLentas)
                print(musicaAleatoria)
            else:
                musicaAleatoria  = None;
        if(musicaAleatoria is not None):
            nomeMusicaASerAdicionada = retornaNomeArquivoNoPadrao(indiceMusicaAtual, indiceBlocoAtual, musicaAleatoria)
            shutil.copy("Forró/" + musicaAleatoria, nomePlaylist +"/" + nomeMusicaASerAdicionada)
        indiceMusicaAtual+= 1;
    musicaRapida =  not musicaRapida;
    indiceBlocoAtual = chr(ord(indiceBlocoAtual) + 1);

#usar random.sample(listaMusicasRapidas, k) ou shuffle + pop




