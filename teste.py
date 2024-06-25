import jogoBatalha
import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="dbGame",
        user="avnadmin",
        password="AVNS_I2YSg3hf2GFrMM8X7eZ",
        host="pg-126b320f-ncgaloni-ec04.d.aivencloud.com",
        port="21577"
    )

conn = connect_db()
print("Bem-vindo ao jogo de batalha!")

jogadores = jogoBatalha.get_jogadores(conn)
print("(jogador_id, jogador_id, nome, apelido, nivel, classe")
for jogador in jogadores:
    print(jogador)