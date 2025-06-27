class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def mediana_das_medianas(arr: List[int], k: int) -> int:
            if len(arr) <= 5:
                return sorted(arr, reverse=True)[k - 1]

            grupos = [arr[i:i+5] for i in range(0, len(arr), 5)]
            medianas = [sorted(grupo)[len(grupo)//2] for grupo in grupos]

            pivo = mediana_das_medianas(medianas, len(medianas)//2 + 1)

            maiores = [x for x in arr if x > pivo]
            iguais = [x for x in arr if x == pivo]
            menores = [x for x in arr if x < pivo]

            if k <= len(maiores):
                return mediana_das_medianas(maiores, k)
            elif k <= len(maiores) + len(iguais):
                return pivo
            else:
                return mediana_das_medianas(menores, k - len(maiores) - len(iguais))

        return mediana_das_medianas(nums, k)