import os
import eyed3
import random
import shutil
import re

def geraListasDeAcordoComTags():
    listaMusicasLentas = [];
    listaMusicasMedias = [];
    listaMusicasRapidas = [];
    for f in os.listdir("Forró"):
        audioFile = eyed3.load("Forró/" + f)
        tag = audioFile.tag
        ##100 pra cima é rápido
        #if(tag.genre is not None and tag.genre.name == "Xote"):

        if(tag.title is not None and tag.title == "silencio"):
            continue
        elif(tag.bpm is not None and tag.bpm < 100 and tag.genre is not None and tag.genre.name == "Xote"):
            listaMusicasLentas.append(f)
        elif(tag.bpm is not None and tag.bpm < 100):
            listaMusicasMedias.append(f)
        elif(tag.bpm is not None and tag.bpm >= 100):
            listaMusicasRapidas.append(f);
    return listaMusicasLentas, listaMusicasMedias, listaMusicasRapidas

def retornaNomeArquivoNoPadrao(indiceMusicaAtual, indiceBlocoAtual, musicaAleatoria ):
    audioFile = eyed3.load("Forró/" + musicaAleatoria)
    tag = audioFile.tag
 
    if(tag.genre is None):
        return (str(indiceBlocoAtual).zfill(2) +
            indiceMusicaAtual + " (" + str(tag.bpm).zfill(3) + "bpm)" +
            tag.artist.replace("/", ",")+ " - " + tag.title +".mp3" )
    return (str(indiceBlocoAtual).zfill(2) +
            indiceMusicaAtual + " (" + str(tag.bpm).zfill(3) + "bpm)(" + tag.genre.name +") " +
            tag.artist.replace("/", ",")+ " - " + tag.title +".mp3" )
   
def criaDiretorioDestino(nomePlaylist):
    if not os.path.exists(nomePlaylist):
        os.mkdir(nomePlaylist)
    else:
        shutil.rmtree(nomePlaylist)
        os.mkdir(nomePlaylist)
    return

def insereSilencio(indiceMusicaAtual, indiceBlocoAtual):
    nomeArquivoSilencioDestino = (str(indiceBlocoAtual).zfill(2) +
            indiceMusicaAtual + " silencio.mp3")
    shutil.copy("Forró/" + "silencio.mp3", nomePlaylist +"/" + nomeArquivoSilencioDestino)

def atualizaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido):
    if(estiloBlocoLento == True):
        estiloBlocoLento = False;
        estiloBlocoMedio = True;
        estiloBlocoRapido = False;
        return estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido
    elif (estiloBlocoMedio == True):
        estiloBlocoLento = False;
        estiloBlocoMedio = False;
        estiloBlocoRapido = True;
        return estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido
    elif(estiloBlocoRapido == True):
        estiloBlocoLento = True;
        estiloBlocoMedio = False;
        estiloBlocoRapido = False;
        return estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido

def verificaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido):
    if(estiloBlocoLento == True):
        return 'Lento'
    if(estiloBlocoMedio == True):
        return 'Medio'
    if(estiloBlocoRapido == True):
        return 'Rapido'

def geraPlaylistDestino(listaMusicasLentas, listaMusicasMedias, listaMusicasRapidas, nomePlaylist):
    indiceMusicaAtual = 'A';
    indiceBlocoAtual = 1;
    random.shuffle(listaMusicasLentas)
    random.shuffle(listaMusicasMedias)
    random.shuffle(listaMusicasRapidas)
    estiloBlocoLento = False;
    estiloBlocoMedio = True;
    estiloBlocoRapido = False;
    tamanhoBloco = 3
    for x in range(0,3):
        insereSilencio(indiceMusicaAtual, indiceBlocoAtual)
        if(verificaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido) == 'Lento'):
            tamanhoBloco = 2;
        else:
            tamanhoBloco = 3;
        for y in range(0,tamanhoBloco):
            indiceMusicaAtual = chr(ord(indiceMusicaAtual) + 1);
            if(verificaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido) == 'Rapido' ):
                if(listaMusicasRapidas):
                    musicaAleatoria = listaMusicasRapidas.pop();
                else:
                    musicaAleatoria = None;
            elif(verificaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido) == 'Lento'):
                if(listaMusicasLentas):
                    musicaAleatoria = listaMusicasLentas.pop();
                else:
                    musicaAleatoria  = None;
            elif(verificaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido) == 'Medio' ):
                if(listaMusicasMedias):
                    musicaAleatoria = listaMusicasMedias.pop();
                else:
                    musicaAleatoria  = None;
            if(musicaAleatoria is not None):
                nomeMusicaASerAdicionada = retornaNomeArquivoNoPadrao(indiceMusicaAtual, indiceBlocoAtual, musicaAleatoria)
                shutil.copy("Forró/" + musicaAleatoria, nomePlaylist +"/" + nomeMusicaASerAdicionada)
            
        estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido = atualizaEstiloBloco(estiloBlocoLento, estiloBlocoMedio, estiloBlocoRapido)

        indiceBlocoAtual +=1
        indiceMusicaAtual = 'A';
    return


listaMusicasLentas, listaMusicasMedias, listaMusicasRapidas = geraListasDeAcordoComTags()
nomePlaylist="playlist_destino"
criaDiretorioDestino(nomePlaylist)
geraPlaylistDestino(listaMusicasLentas, listaMusicasMedias, listaMusicasRapidas, nomePlaylist)


#usar random.sample(listaMusicasRapidas, k) ou shuffle + pop




