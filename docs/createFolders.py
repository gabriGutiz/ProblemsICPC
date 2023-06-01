"""
Program to create all folders
"""
import os


def position_char(position) -> str:
    return chr(position + 96).upper()

def invalid_input(inp):
    print(f'Invalid input ({inp})! Try again\n')

def main():
    print('This program will create all folders needed to store all ICPC and Brazilian finals')
    while True:
        print('( i ) ICPC Finals\n( b ) Brazilian Finals\n( l ) Latin America Finals\n( e ) Exit')
        choice = input('What marathon do you want to create? ')
        if len(choice) != 1 or choice not in 'ibelIBEL':
            invalid_input(choice)
            continue
        elif choice in 'eE':
            break

        print('\n##### Expected input: "YEAR1-YEAR2" #####')
        years = input('What years do you want to create? ').split('-')
        if len(years) != 2 or [i.isnumeric() for i in years].count(True) != 2:
            invalid_input(years.join('-'))
            continue

        path = ''
        if choice in 'iI':
            path = '../ICPCFinals/'
        elif choice in 'bB':
            path = '../SouthAmerica/BrazilianFinals/'
        else:
            path = '../SouthAmerica/Finals/'

        if not os.path.exists(path):
            os.mkdir(path)

        for i in range(int(years[0]), int(years[-1])+1):
            path_year = os.path.join(path, str(i))
            if not os.path.exists(path_year):
                os.mkdir(path_year)

            path_problems = os.path.join(path_year, 'mySolutions')
            if not os.path.exists(path_problems):
                os.mkdir(path_problems)

            for j in range(1, 13):
                path_exs = os.path.join(path_problems, position_char(j))
                if not os.path.exists(path_exs):
                    os.mkdir(path_exs)

        print('All folders created!')
        break

if __name__ == '__main__':
    main()
