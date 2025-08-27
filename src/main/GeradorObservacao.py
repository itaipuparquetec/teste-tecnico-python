class GeradorObservacao:
    # Textos pré-definidos
    __umaNota = "Fatura da nota fiscal de simples remessa: "
    # Identificador da entidade
    __t = ""

    # Gera observações, com texto pre-definido, incluindo os números, das notas fiscais, recebidos no parâmetro
    def geraObservacao(self, args1):
        self.__t = ""
        if len(args1) != 0:  # Se a lista não estiver vazia
            return self.__retornaCodigos(args1) + "."
        return ""

    # Cria observação
    def __retornaCodigos(self, lista2):
        if len(lista2) >= 2:
            self.t = "Fatura das notas fiscais de simples remessa: "
        else:
            self.t = self.__umaNota

        # Acha separador
        c = ""
        for i, t2 in enumerate(lista2):
            if i == 0:
                c += str(t2)
            elif i == len(lista2) - 1:
                c += " e " + str(t2)
            else:
                c += ", " + str(t2)

        return self.t + c
