import os
import eyed3
import random
import shutil
import re

def geraListasDeAcordoComTags():
    listaMusicasRapidas = [];
    listaMusicasLentas = [];
    for f in os.listdir("Forró"):
        audioFile = eyed3.load("Forró/" + f)
        tag = audioFile.tag
        ##100 pra cima é rápido
        #if(tag.genre is not None and tag.genre.name == "Xote"):
        if(tag.title == "silencio"):
            continue
        elif(tag.bpm > 100):
            listaMusicasRapidas.append(f);
        else:
            listaMusicasLentas.append(f)
    return listaMusicasRapidas, listaMusicasLentas

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
        

def geraPlaylistDestino(listaMusicasRapidas, listaMusicasLentas, nomePlaylist):
    indiceMusicaAtual = 'A';
    indiceBlocoAtual = 1;
    random.shuffle(listaMusicasRapidas)
    random.shuffle(listaMusicasLentas)
    musicaRapida = True;
    for x in range(0,3):
        insereSilencio(indiceMusicaAtual, indiceBlocoAtual)
        for y in range(0,2):
            indiceMusicaAtual = chr(ord(indiceMusicaAtual) + 1);
            if(musicaRapida == True):
                if(listaMusicasRapidas):
                    musicaAleatoria = listaMusicasRapidas.pop();
                else:
                    musicaAleatoria = None;
            else:
                if(listaMusicasLentas):
                    musicaAleatoria = listaMusicasLentas.pop();
                else:
                    musicaAleatoria  = None;
            if(musicaAleatoria is not None):
                nomeMusicaASerAdicionada = retornaNomeArquivoNoPadrao(indiceMusicaAtual, indiceBlocoAtual, musicaAleatoria)
                shutil.copy("Forró/" + musicaAleatoria, nomePlaylist +"/" + nomeMusicaASerAdicionada)
            
        musicaRapida =  not musicaRapida;

        indiceBlocoAtual +=1
        indiceMusicaAtual = 'A';
    return


listaMusicasRapidas, listaMusicasLentas = geraListasDeAcordoComTags()
nomePlaylist="playlist_destino"
criaDiretorioDestino(nomePlaylist)
geraPlaylistDestino(listaMusicasRapidas, listaMusicasLentas, nomePlaylist)


#usar random.sample(listaMusicasRapidas, k) ou shuffle + pop




