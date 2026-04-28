while True :
  kodebarang = (input("Input Nama Barang"))
  
  match kodebarang :
    case "A01":
      print("Nama : Snack")
      print("Harga : 10000")
    case "A02":
      print("Nama : Minuman")
      print("Harga : 8000")
    case "B01":
      print("Nama : Mie Instant")
      print("Harga : 3000")
    case "B02":
      print("Nama : Sabun")
      print("Harga : 5000")
    case "C01":
      print("Nama : Shampoo")
      print("Harga : 12000")
    case _ :
      print("Barang Gada")
  
    
