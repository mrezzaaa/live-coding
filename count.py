#Soal: Jumlah Pasangan yang Mendapatkan Jumlah Tertentu
#Buat sebuah fungsi countPairs yang menerima dua parameter: sebuah array dari angka-angka (number[]) dan sebuah angka target (number). 
#Fungsi tersebut harus menghitung dan mengembalikan berapa banyak pasangan angka dalam array yang jumlahnya sama dengan angka target.
#Setiap pasangan angka hanya boleh dihitung sekali, meskipun angkanya muncul lebih dari satu kali dalam array. //Pakai List untuk cek existing atau tidak
#Contoh:
#countPairs([1, 3, 2, 2, 3, 4], 5); // Output: 2
#countPairs([1, 1, 1, 1], 2); // Output: 1
#countPairs([1, 2, 3, 4, 5], 7); // Output: 2
#Penjelasan:
#Input pertama: Pasangan yang menghasilkan jumlah 5 adalah (1, 4) dan (3, 2) (dua kali, namun hanya dihitung sekali per pasangan).
#Input kedua: Pasangan yang menghasilkan jumlah 2 adalah (1, 1) yang muncul satu kali. //berarti angka sama boleh muncul jika sesuai target.
#Input ketiga: Pasangan yang menghasilkan jumlah 7 adalah (2, 5) dan (3, 4).
#Instruksi:
#Definisikan tipe untuk parameter dan nilai kembalian.
#Gunakan pendekatan yang efisien, yaitu menghindari perhitungan yang berulang.
#Setiap pasangan (a, b) yang muncul dalam array harus dihitung hanya sekali, meskipun mereka muncul beberapa kali.  // cek existing 

from typing import List,Tuple

def countPairs(numbers:List[int], target:int)-> Tuple[int,List[int]]:
    frequent = {}
    paircount = 0
    pairs = []
    paired = set()
    # Save the frequent number and set how frequent the number
    for num in numbers:
        frequent[num] = frequent.get(num,0) + 1 # Set index and get index from frequent if exist, if not set to 0. And set default frequent number to be 1
    
    # Do the math
    for num in numbers:
        if num + num == target and (num,num) not in paired:
            paircount += 1
            paired.add((num,num))
            pairs.append(f"{num}+{num} is {num+num}")
        gap = target - num
        if gap in frequent:
            if gap > num and (gap,num) not in paired:
                paircount += 1
                paired.add((gap,num))
                pairs.append(f"{gap}+{num} is {gap+num}")




    return paircount,pairs

def printResult(numbers:List[int], target:int):
    paircount, pairs = countPairs(numbers,target)
    print(f"Array\t\t\t\t: {numbers}")
    print(f"Target\t\t\t\t: {target}")
    print(f"Paircount\t\t\t: {paircount}")
    print("\n")
    print(f"Pairs\t\t\t\t: {pairs}")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––")


printResult([1, 3, 2, 2, 3, 4], 5)
printResult([1, 1, 1, 1], 2)
printResult([1, 2, 3, 4, 5], 7)