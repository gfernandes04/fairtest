def fraud_check(user):
    if user.country != "Brazil":
        return True  
    return False

#implemente uma funcao com atributo usando renda como atributo sensivel
def income_fraud_check(user):
    if user.income > 50000:
        return True  
    return False

