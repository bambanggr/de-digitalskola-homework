class SaldoMinimalKurangError(Exception):
    pass


class SaldoMelebihiMaksimalError(Exception):
    pass

class SaldoTidakCukupError(Exception):
    pass


def transfer(**data):
    # print(data)
    try:
        if(data['rekening_sumber'] < data['jumlah']):
            raise SaldoTidakCukupError
        elif((data['rekening_sumber'] - data['jumlah']) < 5000):
            raise SaldoMinimalKurangError
        elif((data['rekening_target'] + data['jumlah']) > 100000):
            raise SaldoMelebihiMaksimalError
        else:
            data['rekening_sumber'] = data['rekening_sumber']-data['jumlah']
            data['rekening_target'] = data['rekening_target']+data['jumlah']
    except Exception:
        """Other Exception"""
    return data


transfer(rekening_sumber=10000, rekening_target=1000000, jumlah=3000)