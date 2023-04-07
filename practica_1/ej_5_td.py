
def asignaciones(A, B, Pi):
    # Caso base:
    if len(A) == 1:
        i = 0
        for i in range(len(B)):
            tupla = [A[0], B[i]]
            linea = [tupla]
            Pi.append(linea)
            #Pi.append(linea) # vamoo
        return Pi
    else:
        ultimo_A = A[len(A)-1]
        A.pop()
        Pi = asignaciones(A,B,Pi)

        for i in range(len(B)):
            tupla = [ultimo_A, B[i]]

            for linea in Pi:
                no_esta = True
                for vec in linea:
                    if (vec[0] == ultimo_A) or (vec[1] == B[i]):
                        no_esta = False
                if (no_esta == True):

                    #copiar la linea y crear una nueva
                    bony = 0
                    for bony in range(len(A)-1):
                        nueva_linea = linea
                        #nueva_linea.append(tupla)
                        Pi.append(nueva_linea)

                    linea.append(tupla)

        #Pi = Aux
        return Pi
    
print(asignaciones([1,2,3], [4,5,6], []))

# else {
#         int num_insertar = *C.begin(); 
#         C.erase(C.begin());
#         set<set<set<int>>> aux; // { {2,1} {3} } { {2} {3, 1} } { {1,2,3} } } { {2,1} }
#         set<set<set<int>>> aux_particiones = particiones(C); //{ { {1} {2} {3} }, { {1} {2,3} } }
#         for(auto i : aux_particiones) {
#             for(auto j : i) {
#                 j.insert(num_insertar);
#                 aux.insert(i);
#                 j.erase(j.find(num_insertar));
#             }
#             set<set<int>> aux_i = i;
#             aux_i.insert({num_insertar});
#             aux.insert(aux_i);
#         }
#     return aux;
#     }


