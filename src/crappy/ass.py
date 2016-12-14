'''
Created on 14/12/2016

@author: ernesto
'''


import logging

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

def numero_magicaca_lento_core(numero):
	dividendo_act = 1
	maximas_posiciones = 0
	numeros_vistos = set()
	
	logger_cagada.debug("calculando para %u" % numero)
	
	while(numero // dividendo_act):
		maximas_posiciones += 1
		dividendo_act *= 10
	logger_cagada.debug("la max pos del num %u es %u" % (numero, maximas_posiciones))
	
	maximas_posiciones = 5
	
	num_act = numero
	while(num_act != 1 and num_act not in numeros_vistos):
		num_act_tmp = 0
		dividendo_act = 1
		for posicion in range(maximas_posiciones):
			lomberto = (num_act // dividendo_act) % 10
			logger_cagada.debug("sumando mierda %u de %u" % (lomberto ** 2, lomberto))
			num_act_tmp += lomberto * lomberto
			dividendo_act *= 10
		
		logger_cagada.debug("el unm act calculado es %u" % num_act_tmp)
		
		numeros_vistos.add(num_act)
		num_act = num_act_tmp
	
	return num_act == 1

def numero_magicaca_main():
	for mierda in range(1, 400):
		crap = numero_magicaca_lento_core(mierda)
		logger_cagada.debug("el num %u es magico %s" % (mierda, crap))

if __name__ == '__main__':
	FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
	logging.basicConfig(level=nivel_log, format=FORMAT)
	logger_cagada = logging.getLogger("asa")
	logger_cagada.setLevel(nivel_log)
	numero_magicaca_main()
