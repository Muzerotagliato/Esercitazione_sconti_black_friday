class Utente:
    def __init__(self, username, password):     #costruttore
        self.__username=username
        self.__password=password
        self.__codice_sconto=False

    def set_codice_sconto(self,valore):         #per aggiornare il valore di verità del codice sconto
        self.__codice_sconto=valore

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_codice_sconto(self):
        return self.__codice_sconto


def assegna_sconti(numero_sconti):
    clienti = []
    k = 1
    while True:
        username = input(f"\nInserisci nome utente{k}: ")
        password = input("Inserire la password: ")
        utente = Utente(username, password)

        clienti.append(utente)
        tasto = input("\nPremere invio per inserire  un altro utente (un tasto qualsiasi per terminare)\n")

        if tasto == "":
            k += 1
            # pass
        else:
            break

    #######################
    print(f"\nCi sono {len(clienti)} clienti per un totale di {numero_sconti} sconti\n")
    #######################

    # Assegnazione sconti
    sconti_rimasti = numero_sconti

    for utente in clienti:

        if sconti_rimasti <= 0:
            break

        utente.set_codice_sconto(True)
        sconti_rimasti = sconti_rimasti - 1

    for utente in clienti:
        print(
            f"Utente: {utente.get_username()}\nPassword: {utente.get_password()}\nCodice sconto: {utente.get_codice_sconto()}\n")

