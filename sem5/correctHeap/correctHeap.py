def correctHeap(nums: list):
    l = len(nums)
    for i in range(l // 2):
        left = 2*i + 1
        right = 2*i + 2

        if (left < l) and nums[i] < nums[left]:
            return False
        if (right < l) and nums[i] < nums[right]:
            return False
    return True

# Что-то на умном:
# (оперируем (Значение, Номер массива, Номер Элемента))
# Куча состоит из первых элементов всех массивов - мы достаём минимальный элемент
# Далее мы достаём минимальный элемент - получаем (Значение, N Массива, N Элемента)
# Добавляем в кучу следующий элемент из того же массива и по кругу