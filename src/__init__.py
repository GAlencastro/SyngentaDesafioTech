class Hotel:
    def __init__ (self, nome, classificacao, rewardSemana, rewardFDS, regularSemana, regularFDS):
        self.nome = nome
        self.classificacao = classificacao
        self.rewardSemana = rewardSemana
        self.rewardFDS = rewardFDS
        self.regularSemana = regularSemana
        self.regularFDS = regularFDS

    Lakewood = ('Lakewood', 3, 80, 80, 110, 90)
    Bridgewood = ('Bridgewood', 4, 110, 50, 160, 60)
    Ridgewood = ('Ridgewood', 5, 100, 40, 220, 150)

    def getTipoDia(self, dia):
        if dia == 'sat' or dia == 'sun':
            return 'WeekEnd'
        else:
            return 'Weekday'

    def valorTotal(self, vetorInput):
        soma = 0
        tipoCliente = vetorInput[0]
        if (tipoCliente == 'Reward'):
            for i in range(1,4):
                if(self.getTipoDia(vetorInput[i]) == 'WeekEnd'):
                    soma += self.rewardFDS
                else:
                    soma += self.rewardSemana

        else: 
            for i in range(1,4):
                if(self.getTipoDia(vetorInput[i]) == 'WeekEnd'):
                    soma += self.regularFDS
                else:
                    soma += self.regularSemana
    
        return {'Nome': self.nome, 'Classificacao': self.classificacao, 'ValorTotal': soma}