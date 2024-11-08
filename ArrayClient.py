import Array
maxSize = 10
arr = Array.Array(maxSize)
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))
print("Search for 12.34 returns", arr.search(12.34))
print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)
print("Array after deletions has", len(arr), "items")
arr.traverse()

# Prueba el nuevo método getMaxNum()
print("El número más alto en la matriz es:", arr.getMaxNum())

# Prueba el nuevo método getAverageNum()
print("El promedio de los números en la matriz es:", arr.getAverageNum())

print("La cantidad de numeros:", arr.parImpar())
