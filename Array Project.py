# 陣列示例
def array_example():
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)

    # 訪問元素
    print("Element at index 2:", arr[2])

    # 修改元素
    arr[2] = 10
    print("Modified array:", arr)

    # 插入元素
    arr.insert(2, 7)
    print("Array after insertion:", arr)

    # 刪除元素
    arr.pop(2)
    print("Array after deletion:", arr)

if __name__ == "__main__":
    array_example()