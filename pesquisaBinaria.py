def iterativeBinarySearch (alist, key):
    n = len(alist)
    low = 0
    high = n-1
    mid = (low + high) // 2
    while (low <= high):
      if key == alist [mid]:
        return mid
      elif key < alist [mid]:
        high = mid - 1
      else:
        low = mid -1
      mid = (low + high) // 2
    return not_found