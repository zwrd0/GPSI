# Imports
import os
from termcolor import colored
import time


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


def iniciar_venda():
	cls()
	lista = []
	preco = 0
	ask1 = ""
	
	palavras = []
	while ask1 != "STOP":
		f = open("items.txt", "r")
		flag = 0
		ask1 = input("ID do Produto (STOP para parar): ")

		
		for line in f:
			palavras = (line.split("/"))
			for check in palavras:
				if check == ask1:
					flag = 1	
				
		if flag == 1:
			lista.append(ask1)
			print(colored("Produto Adicionado", "green"))
			time.sleep(1)
			cls()
		elif flag == 0 and ask1 != "STOP":
			print(colored("Produto não encontrado!", "red"))
			time.sleep(1)
			cls()
		f.close()

	# # # # # # # # # # # # # # # # # # # # # # # # # # #


	print(colored("Venda Encerrada.", "red"))
	time.sleep(2)
	cls()
	f.close()
	f = open("items.txt", "r")
	linhas = f.readlines()
	f.close()

	for x in lista:
		for linha in linhas:
			linha = linha.replace("\n","").split("/")
			if linha[0] == x:
				preco += float(linha[2])
				print(">> " + linha[1] + " | " + linha[2] + "€")
	print()
	print("Total: " + str(preco) + "€")
	print()
	print()
	input(colored("Pressione Enter para continuar...", "blue"))
	cls()


def verificar_disponibilidade():
	f = open("items.txt", "r")
	item = input("Nome do item: ")
	flag = 0
		
	for line in f:
		palavras = (line.split("/"))
		for check in palavras:
			if check == item:
				flag = 1

	if flag == 1:
		print(colored("Item encontrado!", "green"))
	else:
		print(colored("Item não encontrado!", "red"))
	f.close()
	time.sleep(1)
	cls()
	
	
				
					

def listar_todos_produtos():
	cls()
	f = open("items.txt", "r")

	for line in f:
		linha = (line.split("/"))
		print(colored(linha[0], "blue") + " -", colored(linha[1], "green") + " |", colored(linha[2], "red"))

	f.close()
	print()
	print()
	input(colored("Pressione Enter para continuar...", "blue"))
	cls()
	


def add_produto():

	f = open("items.txt", "a")
	nome_produto = input("Produto: ")
	try:
		preco = float(input("Preço: "))
	except:
		print("O preço colocado não é válido!")
		exit()
	ID = input("ID: ")
		
	f.write("\n" + ID + "/" + nome_produto + "/" + str(preco))
	print(colored("Produto Adicionado", "green"))
	time.sleep(1)
	cls()
	f.close()
		



def menu():
	opc = ""
	while opc != 0:
		print("********************************")
		print("######### GPSI Mercado #########")
		print("********************************")
		print("1 - Iniciar Venda")
		print("2 - Verificar Disponiblidade de um Produto")
		print("3 - Listar todos os produtos")
		print("4 - Adicionar produto")
		print("0 - Sair")
		opc = int(input(">>> "))
		if opc == 1:
			iniciar_venda()
		if opc == 2:
			verificar_disponibilidade()
		if opc == 3:
			listar_todos_produtos()
		if opc == 4:
			add_produto()
		cls()


menu()
	
