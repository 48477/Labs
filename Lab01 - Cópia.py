{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.  Verify if a value is integer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "valor = 3.5\n",
    "int(valor) == valor"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Verify if a value is even"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "valor = 5\n",
    "valor % 2 == 0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Insert two numbers. Is the first is bigger than the second?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nº1 = 5\n",
      "nº2 = 6\n",
      "5 é menor que 6\n"
     ]
    }
   ],
   "source": [
    "valor1 = int(input(\"Nº1 = \"))\n",
    "valor2 = int(input(\"nº2 = \"))\n",
    "if valor1 >= valor2:\n",
    "    print(str(valor1) + \" é maior que \" + str(valor2))\n",
    "print(str(valor1) + \" é menor que \" + str(valor2))\n",
    "#VER COMO SE FAZ O IF NOT"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Verify if one value is multiple of another"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nº1 = 6\n",
      "nº2 = 3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "valor1 = int(input(\"Nº1 = \"))\n",
    "valor2 = int(input(\"nº2 = \"))\n",
    "valor1 % valor2 == 0 or valor2 % valor1 == 0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Calculate the interest earn by an investor that invested a capital of 200 during 3 years with an interest rate of 3%. (I= P*R*T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Receberá um juro de 18.0€\n"
     ]
    }
   ],
   "source": [
    "capital = int(200)\n",
    "tempo = int(3)\n",
    "rate = float(0.03)\n",
    "juro = str(capital * tempo * rate)\n",
    "print(\"Receberá um juro de \" + juro + \"€\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Capital that an investor obtained after investing a capital of 200 during 3 years with an interest rate of 3%. (Compound interest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Receberá um juro de 218.5454€\n"
     ]
    }
   ],
   "source": [
    "capital = int(200)\n",
    "tempo = int(3)\n",
    "rate = float(0.03)\n",
    "capitalAcumulado = capital * ((1 + rate)**tempo)\n",
    "print(\"Receberá um juro de \" + str(capitalAcumulado) + \"€\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Calculate your BMI (Body Mass Index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Qual é o teu peso kg?65\n",
      "Qual é a tua altura em m?1.90\n",
      "O teu BMI é 234.65\n"
     ]
    }
   ],
   "source": [
    "massa = float(input('Qual é o teu peso kg?'))\n",
    "altura = float(input('Qual é a tua altura em m?'))\n",
    "bmi = massa * (altura**2)\n",
    "print('O teu BMI é ' + str(bmi))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. Calcule the Golden ration:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.618033988749895\n",
      "1.618033988749895\n"
     ]
    }
   ],
   "source": [
    "gr = (1 + 5**(1/2))/2\n",
    "print(gr)\n",
    "\n",
    "#OU\n",
    "#Para usar a função sqr tem de se importar o import math\n",
    "\n",
    "import math\n",
    "gr = (1 + math.sqrt(5))/2\n",
    "print(gr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9. Calculete the NPV (Net present value) of an investment, considering an initial investment of 10000, the following: Cashflows 2000,3000, 4000, 4000 and 5000 and a discount rate of 10%."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O valor atual líquido é 3139.440301519393\n"
     ]
    }
   ],
   "source": [
    "inicial = int(10000)\n",
    "k = float(0.1)\n",
    "cash1 = int(2000) \n",
    "cash2 = int(3000)\n",
    "cash3 = int(4000)\n",
    "cash4 = int(4000)\n",
    "cash5 = int(5000)\n",
    "npv = (cash1/((1+k)**1) + (cash2/(1+k)**2) + (cash3/(1+k)**3) + (cash4/(1+k)**4) + (cash5/(1+k)**5)) - inicial\n",
    "print('O valor atual líquido é ' + str(npv))  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10. Ask the user to insert name and age. Calculate the the birth. Print a result saying the 'this person was born in'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Qual é o teu nome? Mariana\n",
      "Qual é a tua idade? 21\n",
      "Mariana nasceu em 1998\n"
     ]
    }
   ],
   "source": [
    "nome = input('Qual é o teu nome? ')\n",
    "idade = int(input('Qual é a tua idade? '))\n",
    "ano = 2019 - idade\n",
    "print(nome + ' nasceu em ' + str(ano) )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11. Ask the user to insert forenames, surnames. create a new variable (name) with your complete name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quais são os seus nomes próprios? Mariana Alexandra\n",
      "Quais são os seus apelidos? Cravo Ramos\n",
      "MARIANA ALEXANDRA CRAVO RAMOS\n",
      "Mariana Alexandra Cravo Ramos\n",
      "mariana alexandra cravo ramos\n",
      "Mariana alexandra cravo ramos\n"
     ]
    }
   ],
   "source": [
    "forename = str(input(\"Quais são os seus nomes próprios? \"))\n",
    "surname = str(input(\"Quais são os seus apelidos? \"))\n",
    "name = forename + \" \" + surname\n",
    "nameBig = name.upper()\n",
    "print(nameBIG)\n",
    "nameTitle = name.title()\n",
    "print(nameTitle)\n",
    "nameSmall = name.lower()\n",
    "print(nameSmall)\n",
    "nameCapitalize = name.capitalize()\n",
    "print(nameCapitalize)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "12. Supopose that your name is stored in the variable name. Use the follwoing method to show where in which carater appears the firts \"da\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quais são os seus nomes próprios? Mariana\n",
      "Quais são os seus apelidos? Ramos\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forename = str(input(\"Quais são os seus nomes próprios? \"))\n",
    "surname = str(input(\"Quais são os seus apelidos? \"))\n",
    "name = forename + \" \" + surname\n",
    "name.find('da')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#-1 porque o \"da\" não foi encontrado"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
