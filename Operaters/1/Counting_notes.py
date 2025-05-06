amount = int(input(f'Please enter amount for withdrawing ; '))
note_1000 = amount // 1000
note_500 = (amount % 1000) // 500
note_200 = (amount % 500) // 200
note_100 = (amount % 200) // 100
note_50 = (amount % 100) // 50
note_20 = (amount % 50) // 20
note_10 = (amount % 20) // 10
note_5 = (amount % 10) // 5
note_2 = (amount % 5)// 2
note_1 = (amount % 2)// 1
print(f"the least amount of notes needed to change {amount} = 1000tk notes => {note_1000} \n 500tk notes => {note_500} \n 200tk notes => {note_200} \n 100tk notes => {note_100} \n 50tk notes => {note_50} \n 20tk notes => {note_20} \n 10tk notes => {note_10} \n 5tk notes => {note_5} \n 2tk notes => {note_2} \n 1tk notes => {note_1} ")