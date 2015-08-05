//
//  main.cpp
//  01 - Criptografia classica
//
//  Created by Fernando Nesi on 03/08/15.
//  Copyright (c) 2015 Fernando Nesi. All rights reserved.
//
// Desenvolver um programa com 4 tipos de criptografia classica
// 1 - Cifra de céasar
// 2 - Cifra de Transposição
// 3 - Cifra de Vigenère
// 4 - Cifra de Substituição

#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <fstream>

/*lib complementares*/
#include <sstream>
#include <string>
#include <vector>
#include <time.h>
#include <algorithm>
/*lib complementares*/
using namespace std;

#define bool int
#define TRUE 1
#define FALSE 0
vector <vector <string>> codEntrada;
vector <vector <string>> codCeasar;

void carregaEntrada(string nomeArquivo);
void imprime(vector <vector <string>> entrada);
void cifraCeasar(int key);

int main(int argc, const char * argv[]) {
    string pastaLocal = "/Users/fernandonesi/Google Drive/UFFS/12º Semestre/Segurança e auditoria de sistemas/SAS-Trabalhos/01 - Criptografia classica/";
    string num, arquivo, local, palavra;
    int chave1 = 1;
    
    cout << "\t\t\t Métodos de criptografia classica";
    cout << "\n\n 1 - Cifra de céasar";
    cout << "\n\t\t | Informe chave numerica:";
//    cin >> chave1;
    
    carregaEntrada(pastaLocal+"entrada.txt");
    imprime(codEntrada);
    cifraCeasar(chave1);
    imprime(codCeasar);
    
    
    
    
    return 1;
}


void carregaEntrada(string nomeArquivo){
    ifstream infile(nomeArquivo);
    string line;
    
    //Leitura do arquivo
    if (infile.is_open()){
        while (getline(infile, line)){
            istringstream iss(line);
            string n;
            vector<string> v;
            
            while (iss >> n){
                v.push_back(n);
            }
            codEntrada.push_back(v);
        }
        infile.close();
    }else
        cout << "\n\tArquivo não encontrado!";
}

void imprime(vector <vector <string>> entrada){
    for (int i = 0; i < entrada.size(); i++){
        for (int j = 0; j < entrada[i].size(); j++){
            cout << entrada[i][j];
        }
        cout << endl;
    }
}

void cifraCeasar(int key){
    for (int i = 0; i < codEntrada.size(); i++){
        for (int j = 0; j < codEntrada[i].size(); j++){
            codCeasar[i][j] = codEntrada[i][j]++;
        }
    }
}