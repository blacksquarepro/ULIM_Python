'''Scrieți un program care vă permite să creați o clasă de bază, apoi adăugați un constructor, care vă permite să creați obiectul cel puțin în două moduri (de exemplu, fără parametri, cu toți parametrii indicați, cu doar câțiva parametri indicați, în dependență de temă) la această clasă. Adăugați cel puțin o metodă proprie și supraîncărcați cel puțin un operator (de exemplu + sau >). După aceasta mai adăugați o clasă care moștenește câmpurile și metodele clasei create, dar mai adaugă și careva proprietăți proprii, creând și constructorul respectiv (care să corespundă constructorului clasei de bază), apoi mai creați o clasă care moștenește caracteristicile clasei a doua, având și constructorii necesari. Tema, pe baza căreia trebuie să creați clasele, inclusiv cele derivate, precum și câmpurile obligatorii, sunt indicate în variantă (mai întâi clasa de bază, apoi prima clasă derivată, apoi a doua clasă derivată), dar se permite de creat și alte clase derivate, care să fie logic legate cu cea de bază, în dependență de imaginația studenților.

Var 2: Angajați (Nr, Nume, Prenume, Funcție, Adresă, Telefon, Salariu), Administrație (Categorie de manager, Nr. persoane aflate în conducere), respectiv Proprietari (Tip proprietar, Procent de acțiuni de care dispune)'''


class Employees:
    def __init__(self, first_name, last_name, position, address, phone, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.address = address
        self.phone = phone
        self.salary = salary

    # base class method
    def __repr__(self):
        return (f'First name: {self.first_name}\nLast name: {self.last_name}\nPosition: {self.position}\nAddress: {self.address}\nPhone: {self.phone}\nSalary: {self.salary}')


class Managers(Employees):
    def __init__(self, first_name, last_name, position, address, phone, salary, manager_type, subordinates_count):
        super().__init__(first_name, last_name, position, address, phone, salary)
        self.manager_type = manager_type
        self.subordinates_count = subordinates_count

    # override base class method
    def __repr__(self):
        return (f'{super().__repr__()}\nManager type: {self.manager_type}\nSubordinates count: {self.subordinates_count}')


class ShareHolders(Managers):
    def __init__(self, first_name, last_name, position, address, phone, salary, manager_type, subordinates_count, shareholder_type, shares_percentage):
        super().__init__(first_name, last_name, position, address,
                         phone, salary, manager_type, subordinates_count)
        self.shareholder_type = shareholder_type
        self.shares_percentage = shares_percentage

    # override base class method
    def __repr__(self):
        return (f'{super().__repr__()}\nShareholder type: {self.shareholder_type}\nShares percentage: {self.shares_percentage}')


employee = Employees('Christian', 'Scorohodco', 'CEO',
                     'Chisinau', '+37369701911', '10000 MDL')
manager = Managers('Christian', 'Scorohodco', 'CEO', 'Chisinau',
                   '+37369701911', '10000 MDL', 'IT Project Manager', 25)
shareholder = ShareHolders('Christian', 'Scorohodco', 'CEO', 'Chisinau',
                           '+37369701911', '10000 MDL', 'IT Project Manager', 25, 'Major', 100)
print(employee)
print(f'\n\n{manager}')
print(f'\n\n{shareholder}')
