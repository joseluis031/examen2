import threading

saldo = 100
lock = threading.Lock()

def ingresar(cantidad):
    global saldo
    with lock:
        saldo += cantidad

def retirar(cantidad):
    global saldo
    with lock:
        saldo -= cantidad

# Crear los procesos de ingreso
for i in range(40):
    threading.Thread(target=ingresar, args=(100,)).start()
for i in range(20):
    threading.Thread(target=ingresar, args=(50,)).start()
for i in range(60):
    threading.Thread(target=ingresar, args=(20,)).start()

# Crear los procesos de retiro
for i in range(40):
    threading.Thread(target=retirar, args=(100,)).start()
for i in range(20):
    threading.Thread(target=retirar, args=(50,)).start()
for i in range(60):
    threading.Thread(target=retirar, args=(20,)).start()

# Esperar a que todos los procesos terminen
for thread in threading.enumerate():
    if thread is not threading.current_thread():
        thread.join()

# Comprobar que el saldo final es 100
if saldo == 100:
    print("El saldo final es correcto: 100 euros.")
else:
    print(f"El saldo final es incorrecto: {saldo} euros.")
