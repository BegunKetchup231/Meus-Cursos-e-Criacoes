# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

primeirotermo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
decimo = primeirotermo + (10 - 1) * razao

print("Os 10 primeiros dígitos da PA são: ")

for c in range(primeirotermo, decimo + razao, razao):
    
    print(f"{c}", end= " > ")
    
print("Fim")